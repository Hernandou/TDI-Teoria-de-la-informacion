import socket
import random
import struct
import threading

class ServerTCP:

    #Configuracion del servidor
    CHANNEL_SEED : str
    PORT : int
    HOST : str

    #Configuracion del canal
    rng_channel : int
    limit_a : int
    limit_b : int
    p_error : float

    #Configuracion del ruido por cliente 
    noise_range : int

    def __init__(self, port, host):
        self.setServerSettings(port,host)
        self.setServerSettings()
        self.setNoiseRange()

    def setNoiseRange(self):
        self.noise_range = random.Random(self.CHANNEL_SEED + 1)

    def setServerSettings(self,port, host):
        self.PORT = port
        self.HOST = host
        self.CHANNEL_SEED = 2026
    
    def channelGeneration(self):
        rng_channel = random.Random(self.CHANNEL_SEED)
        self.limit_a = rng_channel.random()
        self.limit_b = rng_channel.random()
        self.p_error = min(self.limite_a, self.limite_b) * self.rng_channel.random()

    def receiveExactly(self, socket, quantity):
        data = bytearray()
        while(data < len(quantity)):
            block = socket.recv(quantity - len(data))
            
            if(not block):
                raise ConnectionError("Conexión cerrada por el cliente.")
            
            data.extend(block)
        
        return bytes(data)

    def receiveMessage(self, socket):
        header = self.receiveExactly(socket, 4)
        size = struct.unpack("!I", header)[0]
        data = self.receiveExactly(socket, size)
        return data.decode("ascii")

    def sendMessage(self, socket, message):
        data = message.encode("ascii")
        header = struct.pack("!I", len(data))
        socket.sendall(header + data)

    def serveTheCostumer(self, customer, address):
        print(f"[+] Cliente conectado: {address[0]}:{address[1]}")

        while True:
            message = self.receiveExactly(customer)

            if(message == 'SALIR'):
                break
            
            if(not message):
                self.sendMessage(customer, "ERROR: Mensaje vacío")
                continue

            if (any(bit not in '01' for bit in message)):
                self.sendMessage(customer, "ERROR: Solo se permiten simbolos 0 y 1")
                continue

            




