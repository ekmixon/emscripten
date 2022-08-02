import socket
import sys


def listen():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(('0.0.0.0', int(sys.argv[1])))
  s.listen(10)
  while True:
    conn, address = s.accept()
    while True:
      if data := conn.recv(2048):
        conn.sendall(data)
      else:
        break
    conn.close()


if __name__ == "__main__":
  listen()
