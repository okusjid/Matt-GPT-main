from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.router import api_router

app = FastAPI(title="Matt GPT", version="1.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
