from llm import LLMClient
from tools import execute_tool, TOOLS

SYSTEM_PROMPT = """
You are a helpful AI assistant with access to tools.

Available tools:
- calculator: Evaluates a mathematical expression string.
- get_time: Returns the current date and time.


To use a tool, you MUST respond in this exact format:
Action: <tool_name>
Action Input: <tool_input>

When you have the final answer for the user, respond in this exact format:
Final Answer: <your_final_response>

Always output either an Action block or a Final Answer block, never both at once.
"""


class Agent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, user_query: str, max_turns: int = 5) -> str:
        history = f"{SYSTEM_PROMPT}\nUser: {user_query}\n"

        for _ in range(max_turns):
            response = self.llm.generate(history)
            history += f"{response}\n"

            if "Final Answer:" in response:
                return response.split("Final Answer:")[1].strip()

            if "Action:" in response and "Action Input:" in response:
                lines = response.strip().split("\n")
                tool_name = ""
                tool_input = ""

                for line in lines:
                    if line.startswith("Action:"):
                        tool_name = line.replace("Action:", "").strip()

                    elif line.startswith("Action Input:"):
                        tool_input = line.replace("Action Input:", "").strip()

                if tool_name and tool_input is not None:
                    observation = execute_tool(tool_name, tool_input)
                    history += f"Observation: {observation}\n"
        return "Reached maximum turn limit without a final answer."
if __name__ == "__main__":
    agent = Agent()
    print("Agent Response:\n", agent.run("What is 45 times 89?"))
