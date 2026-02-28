import json
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException
from openai import OpenAI
from model import QuoteRequest
import os
from helper import SYSTEM_PROMPT, get_openai_client, mock_llm_response
from typing import Dict, Any
from dotenv import load_dotenv


load_dotenv() 

def Quota_Response(payload: Dict[str, Any]) -> Dict[str, Any]:
    client= get_openai_client()
    if client is None:
        return mock_llm_response(payload)
    completion=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {"role": "user", "content": json.dumps(payload)},
            
        ],
        response_format={"type": "json_object"}
    )
    print("LLM Response:", completion.choices[0].message.content)

    return json.loads(completion.choices[0].message.content)



app=FastAPI()

# client=OpenAI()



@app.get("/")
def readroot():
    return {"Hello":" World!"}

# @app.get("/items/{itemid}")
# def readitem(itemid:int,q:Union[str,None]=None):
#     return {"itemid": itemid,"q":q}

@app.post("/quota/")
async def email_quota_response(request:QuoteRequest): 
    try:
        # print("Received request:", request)
        payload = json.loads(request.json())
        print("Parsed payload:", payload)
        response=Quota_Response(payload)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8003,reload=True)