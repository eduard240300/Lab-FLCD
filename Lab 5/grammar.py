class Grammar:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        N = self.parseLine(file.readline())
        E = self.parseLine(file.readline())
        S = file.readline()[2:]
        tempP = self.parseLine(file.readline())

        P = {}

        for elem in tempP:
            newElem = elem[1:-1]
            key = newElem.split('->')[0]
            value = [e for e in newElem.split('->')[1].split('|')]
            P[key] = value

        self.__N = N
        self.__E = E
        self.__S = S
        self.__P = P

    def parseLine(self, line):
        return [value for value in line.split('=')[1][1:-1].split(',')]

    def printNonTerminals(self):
        print(self.__N)

    def printTerminals(self):
        print(self.__E)

    def printProductions(self):
        print(self.__P)

    def cfgCheck(self):
        pass

    def printProductionsForNonTerminal(self, nonTerminal):
        result = ""
        if nonTerminal in self.__P.keys():
            result = result + nonTerminal
            result = result + " -> "
            for elem in self.__P[nonTerminal]:
                if result[-2] != '>':
                    result = result + " | "
                result = result + elem
            print(result)
        else:
            print(nonTerminal + " is not a non terminal !")