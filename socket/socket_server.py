import socket

import logging as log
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

conn = set()

tpExecutor = ThreadPoolExecutor(max_workers=4)
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d) - %(message)s')

def socket_server(host, ip):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((host, ip))
  sock.listen(1)
  log.info('wait for connecting')
  try:
    client_socket, address = sock.accept()
    conn.add(client_socket)
    log.info(f'connection from {address} has been created')
    while True:
      log.debug(f'')
  except Exception as err:
    log.info(f'error: {err}')

def send_data():
  while True:
    for sock in conn:
      msg = f'time: {datetime.now()}'
      log.info(msg)
      sock.sendall(msg)

if __name__=='__main__':
  tpExecutor.submit(socket_server, "localhost", 19205)
  tpExecutor.submit(send_data)



    