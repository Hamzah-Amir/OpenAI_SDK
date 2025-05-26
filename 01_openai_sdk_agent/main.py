import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
load_dotenv()

gemini_api = os.environ["GEMINI_API_KEY"]

external_client = AsyncOpenAI(
    api_key=gemini_api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
urdu_agent : Agent = Agent(name="urdu assistant", instructions="You are a PHD graduate, You always talk in Roman urdu but keep conversation short")

agent = Agent(
    name="Assistant",
    instructions="You are a PHD graduate assistant, who gives concise but complete answers, keep conversation short enough",
    model=model,
    handoffs= {"roman urdu": urdu_agent},
    handoff_description="Hand off to the urdu assistant whenever the user speaks in Roman Urdu or asks for replies in Roman Urdu. The urdu assistant should always respond briefly and to the point.",
)

@cl.on_chat_start
async def handle_chat_start():
    history = cl.user_session.set('history',[])
    await cl.Message(content="Hello, How can I help you today?").send()

@cl.on_message
async def handle_message(message:cl.Message):
    history = cl.user_session.get("history")

    msg = cl.Message(content="")
    await msg.send()

    history.append({"role":"user", "content":message.content})
    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and hasattr(event.data,"delta"):
            await msg.stream_token(event.data.delta)
    
    history.append({"role":"assistant", "content":result.final_output})
    cl.user_session.set("history", history)