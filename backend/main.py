from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any

from starlette.staticfiles import StaticFiles

# Load environment variables from .env file (if any)
load_dotenv()

class Response(BaseModel):
    result: str | None

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://smart-filechartbot-6717d0410ce8.herokuapp.com/"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="static")


@app.post("/predict", response_model = Response)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
def predict() -> Any:
  
  #implement this code block
  
  return {"result": "hello world!"}