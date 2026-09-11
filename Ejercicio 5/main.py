from personHandler import PersonHandler


if __name__ == '__main__':
    
    option = ''
    cut = False

    personHandler = PersonHandler()


    while(not cut):
        option = int(input(''' 
        
        ------------ Menu ------------
        1- Cargar Usuarios
        2- Generar Archivos (.json y .bin)
        3- Fin
        ------------------------------
        '''))

        if(option == 1):
            suboption = input(' ¿Desea cargar usuarios predefinidos? (s/n)')
            if(suboption == 's' or suboption == 'S'):
                personHandler.uploadPersons()
            else:
                personHandler.setPersons()

        elif (option == 2):
            personHandler.generateBinaryFile()
            personHandler.generateJsonFile()
        elif( option == 3):
            cut = True