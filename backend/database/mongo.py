from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_URI")

# Create MongoDB client
client = MongoClient(MONGO_URI)

# Create database
db = client["ai_chat_db"]

# Create collection
collection = db["chat_history"]