import asyncio
import time

def sync_function(test_param: str)-> str:
    print("This is a synchronous function")
    time.sleep(0.1)
    return f"Sync Result: {test_param}"

async def async_function(test_param: str)-> str:
    print("This is  an aysnchronous function")

    await asyncio.sleep(0.1)
    return f"Async Result: {test_param}"

async def main():
    sync_result=sync_function("Test")
    print(sync_result)

    coroutine_obj=async_function("Test")
    print(coroutine_obj)

    coroutine_result=await coroutine_obj
    print(coroutine_result)

    task=asyncio.create_task(async_function("Test"))
    print(task)

    task_result= await task
    print(task_result)

#Event Loop
if __name__=="__main__":
    asyncio.run(main())

