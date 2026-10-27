import json
from pathlib import Path

import ollama


MODEL = "llama3.2:latest"
HISTORY_FILE = Path("conversation.json")

SYSTEM_PROMPT = """
You are an expert Data Structures and Algorithms (DSA) tutor.
Teach Python and DSA to a beginner.
Explain concepts step by step, use simple examples,
and analyze time and space complexity when relevant.
Remember the conversation context when answering follow-up questions.
"""

messages = [{"role": "system", "content": SYSTEM_PROMPT}]


def stream_response():
    """Stream the assistant's answer and save it to history."""
    print("\nBot: ", end="", flush=True)
    full_response = ""

    try:
        stream = ollama.chat(
            model=MODEL,
            messages=messages,
            stream=True,
        )

        for chunk in stream:
            content = chunk["message"]["content"]
            print(content, end="", flush=True)
            full_response += content

        print()

        messages.append({
            "role": "assistant",
            "content": full_response,
        })

    except Exception as error:
        print(f"\nOllama error: {error}")
        print("Check that Ollama is running and the model is available.")


def save_conversation():
    """Save conversation history to JSON."""
    HISTORY_FILE.write_text(
        json.dumps(messages, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Conversation saved to {HISTORY_FILE.resolve()}")


def load_conversation():
    """Load a previously saved conversation."""
    global messages

    if not HISTORY_FILE.exists():
        print("No saved conversation found.")
        return

    try:
        saved_messages = json.loads(
            HISTORY_FILE.read_text(encoding="utf-8")
        )

        if (
            isinstance(saved_messages, list)
            and saved_messages
            and saved_messages[0].get("role") == "system"
            and all(
                isinstance(message, dict)
                and message.get("role") in {"system", "user", "assistant"}
                and isinstance(message.get("content"), str)
                for message in saved_messages
            )
        ):
            messages = saved_messages
            print("Previous conversation loaded.")
        else:
            print("Saved conversation has an invalid format.")

    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not load conversation: {error}")


def main():
    print("=" * 48)
    print("       STREAMING DSA TUTOR CHATBOT")
    print("=" * 48)
    print(f"Model: {MODEL}")
    print("Commands: /reset, /save, /load, /exit")

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        command = user_input.lower()

        if command == "/exit":
            print("Goodbye!")
            break

        if command == "/reset":
            messages[:] = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ]
            print("Conversation history cleared.")
            continue

        if command == "/save":
            try:
                save_conversation()
            except OSError as error:
                print(f"Could not save conversation: {error}")
            continue

        if command == "/load":
            load_conversation()
            continue

        messages.append({"role": "user", "content": user_input})
        previous_length = len(messages)

        stream_response()

        # If generation failed, don't leave an unanswered user message.
        if len(messages) == previous_length:
            messages.pop()


if __name__ == "__main__":
    main()