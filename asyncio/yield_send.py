import asyncio

async def async_generator():
  while True:
    print('receive signal')
    value = yield
    print(f'Received: {value}')

async def use_generator():
  gen = async_generator()
  await gen.__anext__()
  gen.asend('Hello')
  print('send Hello to yield')
  gen.asend('World')
  print('send World to yield')
  await gen.asend(None)

async def main():
  await use_generator()

def coroutine():
  print('Coroutine started')
  data = yield
  print(f'Received: {data}')
  data = yield
  print(f'Received: {data}')

def invoke_coroutine():
  coro = coroutine()
  next(coro)
  coro.send('Hello')
  # coro.send('World')

if __name__=='__main__':
  # asyncio.run(main())
  # invoke_coroutine()
  coro = coroutine()
  next(coro)
  coro.send('Hello')
  coro.send('World')