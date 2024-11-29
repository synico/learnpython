import cv2
import asyncio
import logging as log

from datetime import datetime
from multiprocessing import Process
from websockets.asyncio.server import serve

log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def cap():
  log.info('start to cap')
  cap = cv2.VideoCapture('rtsp://192.168.0.51:8554/live/test30')
  while True:
    ret, frame = cap.read()
def startCapture():
  p = Process(target=cap)
  p.start()

async def websocket():
  async with serve(handler, "", 19205):
    await asyncio.get_running_loop().create_future() # run forever
    log.info('end of with serve')

async def handler(websocket):
  name = await websocket.recv()
  log.info(f'name [{name}] sent by client')

  greeting = f'Hello {name}!'

  await websocket.send(greeting)

if __name__ == '__main__':
  log.info('start.......')
  startCapture()
  asyncio.run(websocket())