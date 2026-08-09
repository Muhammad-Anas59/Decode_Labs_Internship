import os
from google import genai
import string
client=genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def ask_gemini(user_message):
    """Fallback: ask Gemini when no rule matches."""
    try:
        prompt = f"You are {BOT_NAME}, a friendly chatbot. Reply briefly and casually to: {user_message}"
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return "Sorry, I couldn't reach my brain right now. Try again later."
def sanitize_input(raw_input):
    """Cleans user input: lowercases and strips extra whitespace."""
    cleaned= raw_input.lower().strip()
    cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
    
    return cleaned

BOT_NAME="Anas"

responses = {
    "hello": f"Hey there! I'm {BOT_NAME}, your friendly chatbot.",
    "hi": f"Hi! {BOT_NAME} here, ready to chat.",
    "how are you": "I'm running at 100% CPU efficiency, thanks for asking! How about you?",
    "what is your name": f"I go by {BOT_NAME}. Nice to meet you!",
    "thanks":"Have a nice day",
    "thank you": "You're welcome!",
    "bye": "Goodbye! See you later. ",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}
FALLBACK_RESPONSE = "I don't understand that. Can you rephrase?"

def run_chatbot():
    print(f"{BOT_NAME}: Hi! I'm ready. Type 'bye' or 'exit' anytime to end our chat.")
    user_name = None  
    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize_input(raw_input_text)

        if clean_input in EXIT_COMMANDS:
            farewell = f"Goodbye, {user_name}! See you later." if user_name else responses.get("bye")
            print(f"{BOT_NAME}: {farewell}")
            break

        if clean_input.startswith("my name is"):
            user_name = clean_input.replace("my name is", "").strip().title()
            print(f"{BOT_NAME}: Nice to meet you, {user_name}!")
            continue

        if clean_input == "how are you" and user_name:
            print(f"{BOT_NAME}: I'm doing great, {user_name}! Thanks for asking.")
            continue

        if clean_input in responses:
            reply = responses[clean_input]
        else:
            reply = ask_gemini(raw_input_text)
        print(f"{BOT_NAME}: {reply}")

if __name__ == "__main__":
    run_chatbot()