## About Matt GPT
A custom openai Assistant API based chatbot that uses retrieval tool and acts as receptionist for merrimackroofing company.
It also has ability to notify the company about the new leads and also has ability to send the leads to the company's email.

## Features
- GPT based chatbot
- Ability to notify the company about the new leads

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
uvicorn main:app --reload
```

## Environment Variables
- `OPENAI_API_KEY` - OpenAI API Key
- `LLM_MODEL` - OpenAI Language Model
- `ASSISTANT_ID` - OpenAI Assistant ID
- `MATT_EMAIL` - Email to receive the leads
- `MAIL_USERNAME` - Email username
- `MAIL_PASSWORD` - Email password
- `MAIL_SERVER` - Email server
- `MAIL_PORT` - Email port
- `MAIL_EMAIL` - Email for mail server configuration.
- `MAIL_FROM_NAME` - Email from name to be displayed in the email.

## API Reference
Currently, the API has only one endpoint.
```http
  POST /chat
  :param message: str
  :param email: str

  :return {
    "message": str
  }
```
