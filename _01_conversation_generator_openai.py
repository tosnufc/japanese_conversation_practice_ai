import openai
import os
from _00_prompt import *

client = openai.OpenAI()

# gpt_model = "gpt-3.5-turbo"
gpt_model = "gpt-4o"


def get_completion(prompt, model=gpt_model, temperature=0.8):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

response = get_completion(prompt, temperature=0.7)
print(response)

# save the response to a text file named ‘conversation.txt’
with open('conversation_scripts.txt', 'w', encoding='utf-8') as f:
    f.write(response)
