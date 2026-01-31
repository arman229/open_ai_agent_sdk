from mcp.server.fastmcp import FastMCP

mcp=FastMCP(name='mcp prompt',stateless_http = True)

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.prompt()
def summarizar(text:str)->str:
    print('summarizer fun call')
    prompt = f"""You are an helpful assistant your task is to summarize the content.
              Here is the content:
              {text}
              please use headings builtpoint and give me the response in markdown."""
              
    return prompt

@mcp.tool()
def search_online(query:str):
    return f"Results for {query}"

@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource( "docs://{doc_id}", mime_type="text/plain")
def get_doc(doc_id: str) -> str:
    return docs[doc_id]

 
mcp_app = mcp.streamable_http_app()