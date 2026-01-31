import asyncio
import random
from agents import Agent, ItemHelpers, Runner, function_tool
import time
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
import nest_asyncio

nest_asyncio.apply() 
import os
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner
import asyncio
try:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI ApI key not found")
  
    external_client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=GEMINI_API_KEY,
    )
    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash", openai_client=external_client
    )
except Exception as e:
    print("Error", e)
 
async def main():
    agent = Agent(
        name="Joker",
      
       
        model=model
        
    )

    result = Runner.run_streamed(
        agent,
        input="writ about easy on allama iqbal in 500 words",
        max_turns=1
    )
    print("=== Run starting ===")

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


    print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())