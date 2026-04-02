from groq import Groq

client = Groq(api_key="Enter your API key here")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Give me a joke about cats"}
    ]
)

print("Joke:", response.choices[0].message.content)
print("Total tokens used:", response.usage.total_tokens)