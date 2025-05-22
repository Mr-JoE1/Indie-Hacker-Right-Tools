# Import necessary modules
import os
from cerebras.cloud.sdk import Cerebras
import dotenv

def load_env_variables():
    """
    Load environment variables.
    """
    dotenv.load_dotenv()

def create_cerebras_client():
    """
    Create a Cerebras client instance.
    """
    api_key = os.environ.get("CEREBRAS_API_KEY")
    if not api_key:
        raise ValueError("Environment variable CEREBRAS_API_KEY is not set")
    return Cerebras(api_key=api_key)

def process_chat(client, chat_history):
    """
    Chat with the user and handle conversation logic.
    """
    while True:
        # Get user input
        user_input = input("User: ")
        user_message = {"role": "user", "content": user_input}
        
        # Add user input to chat history
        chat_history.append(user_message)
        
        # Send request to Cerebras
        response = client.chat.completions.create(
            messages=chat_history,  # Use full history to generate response
            model="llama3.1-8b",
        )
        
        # Get assistant response and update chat history
        assistant_message = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": assistant_message})
        
        # Print assistant response
        print("Assistant:", assistant_message)
        
        # Display performance statistics
        display_performance_stats(response)

def display_performance_stats(response):
    """
    Display performance statistics: total tokens processed, time taken, and tokens processed per second.
    """
    total_tokens = response.usage.total_tokens
    total_time = response.time_info.total_time
    tokens_per_second = total_tokens / total_time if total_time > 0 else 0
    print(f"(Tokens processed per second: {tokens_per_second:.2f})\n")

def main():
    """
    Main function to start the program.
    """
    try:
        # Load environment variables
        load_env_variables()
        client = create_cerebras_client()
        chat_history = []
        process_chat(client, chat_history)
    except KeyboardInterrupt:
        print("\nProgram exited.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
