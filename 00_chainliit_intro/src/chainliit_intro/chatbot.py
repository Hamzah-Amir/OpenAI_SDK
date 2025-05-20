import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # Our logic here
    # Send a fake response back to user
    await cl.Message(
        content = f'Hi, How are you. I Received \"{message.content}\"',
    ).send()