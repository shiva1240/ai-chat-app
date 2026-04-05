# 🤖 AI Chat Application

A simple full-stack AI-powered chat application built using **FastAPI**, **MongoDB Atlas**, and a **JavaScript frontend**.
The app allows users to enter a username, chat with an AI model, and store conversation history in MongoDB.

---

# 📌 Features

* Simple **username-based login**
* Chat with AI model
* Chat history stored in **MongoDB Atlas**
* Load previous chat history
* Clear chat history
* REST API using **FastAPI**
* Frontend built using **HTML, CSS, JavaScript**

---

# 🛠️ Tech Stack

**Backend**

* Python
* FastAPI
* MongoDB Atlas
* PyMongo
* Uvicorn
* Groq / OpenAI API

**Frontend**

* HTML
* CSS
* JavaScript

**Database**

* MongoDB Atlas (Cloud Database)

---

# 📂 Project Structure

```
ai-chat-app/
│
├── backend/
│   │
│   ├── database/
│   │   └── mongo.py
│   │
│   ├── routes/
│   │   └── chat.py
│   │
│   ├── services/
│   │   ├── ai_service.py
│   │   └── chat_service.py
│   │
│   ├── main.py
│   ├── test_mongo.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md
```

---

# ⚙️ Prerequisites

Before running this project, make sure you have:

* Python **3.9 or higher**
* MongoDB Atlas account
* Git installed
* Groq or OpenAI API key
* Internet connection

---

# 🚀 Setup Instructions

Follow these steps to run the project on your system.

---

# Step 1 — Clone the Repository

```bash
git clone https://github.com/shiva1240/ai-chat-app
cd ai-chat-app
```

Or download the ZIP and extract it.

---

# Step 2 — Setup Backend

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

# Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4 — Configure Environment Variables

Create a file named:

```
.env
```

Inside **backend/** folder.

Add:

```
MONGO_URI=your_mongodb_connection_string
GROQ_API_KEY=your_api_key
```

Example:

```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/chatdb
GROQ_API_KEY=sk-xxxxxxxxxxxx
```

---

# Step 5 — Run Backend Server

Inside backend folder:

```bash
uvicorn main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

# Step 6 — Run Frontend

Open:

```
frontend/index.html
```

In your web browser.

You will see:

```
Login Screen → Enter Username → Start Chat
```

---

# 🌐 API Endpoints

## POST /chat

Send message to AI.

Request:

```json
{
  "username": "user1",
  "message": "Hello AI"
}
```

Response:

```json
{
  "user_message": "Hello AI",
  "ai_response": "Hello! How can I help you?"
}
```

---

## GET /history/{username}

Get chat history.

Example:

```
GET /history/user1
```

---

## DELETE /history/{username}

Clear chat history.

Example:

```
DELETE /history/user1
```

---

# 🧪 Testing MongoDB Connection

Run:

```bash
python test_mongo.py
```

Expected output:

```
Mongo insert test: Success
```

And document visible in MongoDB Atlas.

---

# 🖼️ How the Application Works

1. User enters username
2. Chat screen opens
3. User sends message
4. AI generates response
5. Messages saved in MongoDB
6. Chat history loads automatically

---

# 🔐 Notes

* This project uses **basic username login only**
* No password authentication implemented
* Designed for learning/demo purposes

---

# 🧠 Future Improvements

Possible upgrades:

* Add JWT authentication
* Add multiple chat sessions
* Add message timestamps in UI
* Deploy backend to cloud
* Deploy frontend using GitHub Pages
* Add responsive UI design

---

# 🐞 Troubleshooting

## Backend not starting

Make sure:

```
uvicorn main:app --reload
```

is run inside backend folder.

---

## MongoDB not connecting

Check:

* MongoDB URI is correct
* IP Address allowed in MongoDB Atlas
* Internet connection working

---

## Frontend shows "Error contacting server"

Make sure:

* Backend running
* CORS enabled
* API URL correct
