# Simple AI Chatbot for Beginners

# Dictionary of sample responses
responses = {
    "hi": "Hello! 👋 How can I help you today?",
    "hello": "Hi there! 😊",
    "how are you": "I'm doing great! Thanks for asking. How about you?",
    "bye": "Goodbye! 👋 Have a great day!",
    "your name": "I'm a simple Python chatbot created by you!"
}

print("🤖 Simple AI Chatbot")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower()  # get user input and make it lowercase
    if user_input == "bye":
        print("Bot: Goodbye! 👋 See you soon.")
        break
    response = responses.get(user_input, "I'm not sure how to respond to that 🤔")
    print("Bot:", response)
