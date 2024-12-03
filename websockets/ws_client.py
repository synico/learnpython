from datetime import datetime
from websockets.sync.client import connect

if __name__ == "__main__":
  with connect(uri='ws://localhost:19205') as websocket:
    while True:
      for msg in websocket:
        print(f'{datetime.now} msg')