import time
import datetime
import os
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import logging
from multiprocessing import Process, Manager

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
tpExecutor = ThreadPoolExecutor(max_workers=8)

def f(name):
  logging.info(f'hello {name}, pid: {os.getpid()}, ppid: {os.getppid()}')
  time.sleep(3)
  logging.info(f'end of f({name})')
  return datetime.datetime.now()

def runThreadPool():
  a = tpExecutor.submit(f, 'Nick')
  # a_r = a.result()
  # logging.info(f'a:{a_r}')
  b = tpExecutor.submit(f, 'Jack')
  logging.info(f'b:')

def runThread():
  thread = Thread(target=f, args=('John',))
  thread.start()
  logging.info("thread is completed")

if __name__== '__main__':
  logging.info("test")
  logging.info(f'main pid: {os.getpid()} and ppid: {os.getppid()}')
  p = Process(target=f, args=('nick',))
  # p.start()
  # p.join()
  runThreadPool()
  # runThread()
  logging.info('main process is completed')