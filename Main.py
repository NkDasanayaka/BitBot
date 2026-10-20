from google import genai

client = genai.Client(api_key="AQ.Ab8RN6KQYHBb9jRGW6gK01FbDUotOzW-dhj32Cqf6kanx4PpSQ")
response = client.generate(text="Hello, how are you?", temperature=0.2)


chat = client.chat.create(model = "gemini-flash-latest", )

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    
    reply = chat.send_message(user_input)
    print("AI: " + reply.text)