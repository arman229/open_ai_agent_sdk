from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="mcp_tools", stateless_http=True)

@mcp.tool(name="online_researcher", description="Search the web for information")
def search_online(query: str) -> str: 
    return f"Results for {query}..."

mcp_app = mcp.streamable_http_app()