# Project #8: Streaming CLI Chatbot

A terminal-based AI chatbot built with Python and Ollama. It streams responses from a local language model and maintains conversation history across multiple turns.

## Features

- **Streaming responses:** Displays generated text as it arrives.
- **Conversation memory:** Includes previous messages in subsequent requests.
- **System prompt:** Configures the assistant as a beginner-friendly DSA tutor.
- **Reset history:** Use `/reset` to start a fresh conversation.
- **Save conversations:** Use `/save` to save message history as JSON.
- **Load conversations:** Use `/load` to restore a saved conversation.
- **Exit:** Use `/exit` to quit.

## Technology Stack

- Python 3
- Ollama Python library
- Ollama local inference server
- Llama 3.2 language model
- JSON for conversation persistence

## Prerequisites

1. Install Python 3.
2. Install Ollama.
3. Download the model:

   ```powershell
   ollama pull llama3.2:latest
   ```

4. Install the Python dependency:

   ```powershell
   python -m pip install ollama
   ```

## Run the Chatbot

Start the chatbot:

```powershell
python chatbot.py
```

Ask a DSA question, then ask a follow-up to test conversation memory.

## Commands

| Command | Description |
|---|---|
| `/reset` | Clear active conversation history |
| `/save` | Save conversation to `conversation.json` |
| `/load` | Load a previously saved conversation |
| `/exit` | Exit the chatbot |

## How It Works

1. A system message defines the DSA tutor's role.
2. The user's message is appended to conversation history.
3. Ollama receives the conversation and generates a streamed response.
4. The response is printed incrementally.
5. The complete assistant response is added to the history.
6. Conversations can optionally be saved to or loaded from JSON.

## Project Structure

```text
streaming-cli-chatbot/
├── chatbot.py
├── README.md
└── conversation.json  # Generated locally; not required in Git
```

## Learning Outcomes

- Working with a local LLM.
- Streaming model output.
- Managing chat message history.
- Writing system prompts.
- Saving and restoring JSON data.
- Building a practical command-line AI application.

**Project:** Winter Arc Challenge — Project #8 of 100