



from dotenv import load_dotenv
load_dotenv()
import asyncio
import os
from contextlib import AsyncExitStack,asynccontextmanager
from mcp import ClientSession, types
from mcp.client.streamable_http import streamablehttp_client
import asyncio
from openai import AsyncOpenAI 
from agents import OpenAIChatCompletionsModel,Agent
from src.open_ai_client import MCPCLIENT

 
class MCPAgent:
    def __init__(self,gemini_api_key,chat_model,base_url,client):
        self._APIKEY = gemini_api_key,
        self.model = chat_model,
        self.base_url = base_url,
        self.mcp_client = client
        self.gemini_client =  AsyncOpenAI(
            api_key=gemini_api_key,
            base_url=base_url  
        )
        self.agent = Agent(
            name="Assistant",
            instructions="You are a helpful AI assistant that can use tools to answer questions.",
            model=OpenAIChatCompletionsModel(
                model=chat_model,
                openai_client=self.gemini_client
            )
        )
        
        
async def main(gemini_api_key,chat_model,base_url,local_url:str):
    clients = {}
   
    
    async with AsyncExitStack() as stack:
        client = await stack.enter_async_context(MCPCLIENT(local_url))
         
        # agent = MCPAgent(gemini_api_key,chat_model,base_url,client)
        # Chat = Chat()

        
    

 



if __name__ == "__main__":
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    chat_model = os.getenv('CHAT_MODEL')
    base_url = os.getenv('BASE_URL')
    local_url = 'http://localhost:8000/mcp/'
  
    asyncio.run(main(gemini_api_key,chat_model,base_url,local_url))