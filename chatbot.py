import json
import random
import re

# Load intents
with open('intents.json') as file:
    data = json.load(file)

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()

def get_response(user_input):
    user_input = clean_text(user_input)
    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern = clean_text(pattern)
            if pattern in user_input:
                return random.choice(intent['responses'])
    return "I'm not sure how to respond to that."

if __name__ == "__main__":
    print("🤖 Chatbot is ready! Type 'quit' to exit.")
    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            break
        reply = get_response(msg)
        print("Bot:", reply)
