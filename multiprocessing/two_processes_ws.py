import cv2
import asyncio
import time
import logging as log

from datetime import datetime
from multiprocessing import Process
from websockets.asyncio.server import serve, broadcast

log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
CONNECTIONS = set()
socket_addr = ("", 19205)

"""
process to capture video frames
"""
def cap():
  log.info('start to cap by new process')
  # cap = cv2.VideoCapture('rtsp://192.168.0.51:8554/live/test30')
  # while True:
  #   ret, frame = cap.read()
  while True:
    time.sleep(1)
    msg = f'Hello {datetime.now()}'
    broadcast(CONNECTIONS, msg)
    for ws in CONNECTIONS:
      ws.send(msg)
      log.info('send msg')
    log.info(f'broadcast message to clients, CONNS: {len(CONNECTIONS)}')

def startCapture():
  p = Process(target=cap)
  p.start()
  broadcast(CONNECTIONS, 'Hello')

"""
process(main process) to handle web socket
"""
async def registry(websocket):
  log.info(f'new connection: {websocket}')
  CONNECTIONS.add(websocket)
  # try:
  #   await websocket.wait_closed()
  # finally:
  #   CONNECTIONS.remove(websocket)
async def sock():
  async with serve(registry, "localhost", 19205):
    await asyncio.get_running_loop().create_future()

if __name__ == '__main__':
  log.info('start.......')
  startCapture()
  asyncio.run(sock())
  log.info('new socket server has been created')