
class Statics:

    def calculateSingleProbability(message, target):
        total = len(message)
        contTarget = 0

        for letter in message:
            if(letter == target or letter == int(target)):
                contTarget += 1
        
        return contTarget/total

    def compareChanges(fontMessage, outputMessage):
        changedOnes = 0
        changedZeros = 0
        totalOnes = 0

        for i in range(len(fontMessage)):
            if(fontMessage[i] != outputMessage[i]):

                if(fontMessage[i] == '1'):
                    changedOnes += 1
                else:
                    changedZeros += 1
            else:
                if(fontMessage[i] == '1'):
                    totalOnes += 1
        changes = {
            "totalZeroes" : len(fontMessage) - totalOnes,
            "totalOnes" : totalOnes,
            "changedZeros" : changedZeros,
            "changedOnes" : changedOnes
        }

        return changes

    def buildChannelTransitionMatrix(changes):
        
        onesFontProbabillity = 0.5
        zerosFontProbabillity = 0.5

        channelTransitionMatrix = []

        for i in range(4):
            row = []
            



    


        