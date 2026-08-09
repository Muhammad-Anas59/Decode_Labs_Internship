# Project 1: Rule-Based AI Chatbot

A rule-based chatbot built as part of the DecodeLabs AI Engineering Internship (Batch 2026). This project demonstrates deterministic control-flow logic (dictionary-based intent matching) combined with an LLM-based fallback for unmatched inputs.

## Features

- **Sanitized input handling** — lowercases, strips whitespace, and removes punctuation before matching
- **Dictionary-based knowledge base** — 7 predefined intents with O(1) lookup via `.get()`
- **Continuous loop architecture** — runs until an explicit exit command is given
- **Multi-turn memory** — remembers the user's name and personalizes later responses
- **LLM fallback** — unmatched inputs are passed to the Gemini API instead of a generic error message, with a static fallback if the API call itself fails

## Tech Stack

- Python 3
- [google-genai](https://pypi.org/project/google-genai/) — Gemini API SDK

## Setup

1. Clone/download this project and navigate into the folder:
   ```bash
   cd project1-chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

5. Set it as an environment variable:
   ```bash
   setx GEMINI_API_KEY "your-key-here"     # Windows (restart terminal after)
   export GEMINI_API_KEY="your-key-here"   # macOS/Linux
   ```

## Usage

Run the chatbot:
```bash
python main.py
```

Example conversation:
```
Anas: Hi! I'm ready. Type 'bye' or 'exit' anytime to end our chat.
You: hello
Anas: Hey there! I'm Anas, your friendly chatbot.
You: my name is anas
Anas: Nice to meet you, Anas!
You: what is the capital of france
Anas: Paris is the capital of France!
You: bye
Anas: Goodbye, Anas! See you later.
```

Type `bye`, `exit`, or `quit` at any time to end the conversation.

## Project Structure

```
project1-chatbot/
  main.py            # chatbot logic
  requirements.txt   # dependencies
  README.md          # this file
```

## Notes

- This project intentionally keeps its core logic deterministic (rule-based) rather than using an LLM for every response, in line with the goal of practicing control flow and decision-making logic. The Gemini fallback was added as an enhancement for handling out-of-scope queries.
- Never commit your API key to version control. Ensure `.env` or any file containing the key is added to `.gitignore`.