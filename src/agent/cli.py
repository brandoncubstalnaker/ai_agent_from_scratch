import argparse
import sys 
from .tools import TOOL_REGISTRY

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Autonomous ReAct AI Agent Framework CLI"
    )
    parser.add_argument(
       "-p", "--prompt",
       type=str,
       help="Prompt or expression to send to the agent"
    )
    parser.add_argument(
       "-l", "--list-tools",
       action="store_true",
       help="List all registered tools available to the agent"
    )

    args = parser.parse_args()

    if args.list_tools:
        print("Available Agent Tools:")
        for name in TOOL_REGISTRY:
            print(f" -{name}")
        sys.exit(0)

    if args.prompt:
        print(f"[Agent Initialized] Processing prompt: {args.prompt}")
        # Direct execution via tool registry for prompt testing
        result = TOOL_REGISTRY["calculator"](args.prompt)
        print(f"[Agent Output]: {result}")
        sys.exit(0)

    parser.print_help()

if __name__ == "__main__":
    main()
