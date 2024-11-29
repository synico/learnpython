import cv2
import logging as log
import socket
import time

from datetime import datetime
from multiprocessing import Process
from websockets.asyncio.server import serve

log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
socket_addr = ("localhost", 19205)
CONNS = set()

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
    log.info(f'size of CONNS: {len(CONNS)}')

def startCapture():
  p = Process(target=cap)
  p.start()

"""
process(main process) to handle socket
"""
def sock():
  s = socket.create_socket(socket_addr)

if __name__ == '__main__':
  log.info('start.......')
  startCapture()
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(socket_addr)
  s.listen()
  while True:
    client_socket, addr = s.accept()
    CONNS.add(client_socket)
  log.info('new socket server has been created')