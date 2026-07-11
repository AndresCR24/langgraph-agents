# LangGraph Agent

An introductory chatbot agent built with **LangGraph** and a simple graph-based
architecture. The agent connects a chatbot node with a tools node, letting it
fetch up-to-date information from the web and **send emails** on the user's
behalf.

## Overview

The graph is made up of two main nodes:

- **Chatbot Node** — Handles user interactions and query processing. It decides
  whether it can answer directly or needs to call a tool.
- **Tools Node** — Executes the tools the chatbot requests, such as:
  - **Tavily** — a search engine tool used to retrieve real-time information.
  - **Email** — an action tool used to compose and send emails.

### Flow

1. The user sends a message to the **Chatbot Node**.
2. If the chatbot needs external data or wants to perform an action, it
   delegates to the **Tools Node**.
3. The **Tools Node** runs the requested tool (e.g. calls Tavily to search, or
   sends an email), parses the result, and returns it to the **Chatbot Node**.
4. The **Chatbot Node** composes the final response for the user.

```
        ┌───────────────┐
User ──▶│  Chatbot Node │◀─────────────┐
        └───────┬───────┘              │
                │ needs a tool?        │ results
                ▼                      │
        ┌───────────────┐              │
        │   Tools Node  │──────────────┘
        └───────┬───────┘
                │
     ┌──────────┴──────────┐
     ▼                     ▼
 🔎 Tavily             ✉️ Email
 (web search)          (send emails)
```

## Tech Stack

- **Python** 3.12
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** — graph-based
  orchestration for the agent
- **[LangChain](https://python.langchain.com/)** — LLM and tool integrations
- **LLM provider** — OpenAI
- **[Tavily](https://tavily.com/)** — search engine tool for real-time answers
- **Email tool** — to compose and send emails
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — environment
  variable management
- **[uv](https://github.com/astral-sh/uv)** — dependency and environment
  management

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) installed

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd langgraph-agent

# Install dependencies
uv sync
```

### Configuration

Copy the example environment file and fill in your API keys:

```bash
cp .env.example .env
```

```env
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

### Running

```bash
uv run main.py
```

## Project Structure

```
langgraph-agent/
├── main.py           # Entry point
├── config.py         # Loads environment variables and configuration
├── pyproject.toml    # Project metadata and dependencies
├── .env.example      # Template for required environment variables
└── README.md
```

## License

This project is intended for educational purposes.
