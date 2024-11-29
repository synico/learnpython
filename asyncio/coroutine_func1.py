import asyncio
import datetime

async def say_after(delay, what):
  print(f'{what} at {datetime.datetime.now()}')
  await asyncio.sleep(delay)

async def main():
  print(f"started at {datetime.datetime.now()}")

  await say_after(1, 'hello')
  await say_after(2, 'world')

  print(f"finished at {datetime.datetime.now()}")

if __name__== '__main__':
  asyncio.run(main())