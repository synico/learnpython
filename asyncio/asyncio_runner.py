# https://ruzhila.cn/blog/100-line-fastapi-chatroom?from=csdn_fastapi

import asyncio
import time
import logging as log

from datetime import datetime

log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d) - %(message)s')


async def main():
  log.info('start')
  await asyncio.sleep(1)
  log.info('first sleep')
  await asyncio.sleep(1)
  log.info(f'hello')
  log.info('-------------------------')

def sync_main():
  time.sleep(1)
  log.info('world')

if __name__=='__main__':
  # asyncio.run(main())
  with asyncio.Runner() as runner:
    runner.run(main())
  sync_main()