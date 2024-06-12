import asyncio
from icecream import ic

async def fetch_data(delay):
    print("fetching data: ..")
    td = delay +3
    await asyncio.sleep(td)
    print("data fetched!")
    return {"data":"some-data",
            "delay": delay}
# coroutine function
async def main():
    print("hello from main coroutine")
    for i in range (0,5):
        task = fetch_data(i)
        print("end coroutine ", i)

        result = await(task)
        print(f"receved result: {result}")

# run the coroutine
if __name__ == "__main__":
    print("gogog")
    asyncio.run(main())