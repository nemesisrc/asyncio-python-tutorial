import asyncio

# coroutine function
# main() returns a coroutine object
async def main():
    print("starting point of the main coroutine")



# start the eventloop and run the main coroutine
asyncio.run(main())

