import asyncio
import datetime


async def say_after(delay, what):
  print(f'{what} at {datetime.datetime.now()}')
  await asyncio.sleep(delay)
async def main():
  task1 = asyncio.create_task(say_after(1, 'hello'))
  task2 = asyncio.create_task(say_after(2, 'wrold'))

  print(f"started at {datetime.datetime.now()}")
  # Wait until both tasks are completed (should take
  # around 2 seconds.)
  await task1
  await task2

  print(f"finished at {datetime.datetime.now()}")

if __name__== '__main__':
  asyncio.run(main())