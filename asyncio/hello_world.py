import asyncio

from datetime import datetime

async def main():
  print(f'Hello ...{datetime.now()}')
  await asyncio.sleep(1)
  print(f'... World {datetime.now()}')

asyncio.run(main())