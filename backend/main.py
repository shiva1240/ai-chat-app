from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat import router

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Chat Backend Running"}