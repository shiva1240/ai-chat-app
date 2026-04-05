from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_service import get_ai_response
from services.chat_service import (
    save_chat,
    get_chat_history,
    clear_chat_history
)

router = APIRouter()

# Request model
class ChatRequest(BaseModel):
    username: str
    message: str


# POST /chat
@router.post("/chat")
def chat(request: ChatRequest):

    username = request.username
    user_message = request.message

    ai_response = get_ai_response(user_message)

    save_chat(username, user_message, ai_response)

    return {
        "user_message": user_message,
        "ai_response": ai_response
    }

# GET /history
@router.get("/history/{username}")
def history(username: str):

    return get_chat_history(username)


# DELETE /history
@router.delete("/history/{username}")
def delete_history(username: str):

    clear_chat_history(username)

    return {"message": "Chat history cleared"}