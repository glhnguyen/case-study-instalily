from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os

from utils.session import Session
from utils.chatbot import Chatbot

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://0.0.0.0", "chrome-extension://ljajijkjbhiocbchlljdmjdmlnadelbk"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a basic request body model for chatbot input
class Query(BaseModel):
    question: str

# initialize chatbot and db
chatbot = Chatbot()
redis_db = Session()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the PartSelect Chatbot!"}

@app.post("/ask")
async def ask_question(query: Query, request: Request, response: Response):

    session_id = request.cookies.get("session_id")
    
    if not session_id:
        session_id = redis_db.create_session()
        expiry = datetime.now(timezone.utc) + timedelta(minutes=10)
        response.set_cookie(key="session_id", value=session_id, expires=expiry)
    
    history = redis_db.get_session(f"session_{session_id}")
    question = query.question
    chat = chatbot.chat(question, history)

    previous_chat = f"""
        User: {question}
        System: {chat}
        """
    
    redis_db.update_history(session_id, previous_chat)

    return {"answer": chat}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000,
                reload=True)