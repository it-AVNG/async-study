import asyncio
from icecream import ic


async def fetch_data(id, sleep_time):
    ic(f"Coroutine {id} starts")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"sample data from coroutine{id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleeptime in enumerate([2,1,3], start=1):
            ic(i , sleeptime)
            task =tg.create_task(fetch_data(id=i,sleep_time=sleeptime))
            tasks.append(task)

    # after taskgroups blocks all the tasks has been complete
    res = [task.result() for task in tasks]

    for item in res:
        ic(item)


if __name__ == "__main__":
    asyncio.run(main())