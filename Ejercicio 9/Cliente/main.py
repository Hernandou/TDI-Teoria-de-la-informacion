from Client import ClientTCP


if __name__ == '__main__':

    clientTcp = ClientTCP(5555, 'localhost')
    clientTcp.startConnection()
    try: 

        while True:
            print('''

            -------------- Menu --------------
            1- Enviar una cadena de bits manual
            2- Enviar una cadena de bits predefinida

            3- Salir 
            ''')

            opc = int(input('>>> Ingrese una opcion: '))

            if(opc == 1):
                message = input('>>> Escriba la secuencia de bits a enviar: ')
                clientTcp.sendMessage(message)
                print("Mensaje desde el servidor: "+ clientTcp.receiveMessage(clientTcp.getSocket()))

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

                bitSequence = clientTcp.generateRandomBitSequences(size)
                print(bitSequence)
                clientTcp.sendMessage(bitSequence)
                print(clientTcp.receiveMessage(clientTcp.getSocket()))
    except Exception:
        print('ERROR: No se pudo establecer la conexion con el servidor.')
        
            

    
    