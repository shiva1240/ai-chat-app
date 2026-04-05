import os
from groq import Groq
from dotenv import load_dotenv

# Load env variables
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_response(user_message):

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # updated model
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        ai_response = completion.choices[0].message.content

        return ai_response

    except Exception as e:
        print("AI ERROR:", e)
        return f"Error: {str(e)}"