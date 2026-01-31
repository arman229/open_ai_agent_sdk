import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def my_async_context():
    print("setup")
    await asyncio.sleep(1)   
    try:
        yield "inside"
    finally:
        await asyncio.sleep(1)   
        print("cleanup")

my_async_context()

async def main():
    async with my_async_context() as value:
        print(f'value:{value}')

# asyncio.run(my_async_context())
