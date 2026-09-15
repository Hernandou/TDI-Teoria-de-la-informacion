from Client import ClientTCP


def showAllInformation(fontMessage, clienTcp, showWord = False):
    clientTcp.sendMessage(fontMessage)
    outputMessage = clientTcp.receiveMessage(clientTcp.getSocket())
    if(showWord):
        print(f'Palabra recibida: {binaryToString(outputMessage)}')
    clientTcp.calculateOutputProbability(fontMessage, outputMessage)
    
    return outputMessage
    
def stringToBinary(fontMessage):
    bitSecuence = ''
    print(f'Palabra enviada: {fontMessage}')
    for caracter in fontMessage:
        bitSecuence += format(ord(caracter), '08b')
    
    return bitSecuence

def binaryToString(outputMessage):
    outputWord = ''

    for i in range(0, len(outputMessage), 8):
        byte = outputMessage[i: i+8]
        number = int(byte,2)
        outputWord += chr(number)

    return outputWord


if __name__ == '__main__':

    clientTcp = ClientTCP(5555, 'localhost')
    clientTcp.startConnection()


    while True:
        print('''

            -------------- Menu --------------
            1- Enviar una cadena de texto manual
            2- Enviar una cadena de bits predefinida

            3- Salir 
        ''')

        opc = int(input('>>> Ingrese una opcion: '))

        if(opc == 1):
            baseString = input('>>> Escriba la secuencia de digitos a enviar: ')
            binaryFontMessage = stringToBinary(baseString)
            showAllInformation(binaryFontMessage, clientTcp, True)


        elif (opc == 2):
            size = 0
            opc2 = int(input('''
            >>> Ingrese el tamaño de la secuencia de bits aleatorios a enviar: 
            1- Secuencia de 100 bits.
            2- Secuencia de 10000 bits
            3- Secuencia de 1000000 bits
            '''))

            if(opc2 == 1):
                size = 100
            elif (opc2 == 2):
                size = 10000
            elif(opc2 == 3):
                size = 1000000
            else:
                size = 10000

            fontMessage = clientTcp.generateRandomBitSequences(size)
            showAllInformation(fontMessage, clientTcp)
            


    
        

    
    