
from typing import Dict, Any
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

SYSTEM_PROMPT = """
You are a commercial quotation assistant.

Rules:
- Price per line = unit_cost × (1 + margin_pct/100) × qty
- Return:
  1. Line item totals
  2. Grand total
  3. Professional email draft in  English
- Email must summarize:
  - Total price
  - Delivery terms
  - Any specification notes
- Be concise, professional, and client-ready.
- Output JSON only and should only have the key as email and value should be an simple email draft consist of above price estimation  .
"""

def calculate_totals(payload: Dict[str, Any]) -> Dict[str, Any]:
    line_items = []
    grand_total = 0.0

    for item in payload["items"]:
        unit_price = item["unit_cost"] * (1 + item["margin_pct"] / 100)
        line_total = round(unit_price * item["qty"], 2)
        grand_total += line_total

        line_items.append({
            "sku": item["sku"],
            "qty": item["qty"],
            "unit_price": round(unit_price, 2),
            "line_total": line_total,
        })

    return {
        "currency": payload["currency"],
        "lines": line_items,
        "grand_total": round(grand_total, 2),
    }


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)



def mock_llm_response(payload: Dict[str, Any]) -> Dict[str, Any]:
    totals = calculate_totals(payload)

    en_email = f"""
            Dear {payload['client']['name']},

            Please find below our commercial offer:

            Total Amount: {totals['grand_total']} {payload['currency']}
            Delivery Terms: {payload['delivery_terms']}

            Notes:
            {payload.get('notes', 'N/A')}

            Best regards,
            Sales Team
            """.strip()


    return {"email":en_email}