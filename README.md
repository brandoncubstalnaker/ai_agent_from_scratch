# Autonomous AI Agent from Scratch

A lightweight, custom-built AI Agent framework in Python using the official `google-genai` SDK and Gemini models. 

This project implements a **ReAct (Reasoning + Acting)** architecture, enabling the LLM to autonomously evaluate user prompts, determine necessary tool calls, execute function logic, and synthesize the observations into final answers.

---

## Features

- **Custom ReAct Loop:** Multi-turn autonomous execution cycle (Thought -> Action -> Observation -> Final Answer).
- **Dynamic Tool Execution:** Integrated functions for calculator evaluation and timestamp retrieval.
- **Interactive CLI Interface:** Conversational terminal interface for real-time interaction.
- **Secure Configuration:** Environment variable management to prevent API key exposure.

---

## Project Structure

- `config.py` - API key configuration and environment loading.
- `llm.py` - Core client wrapper for the Google GenAI SDK.
- `tools.py` - Tool definitions and function execution registry.
- `agent.py` - System prompt and ReAct reasoning engine loop.
- `main.py` - Interactive command-line interface.

---

## CLI Usage

Install locally in editable mode:
```bash
pip install -e .
ai-agent --help
ai-agent -p "25 * 4"
```


---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/brandoncub2021-bot/ai_agent_from_scratch.git](https://github.com/brandoncub2021-bot/ai_agent_from_scratch.git)
   cd ai_agent_from_scratch
