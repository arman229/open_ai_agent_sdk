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
import time
from agents import Agent, ModelSettings,function_tool
async def call_fun(n):
    if n<=1:
        return n
    return await call_fun(n-1)+await call_fun(n-2)

@function_tool
async def find_fabonci_no(no:int):
    print('fabonci no')    
    start_time = time.time()
    print(f'start time: {start_time}')
    resp = str(await call_fun(no))
    end_time = time.time()
    print(f' find_fabonci_no total time takes: {end_time-start_time:.3f}')
    return resp


@function_tool
def find_priminister(country:str):
    start_time = time.time()
    print(f'start time: {start_time}')
    print('Country priminister')    
    resp = f'Imran khan is the priminister of {country}'
    print(resp)
    end_time = time.time()
    print(f'find_priminister total time takes: {end_time-start_time:.3f}')
    return resp


 
async def mainfun():
    basic_agent = Agent(name='basic_agent',tools=[find_fabonci_no,find_priminister], instructions='you are helpful assistant ',model=model ,tool_use_behavior='stop_on_first_tool'                   )

    resp =Runner.run(basic_agent,input='we want to calculate fabonichi no of 35 and who is the priminster of pakistan ')
    print(resp.final_output)
if __name__ == '__main__':
    import asyncio
    asyncio.run(mainfun())
