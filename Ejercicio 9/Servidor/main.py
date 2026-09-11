from socket import SO_ERROR
from Server import ServerTCP

if __name__ == '__main__':
    server = ServerTCP(5555, '0.0.0.0')
    server.startServer()