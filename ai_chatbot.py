from groq import Groq
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("🤖 AI Chatbot (type 'exit' to stop)\n")

messages = []
MAX_MEMORY = 6

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Keep memory limited
    messages = messages[-MAX_MEMORY:]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    ai_reply = response.choices[0].message.content

    # Store AI reply
    messages.append({"role": "assistant", "content": ai_reply})

    print(f"AI: {ai_reply}\n")