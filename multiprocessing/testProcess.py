import time
import os
import threading
import logging
from multiprocessing import Process, Manager

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def f(name):
  logging.info(f'hello {name}, pid: {os.getpid()}, ppid: {os.getppid()}')
  time.sleep(3)

if __name__== '__main__':
  logging.info("test")
  logging.info(f'main pid: {os.getpid()} and ppid: {os.getppid()}')
  p = Process(target=f, args=('nick',))
  p.start()
  p.join()
  manager = Manager()
  logging.info('main process is completed')