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

class MCPCLIENT():
    def __init__(self,url):
        self.server_url = url
        self.session = None
        self.exit_stck = AsyncExitStack()
    
    async def connect(self):
        read, write, _ = await self.exit_stck.enter_async_context(streamablehttp_client(self._server_url)) 
        self.session = await self.exit_stck.enter_async_context(ClientSession(read, write))
        await self.session.initialize()

    def session(self) :
        if self.session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        return self.session

    async def list_tools(self): 
        return []

    async def call_tool(self, tool_name, tool_input) : 
        return None

    async def list_prompts(self) : 
        return []

    async def get_prompt(self, prompt_name, args ): 
        return []

    async def read_resource(self, uri ) : 
        return []

    async def cleanup(self):
        await self._exit_stack.aclose()
        self._session = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup()
        
        
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
    async with AsyncExitStack() as stack:
        client = await stack.enter_async_context(MCPCLIENT(local_url))
        agent = MCPAgent(gemini_api_key,chat_model,base_url,client)
        Chat = Chat()

        
    




if __name__ == "__main__":
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    chat_model = os.getenv('CHAT_MODEL')
    base_url = os.getenv('BASE_URL')
    local_url = 'http://localhost:8000/mcp/'
    
    asyncio.run(main(gemini_api_key,chat_model,base_url,local_url))