import chainlit as cl
from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["GROQ_API_KEY"] =("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")

@cl.on_message
async def handle_message(message: cl.Message):
    response = completion(
    model="llama3-8b-8192",
    api_base="https://api.groq.com/openai/v1",
    #api_key=os.environ["GROQ_API_KEY"],
    
    messages=[
            {"role": "user", "content": message.content}
        ]
    )
    await cl.Message(content=response["choices"][0]["message"]["content"]).send()
