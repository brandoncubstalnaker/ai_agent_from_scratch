# Autonomous AI Agent from Scratch

A lightweight, production-grade AI Agent framework in Python supporting both local open-weights LLMs (via Ollama) and cloud providers (Gemini/OpenAI).

This project implements a **ReAct (Reasoning + Acting)** architecture with a modular **Strategy Pattern** provider layer, enabling the agent to autonomously evaluate prompts, execute dynamic tool calls, and fallback cleanly between local and cloud models.

---

## Key Features

- **Custom ReAct Loop:** Multi-turn autonomous execution cycle (`Thought` -> `Action` -> `Observation` -> `Final Answer`).
- **Decoupled Provider Architecture:** Strategy Pattern interface allowing hot-swappable execution between local models (Llama 3.2, Mistral) and cloud APIs.
- **Non-Blocking Async Streaming:** Built with `httpx.AsyncClient` utilizing HTTP chunked transfer encoding (`aiter_lines()`) to parse NDJSON streams token-by-token.
- **Fault-Tolerant Daemon Health Guards:** Proactive HTTP service checks and mid-stream socket error recovery (`RemoteProtocolError`, `ReadTimeout`).
- **Dynamic Tool Execution:** Integrated functions for calculator evaluation and runtime tool calling.
- **Secure Configuration:** Environment variable management to prevent API key exposure.

---

## 🏗️ Provider Architecture



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

- `providers.py` - Strategy pattern interfaces and Ollama/Cloud provider implementations.
- `config.py` - API key configuration and environment variable loading.
- `tools.py` - Tool definitions and function execution registry.
- `agent.py` - System prompt and ReAct reasoning engine loop.
- `test_agent.py` - Async verification script for local LLM streaming.
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
   git clone [https://github.com/brandoncubstalnaker/ai_agent_from_scratch.git](https://github.com/brandoncubstalnaker/ai_agent_from_scratch.git)
   cd ai_agent_from_scratch