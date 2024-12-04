import asyncio
import logging as log

from websockets.asyncio.client import connect

log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d) - %(message)s')
async def receiver():
  log.info('starting to receive msg')
  uri = "ws://localhost:19205"
  async with connect(uri) as websocket:
    while True:
      data = await websocket.recv(1024)
      log.info(f'receive data: {data}')

if __name__ == "__main__":
  asyncio.run(receiver())