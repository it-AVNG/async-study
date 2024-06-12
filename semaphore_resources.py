import asyncio
from icecream import ic

async def access_resource(semaphore, id):
    async with semaphore:
        # simulate acessing a limted resource
        ic('accessing resource:', id)
        await asyncio.sleep(2)
        ic('releasing resource:', id)


async def main():
    semaphore = asyncio.Semaphore(3) # limit to 3 at atime
    await asyncio.gather(*(access_resource(semaphore, i) for i in range (0,5)))

if __name__ == "__main__":
    asyncio.run(main())