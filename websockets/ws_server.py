import asyncio
import queue
import time
import logging as log

from websockets.asyncio.server import serve
from datetime import datetime
from threading import Thread

log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d) - %(message)s')
ws_conn = set()

async def to_registry(websocket):
  log.info(f'websocket connection has been added')
  await websocket.send('connection has been built')
  ws_conn.add(websocket)
  async for msg in websocket:
    log.info(msg)
async def ws_main():
  host="localhost"
  port=19205
  async with serve(to_registry, host, port):
    await asyncio.get_running_loop().create_future()

async def send_msg():
  log.info('start thread to send message')
  while True:
    await asyncio.sleep(0.001)
    for ws in ws_conn:
      msg_to_send=f'{datetime.now()}'
      await ws.send(msg_to_send)
      log.info(f'msg[{msg_to_send}] has been sent to client')

async def all():
  await asyncio.gather(ws_main(), send_msg())

if __name__=='__main__':
  # senderThread = Thread(target=send_msg)
  # senderThread.start()
  asyncio.run(all())  