
class Statics:

    def calculateSingleProbability(message, target):
        total = len(message)
        contTarget = 0

        for letter in message:
            if(letter == target or letter == int(target)):
                contTarget += 1
        
        return contTarget/total

    


        