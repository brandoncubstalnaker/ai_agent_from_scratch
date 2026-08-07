from typing import Callable, Dict

def calculator(expression: str) -> str:
    """Evaluates a basic mathematical expression safely."""
    try:
        allowed = set("0123456789+-*/. ()")
        if not all(c in allowed for c in expression):
            return "Error: Invalid characters in math expression."
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error executing math: {e}"

# Tool registry map
TOOL_REGISTRY: Dict[str, Callable[[str], str]] = {
    "calculator": calculator
}
