from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()


@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic operations like addition, subtraction, multiplication, and division."""
    print("Calc tool is called")
    return f"The sum of {a} and {b} is {a + b}. The difference when {b} is subtracted from {a} is {a - b}. The product of {a} and {b} is {a * b}. The quotient when {a} is divided by {b} is {a / b if b != 0 else 'undefined (cannot divide by zero)'}."


def string_reverser(input_string: str) -> str:
    """Reverses the input string."""
    print("String reverser tool is called")
    return input_string[::-1]


def greeting(name: str) -> str:
    """Generates a greeting message for the given name."""
    print("Greeting tool is called")
    return f"Hello, {name}! Nice to meet you."


def weather_info(location: str) -> str:
    """Provides a mock weather update for the given location."""
    print("Weather info tool is called")
    return f"The current weather in {location} is sunny with a temperature of 25°C."


def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculator, greeting, weather_info, string_reverser]
    agent_executor = create_react_agent(model, tools)

    print("Welcome to the AI Chat Tool! Type 'quit' to quit.")
    print("You can ask me anything, and I'll do my best to assist you.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        print("\nAI is thinking...", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):

            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(f"\nAI: {message.content}", end="")
            print()


if __name__ == "__main__":
    main()
