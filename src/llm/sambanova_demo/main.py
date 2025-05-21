# Import required modules
from openai import OpenAI  # Used to call OpenAI's API
import os  # Used to read environment variables

# Get Sambanova API key
def get_api_key():
    """
    Get the API key from environment variables
    """
    return os.environ.get("SAMBANOVA_API_KEY")

# Send a query request to Sambanova
def query_sambanova(question, api_key):
    """
    Use Sambanova's API to query answers
    :param question: User question
    :param api_key: Sambanova API key
    :return: AI-generated answer
    """
    # Create OpenAI client
    client = OpenAI(
        base_url="https://api.sambanova.ai/v1/",  # Sambanova's API base URL
        api_key=api_key,  # Use the provided API key
    )

    # Specify the model to use
    model = "Meta-Llama-3.1-405B-Instruct"

    # Set prompt information
    prompt = question

    # Request to generate a response
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",  # Specify message role as user
                "content": prompt,  # User input question
            }
        ],
        stream=True,  # Enable streaming response
    )

    # Concatenate response results
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""  # Collect generated content

    return response

# Main function
def main():
    """
    Program entry point, responsible for obtaining the API key and initiating the query
    """
    # Get API key
    api_key = get_api_key()
    if not api_key:
        print("Please set the environment variable SAMBANOVA_API_KEY")
        return

    # User question
    question = "How Xavier Niel got into tech"

    # Call the query function and print the result
    print("Querying, please wait...")
    response = query_sambanova(question, api_key)
    print("\nAI's answer:")
    print(response)

# Program execution entry point
if __name__ == "__main__":
    main()
