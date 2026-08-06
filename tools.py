import datetime

def calculator(expression: str) -> str:
    try:
        # Evaluate simple math strings safely
        result =  eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"


def get_time() -> str:
    now = datetime.datetime.now()
    return now.strftime(" %Y-%m-%d %H:%M:%S")


# Dictionary mapping tool names to python functions
TOOLS = {
    "calculator": calculator,
    "get_time": get_time
}

def execute_tool(tool_name: str, tool_input: str) -> str:
    if tool_name not in TOOLS:
       return f"Tool '{tool_name}' try again."

    tool_func = TOOLS[tool_name]


    if tool_name == "calculator":
        return tool_func(tool_input)


    elif tool_name == "get_time":
        return tool_func()

    else:
        return f"Unknown execution pattern for {tool_name}"



if __name__ == "__main__":
    print("Testing calculator:", execute_tool("calculator", "12 * 12"))
    print("Testing time:", execute_tool("get_time", ""))
