

from io import StringIO
from numbers import Number
class Person:

    __dni : Number
    __name : str
    __address : str

    #Informacion reducida a bits
    __dataInBits : int

    #Informacion por separado
    __elementalSchool : bool
    __highSchool : bool
    __hasOwnHome : bool
    __hasHealthInsurance : bool
    __heWorks : bool
    __hasOwnCar: bool
    __hasAnyDisabillity: bool
    __isRetired: bool

    def __init__(self, name, address, dni, elementalSchool, highSchool, hasOwnHome, hasHealthInsurance, heWorks, hasOwnCar, hasAnyDisabillity, isRetired):
        self.__name = name
        self.__address = address
        self.__dni = dni
        self.__elementalSchool = elementalSchool
        self.__highSchool = highSchool
        self.__hasOwnHome = hasOwnHome
        self.__hasHealthInsurance = hasHealthInsurance
        self.__heWorks = heWorks
        self.__hasOwnCar = hasOwnCar
        self.__hasAnyDisabillity = hasAnyDisabillity
        self.__isRetired = isRetired

    def getName(self):
        return self.__name

    def getDni(self):
        return self.__dni

    def getAdress(self):
        return self.__address

    def getDataInBits(self):
        return self.__dataInBits

    def getElementalSchool(self):
        return self.__elementalSchool

    def getHighSchool(self):
        return self.__highSchool

    def getHasOwnHome(self):
        return self.__hasOwnHome

    def getHasHealthInsurance(self):
        return self.__hasHealthInsurance

    def getHeWorks(self):
        return self.__heWorks

    def getHasOwnCar(self):
        return self.__hasOwnCar

    def getHasAnyDisabillity(self):
        return self.__hasAnyDisabillity

    def getIsRetired(self):
        return self.__isRetired

    def setInfoInByte(self, byte):
        self.__dataInBits = byte


    def __str__(self):
        return "Nombre: "+ self.__name + " DNI: "+ self.__dni+ " Byte de informacion : " + str(self.__dataInBits)
 

