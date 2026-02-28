### Email Quotation Reply System Using LLM
## Project Overview

This project provides an API-based system that generates professional email replies for quotations and related business communication. It uses a Large Language Model (LLM) to analyze incoming quotation data and return structured, meaningful responses.

When no API key is provided, the system automatically switches to a mock LLM to ensure uninterrupted development and testing.

## Requirements

* Python 3.9+

* pip

* Virtual environment support

## Create Python Virtual Environment
### Bash
```bash
python -m venv venv
Activate Virtual Environment
```
### Bash (Linux / macOS)
```bash
source venv/bin/activate
```
### Bash (Windows)
```bash
venv\Scripts\activate
```
## Install Dependencies
### Bash
```bash
pip install -r requirements.txt
```

## Environment Variables Setup

* A .env.example file is provided

* Copy it and create a .env file

* Add the required API keys inside .env

* No code changes are required after adding keys

Example workflow:

* .env.example → reference template

* .env → actual secrets (not committed)

## LLM Behavior

* If a valid API key is present, the system uses OpenAI to generate intelligent email responses

* If no API key is found:

* A mock LLM response is generated

* The API continues to function normally

* Useful for local development, demos, and CI testing

## API Functionality

* Accepts structured quotation request data

* Converts request details into an LLM-friendly format

* Generates a professional quotation email response

* Returns a clean JSON response suitable for frontend or service integration

## Running the Application Locally

You can run the FastAPI application directly without any additional commands.

### Bash
```bash
python main.py
```

* The server will start locally

* Runs with auto-reload enabled for faster development

* Accessible on the configured localhost port