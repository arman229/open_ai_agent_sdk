import asyncio
async def submain(input:str)->str:
    return input
async def main(input):
    return asyncio.run(submain(input))
# if __name__ == '__main__':
#     resp = await main("what is ai")  # ❌ This gives SyntaxError in normal .py files
if __name__ == '__main__':
    result = asyncio.run(main("what is ai"))  # ✅ This is correct
    print(result)