
import asyncio

from websockets.asyncio.client import connect

async def hello():
  print('starting to connect to socket server')
  uri = "ws://localhost:19205"
  async with connect(uri) as websocket:
    # await websocket.send("Nick")
    print('wait')
    greeting = await websocket.recv()
    print(f'message {greeting} from server')

if __name__ == "__main__":
  asyncio.run(hello())