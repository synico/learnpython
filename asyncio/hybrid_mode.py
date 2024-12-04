# Asynchronous Processing and Multithreading
import asyncio
import threading
import queue
import websockets
import cv2
import logging as log

log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d) - %(message)s')
frame_queue = queue.Queue()

def video_stream(url):
  cap = cv2.VideoCapture(url)
  log.info('start to capture frame')
  while True:
    ret, frame = cap.read()
    if ret:
      frame_queue.put(frame)

async def send_frame():
  uri = 'ws://localhost:19205'
  async with websockets.connect(uri) as websocket:
    while True:
      data = frame_queue.get()
      if data is None:
        break
      await websocket.send(data)
      log.info('sent video frame')

def main():
  video_thread = threading.Thread(target=video_stream, args=(''))
  video_thread.start()

  asyncio.run(send_frame())


if __name__=='__main__':
  main()