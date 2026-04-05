from database.mongo import collection
from datetime import datetime


def save_chat(username, user_message, ai_response):

    chat_data = {
        "username": username,
        "user_message": user_message,
        "ai_response": ai_response,
        "timestamp": datetime.utcnow()
    }

    collection.insert_one(chat_data)


def get_chat_history(username):

    history = list(
        collection.find(
            {"username": username},
            {"_id": 0}
        )
    )

    return history


def clear_chat_history(username):

    collection.delete_many(
        {"username": username}
    )