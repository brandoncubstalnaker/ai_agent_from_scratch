from agent import Agent

def main():
    agent = Agent()
    print("============================================")
    print("  ARtimus Agent Ready (type 'exit' to quit)    ")
    print("============================================")

    while True:
       try:
           user_input = input("\nYou: ").strip()

           if not user_input:
               continue

           if user_input.lower() in ["exit", "quit"]:
               print("Goodbye!")
               break

           response = agent.run(user_input)
           print(f"\nAgent: {response}")

       except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
