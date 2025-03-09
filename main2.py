import chainlit as cl
from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GEMINI_API_KEY"] = "GEMINI_API_KEY"  # Load API key from .env file
@cl.on_message
async def handle_message(message: cl.Message):
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[
            {"role": "user", "content": message.content}
        ]
        
    )
    await cl.Message(content=response["choices"][0]["message"]["content"]).send()
