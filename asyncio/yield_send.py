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
  coro.send(None) # equals to 'next(coro)'
  coro.send('Hello')
  coro.send('World')

def func1():
  print(f'result1')
  ret = yield from request('http://test.com/foo')
  print(f'result2 of {ret}')
  ret = yield from func2(ret)
  print(f'result3 of {ret}')
  return ret

def func2(data):
  print(f'result4 of {data}')
  result = yield from request('http://test.com/' + data)
  print(f'result5 of {result}')
  return result

def request(url):
  print(f'request from {url}')
  result = yield "iojob of %s" % url
  print(f'response to {url}')
  return result

if __name__=='__main__':
  # asyncio.run(main())
  # invoke_coroutine()
  
  func = func1()
  func.send(None)
  func.send('p1')
  func.send('p2')
  func.send('p3')