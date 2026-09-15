import struct
import random
import socket
from Statics import Statics

class ClientTCP:

    PORT : str
    HOST: str
    server : socket

    def __init__(self, port, host):
        self.PORT = port
        self.HOST = host

    def startConnection(self):
        
        if((not self.PORT) or (not self.HOST)):
            raise Exception('ERROR: No se indico la direccion del HOST o el PUERTO')
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server.connect((self.HOST,self.PORT))
            print(f'-------- Conexion con el servidor {self.HOST} : {self.PORT} establecida --------')

        except Exception:
            print('No se pudo establecer una conexion con el servidor')
        except TypeError:
            print('ERROR: Error de tipos')

    def sendMessage(self, message):
        data = self.messageEncoder(message, 'ascii')
        header = struct.pack("!I", len(data))
        dataToSend = header + data
        self.server.sendall(dataToSend)

    def messageEncoder(self, message, type):
        return message.encode(type)

    def generateRandomBitSequences(self, size):
        bits = random.choices(['0', '1'], k=size)
        return ''.join(bits)

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

    def getSocket(self):
        return self.server

    def calculateOutputProbability(self, fontMessage, outputMessage):
        output = Statics.compareChanges(fontMessage, outputMessage)
        matrix = Statics.buildChannelTransitionMatrix(output)
        print('=' * 55)
        print(f'BER : errores totales / total bits de la fuente = {output["zerosToOnes"] + output["onesToZeros"]}/{len(fontMessage)} = {(output["zerosToOnes"] + output["onesToZeros"])/ len(fontMessage)}')
        print(f'Frecuencia de la fuente: P(0) = {Statics.relativeFrequency(output["sendedZeros"],len(fontMessage))}')
        print(f'Frecuencia de la fuente: P(1) = {Statics.relativeFrequency(output["sendedOnes"],len(fontMessage))}\n')

        print('Matriz de transicion de canal')
        for row in matrix:
            print(row)

        i = 1
        for row in matrix:
            print(f'Suma en fila {i}: {row[0] + row[1]}')
            i+=1
        print('\n ')
        self.showMutualInformation(fontMessage, matrix, output)
        print(f'Capacidad de canal 1 - H(p) = {self.showChannelCapacity(matrix)}')
        print('=' * 55)

    def showMutualInformation(self, fontMessage, matrix, changes):
        pz = Statics.relativeFrequency(changes['sendedZeros'], len(fontMessage))
        po = Statics.relativeFrequency(changes['sendedOnes'], len(fontMessage))

        mutualInformation = Statics.mutualInformation(matrix, pz, po)

        print(f'\nInformacion Mutua I(A,B) = H(B) - H(B|A) = {mutualInformation}')

    def showChannelCapacity(self, mct):
        return 1 - Statics.conditionalEntropy(mct[0])





