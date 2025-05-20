import os
from dotenv import load_dotenv
import chainlit as cl
from agents.tool import function_tool
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from openai.types.responses import ResponseTextDeltaEvent
from agents.tool import function_tool

load_dotenv()
gemini_key = os.environ["GEMINI_API_KEY"]

external_client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
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

# Defining tools
@function_tool
def get_weather(location:str,   unit:str = "C"):
    """
    Fetch the weather of the given location, also return a short description
    """
    return f"The weather in {location} is 25 {unit} currently."

@function_tool
def check_prime(number):
  """Checks if a number is prime."""
  if number <= 1:
    return f"No, the number{number} is not a prime number."
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return f"No, the number {number} is not prime."
  return f"Yes, the number {number} is a Prime number."

# Defining agent
agent = Agent(
    model=model,
    name="Assistant",
    tools=[get_weather, check_prime],
    instructions='You are a helpful assistant',
)
@cl.on_chat_start
async def handle_chat_start():
    history = cl.user_session.set("history",[])
    await cl.Message(content="HI, I am your assistant. How can I help you today!").send()

@cl.on_message
async def handle_message(message:cl.Message):
    history = cl.user_session.get("history")

    msg = cl.Message(content="")
    await msg.send()

    history.append({"role":"user", "content":message.content})
    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config,
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)
    
    history.append({"role":"assistant", "content":result.final_output})
    cl.user_session.set("history", history)