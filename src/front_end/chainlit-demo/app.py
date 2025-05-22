import chainlit as cl
from chainlit.input_widget import Select
from openai import OpenAI
import asyncio
from datetime import datetime
import speech_recognition as sr
import hashlib
import os
from pydub import AudioSegment
from pydub.playback import play

client = OpenAI()

# New function: Receive voice input and convert it to text
def save_and_convert_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)

        # Generate a hash name for the audio file
        audio_data = audio.get_wav_data()
        audio_hash = hashlib.sha256(audio_data).hexdigest()
        file_name = f"{audio_hash}.wav"

        # Save the audio file
        with open(file_name, "wb") as f:
            f.write(audio_data)

        # Use pydub to play the audio file (optional)
        audio_segment = AudioSegment.from_wav(file_name)
        play(audio_segment)

        # Convert the voice to text
        try:
            text = recognizer.recognize_google(audio, language="en-US")
            print(f"Voice to text result: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the voice")
            return "Sorry, I couldn't understand your voice."
        except sr.RequestError as e:
            print(f"Voice recognition service error: {e}")
            return "Sorry, there was an error with the voice recognition service."

async def get_data_from_openai(prompt, chat_history):
    print(chat_history)
    messages = chat_history + [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message.content

@cl.on_chat_start
async def start():
    
    # Simulate thinking time to make the user feel like the robot is thinking
    await asyncio.sleep(1)  # Simulate thinking time

    await cl.Message(
        content=f"I'm a simple chatbot. How can I assist you today?"
    ).send()

@cl.on_message
async def main(message: cl.Message, chat_history=[]):
    # New: Check if the user has selected voice input
    if message.content.lower() == "voice input":
        voice_text = save_and_convert_voice()
        message.content = voice_text
    
    # Optimized data retrieval function to support async
    response = await get_data_from_openai(message.content, chat_history)
    
    # Update chat history
    chat_history.append({"role": "user", "content": message.content})
    chat_history.append({"role": "assistant", "content": response})
    
    # Send response
    await cl.Message(content=response).send()