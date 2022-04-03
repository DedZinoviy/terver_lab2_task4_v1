from combinatoric import Combinatoric

class Probability:
    def __init__(self):
        pass


    def negativeProbability(probability):
        return 1 - probability

    def bernoulli(p, n, m):
        return Combinatoric.combinations_without_repeats(n, m) * p**m * Probability.negativeProbability(p)**(n-m)
    
    def fullProbability(hypothesisList, probabilityList):
        resultProbability = 0
        for i in range(len(hypothesisList)):
            resultProbability += hypothesisList[i] * probabilityList[i]
        return resultProbability

    def bayesFormula(neededHypotesisIndex, hypothesisList, probabilityList):
            return hypothesisList[neededHypotesisIndex] * probabilityList[neededHypotesisIndex] / Probability.fullProbability(hypothesisList, probabilityList)
