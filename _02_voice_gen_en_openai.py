from pathlib import Path
from openai import OpenAI
from openai import api_key
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

with open('conversation_scripts.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


def divide_list(lst, delimiter):
    try:
        # Find the index of the delimiter
        idx = lst.index(delimiter)
        # Slice the list into two parts based on the index of the delimiter
        return lst[:idx], lst[idx+1:]
    except ValueError:
        # If the delimiter is not in the list, return the original list and an empty list
        return lst, []


lst = lines
delimiter = '*****\n'
en_conv, ja_conv = divide_list(lst, delimiter)

for n in range(len(en_conv)-1):
    speech_file_path = Path(__file__).parent / f"openai_en_voice_{n}.mp3"
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="echo", # alloy, echo, fable, onyx, nova, shimmer
        input=en_conv[n],
        response_format='mp3',
    ) as response:
        response.stream_to_file(speech_file_path)
    print(f"Writing openai_en_voice_{n}.mp3...")

