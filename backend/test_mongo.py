from database.mongo import collection

test_data = {
    "user_message": "Hello",
    "ai_response": "Hi there!",
}

collection.insert_one(test_data)

print("Data inserted successfully!")