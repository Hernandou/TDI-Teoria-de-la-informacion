import math

class Statics:

    def relativeFrequency(ocurrences, total):
        return ocurrences / total

    def compareChanges(fontMessage, outputMessage):
        zerosToOnes = 0
        onesToZeros = 0
        sendedOnes = 0
        zerosToOnes = 0
        
        for i in range(len(fontMessage)):

            #Contadores de lo que llego mal
            if(fontMessage[i] != outputMessage[i]):

                if(outputMessage[i] == '1' and fontMessage[i] == '0'):
                    zerosToOnes += 1 #Contador de ceros que se enviaron como unos 
                elif (outputMessage[i] == '0' and fontMessage[i] == '1'):
                    onesToZeros += 1 #Contador de unos que se enviaron como ceros
            
            if(fontMessage[i] == '1'):
                sendedOnes += 1
        changes = {
            "sendedZeros" : len(fontMessage) - sendedOnes,
            "sendedOnes" : sendedOnes,
            "zerosToOnes" : zerosToOnes,
            "onesToZeros" : onesToZeros
        }

        return changes

    def buildChannelTransitionMatrix(changes):
        channelTransitionMatrix = []

        row = [] 
        calc1 = (changes['sendedZeros'] - changes['zerosToOnes']) / changes['sendedZeros'] # P(0|0)
        row.append(calc1)
        calc2 = changes['zerosToOnes'] / changes['sendedZeros'] # P(1|0)
        row.append(calc2)

        channelTransitionMatrix.append(row)

        row = []

        calc1 = changes['onesToZeros'] / changes['sendedOnes'] # P(1|0)
        row.append(calc1)
        calc2 = (changes['sendedOnes'] - changes['onesToZeros']) / changes['sendedOnes'] # P(1|1)
        row.append(calc2)

        channelTransitionMatrix.append(row)

        return channelTransitionMatrix

    #Seguimos la formula I(A,B) = H(B) - H(B|A)        
    def mutualInformation(mct, pz, po):
        [p0, p1] = Statics.symbolProbabillity(pz, po, mct)
    
        hb = Statics.outputEntropy(p0, p1)
        hba = Statics.conditionalEntropy(mct[0])

        return hb - hba
        

    #Calculamos H(B/A)
    def conditionalEntropy(mct):
        return mct[0] * math.log2(1/mct[0]) + mct[1] * math.log2(1/mct[1])


    def symbolProbabillity(pSymbol0, pSymbol1, conditionalProbabillities):
        flattenedList = sum(conditionalProbabillities, [])
        pVal0 = pSymbol0 * flattenedList[0] + pSymbol1 * flattenedList[2]
        pVal1 = pSymbol0 * flattenedList[1] + pSymbol1 * flattenedList[3]

        return [pVal0, pVal1]

    def outputEntropy(pz, po):
        return pz * math.log2(1/pz) + po * math.log2(1/po)


            



    


        