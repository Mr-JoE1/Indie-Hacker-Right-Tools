# Reference tutorial: https://juejin.cn/post/7444047947249385523

# Reference:
## https://juejin.cn/post/7444047947249385523
# Introduction
# This program demonstrates how to create, publish, and chat with an intelligent agent through the Coze API. It specifically includes the following main functions:
# Initialize Coze client: The program first initializes the Coze client through the initialize_coze_client() function, using the API token obtained from environment variables for authentication, and connects to Coze's China region API service.
# Upload avatar: In the upload_avatar() function, the program supports uploading a user-specified avatar file and returns the uploaded avatar ID.
# Create intelligent agent: Through the create_bot() function, the program creates a new intelligent agent in the specified workspace and assigns it an avatar, name, and prompt information (such as translation function).
# Publish intelligent agent: Using the publish_bot() function, the created intelligent agent is published as an API service, allowing users to interact with the system through this agent.
# Start conversation stream: In the start_conversation() function, the program starts a conversation stream and outputs chat messages in real time. Users can chat with the intelligent agent, and the agent will process and respond accordingly based on the prompt information.
# Main program entry: The main() function connects the above functions, completing client initialization, avatar uploading, intelligent agent creation and publishing, and conversation initiation.
# Execution process
# The program first initializes the Coze client and uploads the avatar.
# Then it creates an intelligent agent and publishes it as an API service.
# Finally, it starts a conversation stream with the intelligent agent, outputting the interaction content between the user and the agent in real time.


import os
from pathlib import Path
from cozepy import Coze, TokenAuth, BotPromptInfo, Message, ChatEventType, MessageContentType, COZE_CN_BASE_URL

def initialize_coze_client():
    """Initialize Coze client"""
    coze_api_token = os.getenv("COZE_API_TOKEN")
    if not coze_api_token:
        raise ValueError("Please set the environment variable COZE_API_TOKEN")

    return Coze(auth=TokenAuth(token=coze_api_token), base_url=COZE_CN_BASE_URL)

def upload_avatar(coze, file_path: Path):
    """Upload avatar and return avatar ID"""
    avatar = coze.files.upload(file=file_path)
    return avatar.id

def create_bot(coze, avatar_id: str, space_id: str, bot_name: str, prompt: str):
    """Create intelligent agent and return"""
    bot = coze.bots.create(
        space_id=space_id,
        name=bot_name,
        icon_file_id=avatar_id,
        prompt_info=BotPromptInfo(prompt=prompt)
    )
    return bot

def publish_bot(coze, bot):
    """Publish intelligent agent as API service"""
    coze.bots.publish(bot_id=bot.bot_id)

def start_conversation(coze, bot_id: str, user_id: str, user_message: str):
    """Start conversation stream and output messages in real time"""
    for event in coze.chat.stream(
        bot_id=bot_id,
        user_id=user_id,
        additional_messages=[Message.build_user_question_text(user_message)],
    ):
        if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
            if isinstance(event.message.content, str):
                print(event.message.content, end="", flush=True)
            elif hasattr(event.message.content, 'type') and event.message.content.type == MessageContentType.TEXT:
                print(event.message.content.text, end="", flush=True)

        if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
            print("\nConversation ended.")
            print("Token usage:", event.chat.usage.token_count)

def main():
    """Main program entry"""
    # Initialize Coze client
    coze = initialize_coze_client()

    # Upload avatar and get avatar ID
    avatar_id = upload_avatar(coze, Path("image.png"))

    # Create intelligent agent
    space_id = "xxxxxx"  # Replace with your workspace ID [Required]
    bot_name = "Translation Robot"  # Intelligent agent name [Optional]
    prompt = "You are a translation assistant, translate the following English to Chinese"  # Intelligent agent's prompt content [Optional]
    bot = create_bot(coze, avatar_id, space_id, bot_name, prompt)

    # Publish intelligent agent as API service
    publish_bot(coze, bot)

    # Start conversation stream
    user_id = "unique_user_id"  # Replace with actual user ID [Optional]
    user_message = "Please translate the following content: Hello, how are you?"  # User input message [Optional]
    start_conversation(coze, bot.bot_id, user_id, user_message)

if __name__ == "__main__":
    main()