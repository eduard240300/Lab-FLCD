class FiniteAutomata:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        Q = self.parseLine(file.readline())
        E = self.parseLine(file.readline())
        q0 = file.readline().split('=')[1]
        F = self.parseLine(file.readline())
        tempS = self.parseLine(file.readline())

        S = []

        for value in tempS:
            state0 = value.split(';')[0][1:]
            number = value.split('>')[0].split(';')[1][:-1]
            state1 = value.split('>')[1]

            pair = [state0, number]
            valueToAdd = [pair, state1]
            S.append(valueToAdd)

        self.__Q = Q
        self.__E = E
        self.__q0 = q0
        self.__F = F
        self.__S = S

    def parseLine(self, line):
        return [value for value in line.split('=')[1][1:-1].split(',')]

    def printStates(self):
        print(self.__Q)

    def printFinalStates(self):
        print(self.__F)

    def printAlphabet(self):
        print(self.__E)

    def printTransitions(self):
        print(self.__S)

    def isDFA(self):
        parsedTransitions = []
        for transition in self.S:
            if transition[0] in parsedTransitions:
                return False
            parsedTransitions.append(transition[0])
        return True

    def isAccepted(self, sequence):
        if self.isDFA():
            state = self.q0
            for element in sequence:
                for transition in self.S:
                    if (state, element) == transition[0]:
                        state = transition[1]
                        break
            if state in self.F:
                print("--- Accepted")
                return True
            else:
                print("--- Not accepted")
                return False
        else:
            print("--- Not DFA!")
            return False