import asyncio
from contextlib import AsyncExitStack,asynccontextmanager
from mcp import ClientSession, types
from mcp.client.streamable_http import streamablehttp_client
from pydantic import AnyUrl

class MCPCLIENT():
    def __init__(self,url):
        self.server_url = url
        self.session = None
        self.exit_stack = AsyncExitStack()
    
    async def connect(self):
        read, write, _ = await self.exit_stack.enter_async_context(streamablehttp_client(self.server_url)) 
        self.session = await self.exit_stack.enter_async_context(ClientSession(read, write))
        await self.session.initialize()

    def app_session(self) :
        if self.session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        return self.session
    async def list_tools(self): 
        resp = await self.app_session().list_tools()
        return resp.tools
 

    async def call_tool(self, tool_name, tool_input) : 
        resp = await self.app_session().call_tool(tool_name,tool_input)
        return resp
    
    async def list_prompts(self) : 
        resp = await self.app_session().list_prompts()
        return resp.prompts

    async def get_prompt(self, prompt_name, args ): 
        resp = await self.app_session().get_prompt(prompt_name,args)
        return resp.messages

    async def read_resource(self, uri) : 
        resp = await self.app_session().read_resource(AnyUrl(uri))
        return resp.contents[0]
 

    async def cleanup(self):
        await self.exit_stack.aclose()
        self.session = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup()
    
     
   
    


   

async def main(url:str):
    async with MCPCLIENT(url) as stack:
        print('hi')
        list_tool = await stack.list_tools()
        print(f'list_of_tools:{list_tool}')
        call_tools = await stack.call_tool('search_online',{'query':"hi"})
        print(f'call_tool :{call_tools}')
        prompt_list = await stack.list_prompts()
        print(f'list_prompts:{prompt_list}')
        get_prompt = await stack.get_prompt('summarizar',{'text':"Hi i am arman"})
        print(f'get_prompt:{get_prompt}') 
        read_reso = await stack.read_resource("docs://deposition.md")
        print(f'read_resource:{read_reso}')
        
 
    
if __name__ == '__main__'  :
    url = 'http://localhost:8000/mcp/'
    asyncio.run(main(url))





 