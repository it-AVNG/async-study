import asyncio
from icecream import ic


async def fetch_data(id, sleep_time):
    ic(f"Coroutine {id} starts")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"sample data from coroutine{id}"}


# async def main():
#     task1 = asyncio.create_task(fetch_data(1,2))
#     task2 = asyncio.create_task(fetch_data(2,3))
#     task3 = asyncio.create_task(fetch_data(3,1))
#     # task1 = fetch_data(1,2)
#     # task2 = fetch_data(2,3)
#     # task3 = fetch_data(3,1)

#     res2 = await task2
#     res1 = await task1
#     res3 = await task3
#     ic(res1,res2,res3)

async def main():
	res = await asyncio.gather(fetch_data(1,2),fetch_data(2,3),fetch_data(3,1))

	for item in res:
		ic(item)

if __name__ == "__main__":
    asyncio.run(main())