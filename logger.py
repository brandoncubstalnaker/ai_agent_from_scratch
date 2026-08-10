import json
import os
from datetime import datetime 
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "agent_execution.jsonl"

def log_step(step_type: str, payload: dict) -> None:
    """Logs a single ReAct execution step as a JSON line entry.

    Args:
        step_type: Catagory of step ('thought', 'tool_call', 'observation', 'final_answer')
        payload: Dict containing relevant contextual data for the step.
    """

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "step_type": step_type,
        "data": payload
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
