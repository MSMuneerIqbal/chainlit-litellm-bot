import chainlit as cl
from litellm import completion
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"  # Ensure API key is loaded

@cl.on_message
async def handle_message(message: cl.Message):
    msg = cl.Message(content="")  
    await msg.send()  # Send an empty message to start streaming

    # Streaming response from Groq API
    stream = completion(
        model="llama3-8b-8192",
        api_base="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
        messages=[{"role": "user", "content": message.content}],
        stream=True,  # Enable streaming
    )

    for chunk in stream:
        if chunk["choices"][0]["delta"].get("content"):  # Check if content exists
            await msg.stream_token(chunk["choices"][0]["delta"]["content"])

    await msg.update()  # Update the final message when done
