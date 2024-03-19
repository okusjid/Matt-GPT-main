from fastapi import APIRouter, Request

from schemas.chat import ChatRequest, ChatResponse
from services.assistant import OpenAIGpt

api_router = APIRouter()
gpt = OpenAIGpt()

@api_router.post("/chat")
async def chat(data: ChatRequest):
    try:
        response = gpt.generate(data.email, data.message)
        return ChatResponse(message=response)
    except Exception as e:
        print(e)
        return "An error occurred while processing your request. Please try again later."
    
@api_router.get("/")
async def root(request: Request):
    return {"message": "Server is running!"}