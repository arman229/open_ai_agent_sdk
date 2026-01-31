import requests

URL = 'http://localhost:8000/mcp/'
headers = {"Accept":'application/json,text/event-stream'}

# get_prompt_input={'jsonrpc':'2.0','method':'prompts/list','id':2,'params':{},}
# get_prompts = requests.post(url=URL,headers=headers,json=get_prompt_input)
# print(get_prompts.text)
  
  
call_prompt_input={'jsonrpc':'2.0','method':'prompts/get','id':3,'params':{'name':'summarizar','arguments':{'text':"Hello, I am arman. I am 24 and i am from pakistan. Pakistan is a very beautiful country it has well location with historical mountains laks and natural things."}},}
get_prompts = requests.post(url=URL,headers=headers,json=call_prompt_input)
print(get_prompts.text)
  