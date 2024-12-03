# coding=utf-8
import logging as log

from queue import Queue
from threading import Thread, RLock
from websockets.sync.server import serve
from websockets import ConnectionClosed

# log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - (%(pathname)s:%(lineno)d) - %(message)s')
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d) - %(message)s')

CONNS = set()
MSG_QUEUE = Queue()
def handler(websocket):
  try:
    log.info(f'conn {websocket.id} has been created, size of CONNS: {len(CONNS)}')
    CONNS.add(websocket)
    while True:
      log.info(f'state of conn: {websocket.state}')
      if websocket.state == 3:
        break
  except Exception as e:
    log.info(f'conn has been closed: {e}')
    CONNS.remove(websocket)
  finally:
    log.info(f'conn has been closed')
    CONNS.remove(websocket) 

def ws_server():
  ws_server = serve(handler, "localhost", 19205)
  server_thread = Thread(target=ws_server.serve_forever)
  server_thread.start()
  server_thread.join()

def send_data():
  while True:
    for ws in CONNS:
      log.info(f'sending data')
      if MSG_QUEUE.empty != True:
        msg = MSG_QUEUE.get()
        ws.send(msg)

if __name__== "__main__":
  ws_server()
