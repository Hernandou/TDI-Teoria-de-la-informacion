import json
from person import Person
from byteEncoder import ByteEncoder
import pickle

class PersonHandler:

    __persons = []
    __byteEncoder : ByteEncoder

    def __init__(self):
        self.__byteEncoder = ByteEncoder()
    
    def setPersons(self):
        cut = False

        while not cut:
            print("\n--- Ingreso de Nueva Persona ---")
            full_name = input('Ingresa Nombre y Apellido: ').strip()
            address = input('Ingresa Dirección: ').strip()
            dni = input('Ingresa DNI: ').strip()

            elementalSchool = input('¿Tiene Primaria completa? (s/n): ').strip().lower() in ['s', 'si', '1']
            highSchool = input('¿Tiene Secundaria completa? (s/n): ').strip().lower() in ['s', 'si', '1']
            hasOwnHome = input('¿Tiene Casa propia? (s/n): ').strip().lower() in ['s', 'si', '1']
            hasHealthInsurance = input('¿Tiene Obra social? (s/n): ').strip().lower() in ['s', 'si', '1']
            heWorks = input('¿Trabaja actualmente? (s/n): ').strip().lower() in ['s', 'si', '1']
            hasOwnCar = input('¿Tiene Auto propio? (s/n): ').strip().lower() in ['s', 'si', '1']
            hasAnyDisabillity = input('¿Tiene alguna discapacidad? (s/n): ').strip().lower() in ['s', 'si', '1']
            isRetired = input('¿Es Jubilado? (s/n): ').strip().lower() in ['s', 'si', '1']

            newPerson = Person(full_name, address, dni, elementalSchool, highSchool, hasOwnHome, hasHealthInsurance, heWorks, hasOwnCar, hasAnyDisabillity, isRetired)
            newPerson.setInfoInByte(self.checkBinaryInfo(newPerson))
            self.__persons.append(newPerson)

            resp = input('¿Quiere agregar otra persona? (s/n): ').strip().lower()
            if resp not in ['s', 'si', '1']:
                cut = True

    def uploadPersons(self):
        persons = self.openJson()
        for person in persons:
            newPerson = Person(person['full_name'], person['address'], person['dni'], person['elementalSchool'], person['highSchool'], person['hasOwnHome'], person['hasHealthInsurance'], person['heWorks'], person['hasOwnCar'], person['hasAnyDisabillity'], person['isRetired'])
            self.__persons.append(newPerson)

    def StorageBinaryInfo(self):
        for person in self.__persons:
            person.setInfoInByte(self.checkBinaryInfo(person))
            print(person)


    def checkBinaryInfo(self, person):
            resultByte = 0b00000000
            if(person.getElementalSchool()):
                resultByte = self.__byteEncoder.hasElementalSchoolComplete(resultByte)
             
            if(person.getHighSchool()):
                resultByte = self.__byteEncoder.hasHighSchoolComplete(resultByte)

            if(person.getHasOwnHome()):
                resultByte = self.__byteEncoder.hasOwnHome(resultByte)

            if(person.getHasHealthInsurance()):
                resultByte = self.__byteEncoder.hasHealthInsurance(resultByte)
            
            if(person.getHeWorks()):
                resultByte = self.__byteEncoder.heWorks(resultByte)

            if(person.getHasOwnCar()):
                resultByte = self.__byteEncoder.hasOwnCar(resultByte)

            if(person.getHasAnyDisabillity()):
                resultByte = self.__byteEncoder.hasAnyDisabillity(resultByte)
            
            if(person.getIsRetired()):
                resultByte = self.__byteEncoder.isRetired(resultByte)
            
            return resultByte

    def generateBinaryFile(self):
        with open('Ejercicio 5/files/binaryDataPersons.bin','wb') as binaryFile:
            pickle.dump(self.__persons, binaryFile)

    def generateJsonFile(self):
    
        dictList = [{
        "full_name": person.getName(), "address": person.getAdress(), "dni": person.getDni(), "elementalSchool": str(person.getElementalSchool()), "highSchool": str(person.getHighSchool()), "hasOwnHome": str(person.getHasOwnHome()), "hasHealthInsurance": str(person.getHasHealthInsurance()), "heWorks": str(person.getHeWorks()), "hasOwnCar": str(person.getHasOwnCar()), "hasAnyDisabillity": str(person.getHasAnyDisabillity()), "isRetired": str(person.getIsRetired())
        } for person in self.__persons]
        print(dictList)
        with open('Ejercicio 5/files/jsonyDataPersons.json','w') as jsonFile:
            json.dump(dictList,jsonFile)
            



    def openJson(self):
        with open('Ejercicio 5\personas.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

        
