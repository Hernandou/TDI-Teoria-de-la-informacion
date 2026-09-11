

class ByteEncoder:
        
    def hasElementalSchoolComplete(self, carryResult):
        elementalSchoolByte = 0b10000000
        return elementalSchoolByte | carryResult

    def hasHighSchoolComplete(self, carryResult):
        HighSchoolByte = 0b01000000
        return HighSchoolByte | carryResult

    def hasHealthInsurance(self, carryResult):
        healthInsurance = 0b00100000
        return healthInsurance | carryResult
        
    def hasOwnHome(self,carryResult):
        elementalSchoolByte = 0b00010000
        return elementalSchoolByte | carryResult

    def heWorks(self, carryResult):
        works = 0b00001000
        return works | carryResult
    
    def hasOwnCar(self, carryResult):
        ownCar = 0b00000100
        return ownCar | carryResult

    def hasAnyDisabillity(self, carryResult):
        disabillity = 0b00000010
        return disabillity | carryResult

    def isRetired(self, carryResult):
        elementalSchoolByte = 0b00000001
        return elementalSchoolByte | carryResult

    
