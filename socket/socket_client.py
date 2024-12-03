import socket

sock = socket.socket()
host = socket.gethostname()
port = 19205

sock.connect(("127.0.0.1", port))

while True:
  msg = sock.recv(1024)
  print(msg)