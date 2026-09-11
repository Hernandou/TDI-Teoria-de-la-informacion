import random
import struct
import threading
import socket

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
        self.setServerSettings(port, host)
        self.setNoiseRange()
        self.channelGeneration()


    def setNoiseRange(self):
        self.noise_range = random.Random(self.CHANNEL_SEED + 1)

    def setServerSettings(self,port, host):
        self.PORT = port
        self.HOST = host
        self.CHANNEL_SEED = 2026
    
    def channelGeneration(self):
        self.rng_channel = random.Random(self.CHANNEL_SEED)
        self.limit_a =  self.rng_channel.random()
        self.limit_b =  self.rng_channel.random()
        self.p_error = min(self.limit_a, self.limit_b) * self.rng_channel.random()

    def receiveExactly(self, socket, quantity):
        data = bytearray()
        while(len(data) < quantity):
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

        try:
            while True:
                message = self.receiveMessage(customer)

                if(message == 'SALIR'):
                    break
                
                if(not message):
                    self.sendMessage(customer, "ERROR: Mensaje vacío")
                    continue

                if (any(bit not in '01' for bit in message)):
                    self.sendMessage(customer, "ERROR: Solo se permiten simbolos 0 y 1")
                    continue

                output = []
                for bit in message:
                    if(self.noise_range.random() < self.p_error):
                        output.append("1" if bit == '0' else '0')
                    else:
                        output.append(bit)

                self.sendMessage(customer, ''.join(output))
        except (ConnectionError, OSError):
            pass
        finally:
            customer.close()
            print(f"[-] Cliente desconectado: {address[0]}:{address[1]}")

    def startServer(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.HOST, self.PORT))

        server.listen()

        print(f''' 
        
        -------- SERVIDOR - CANAL BINARIO SIMETRICO (BSC) --------
        
        - Escuchando en puerto {self.PORT}
        - La probabilidad de error (p) permanece oculta

        ----------------------------------------------------------        
        ''')

        try:
            while True:
                customer, address = server.accept()
                thread = threading.Thread( target= self.serveTheCostumer, args=(customer, address), daemon=True)
                thread.start()

        except KeyboardInterrupt:
            print(' -------------- SERVIDOR FINALIZADO --------------')




            




