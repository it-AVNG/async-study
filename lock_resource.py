import asyncio
from icecream import ic

# a shared resource
shared_warehouse = 0

# create a lock
lock =asyncio.Lock()

async def modify_warehouse(delay):
    global shared_warehouse
    async with lock:
        # critical start
        ic("resource before modification: ", shared_warehouse)
        ic("Eta:", delay)
        shared_warehouse +=1
        await asyncio.sleep(delay)
        ic("resource after modification: ", shared_warehouse)
        #critical ends

async def main():
    await asyncio.gather(*(modify_warehouse(sleep_time) for sleep_time in [2,5,1,4,3]))



if __name__ == "__main__":
    asyncio.run(main())