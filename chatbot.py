def chatbot(message):
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"
    elif "ai" in message:
        return "AI is about making machines act intelligently."
    elif "bye" in message:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand yet."

while True:
    user = input("You: ")
    reply = chatbot(user)
    print("Bot:", reply)
    if "bye" in user.lower():
        break
