import asyncio
import time


async def brewcoffee():
    print("brew coffee")
    await asyncio.sleep(3)
    return "Coffee ready"


async def toastbread():
    print("toasting bread")
    await asyncio.sleep(2)
    return "Toasted bread ready"


async def main():
    start_time = time.time()

    coffee_task = asyncio.create_task(brewcoffee())
    bread_task = asyncio.create_task(toastbread())

    result_coffee = await coffee_task
    result_bread = await bread_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"result of brew coffe is {result_coffee}")
    print(f"result of toast bread is {result_bread}")
    print(f"total of execution is {elapsed_time}")


if __name__ == '__main__':
    asyncio.run(main())
