import asyncio
from icecream import ic


async def waiter(event):
    ic('I waiter for event to set from waiter()')
    await event.wait()
    ic('Event has been set, I continue from waiter')

async def setter(event):
    await asyncio.sleep(2)
    event.set()
    ic('I set the event from setter()')

async def main():
    event = asyncio.Event()
    await ic(asyncio.gather(waiter(event), setter(event)))

if __name__ == "__main__":
    asyncio.run(main())