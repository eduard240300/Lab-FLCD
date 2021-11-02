import re
from symbolTable import symbolTable


class Analyzer:
    def __init__(self):
        self.__tokenFile = "./input/token.in"
        f = open(self.__tokenFile, "r")
        self.__tokens = f.readlines()
        for i in range(len(self.__tokens)):
            self.__tokens[i] = self.__tokens[i][:-1]
        f.close()
        self.__symbolTable = symbolTable()

    def checkProgram(self, fileName):
        error = False
        quotes = False
        index = 0
        pifKeys = []
        pifValues = []
        file = open(fileName, "r")
        allChars = ""
        while True:
            char = file.read(1)
            if not char:
                break
            allChars = allChars + char
        file.close()
        tempReadTokens = re.split(' |\n|\t', allChars)
        readTokens = []
        for token in tempReadTokens:
            if token != '':
                readTokens.append(token)
        for token in readTokens:
            if token in self.__tokens:
                pifKeys.append(token)
                pifValues.append(0)
            elif quotes:
                if token[-1] == '"':
                    quotes = False
                    bigToken = bigToken + " " + token[:-1]
                    index = index + 1
                    self.__symbolTable.add('"' + bigToken + '"')
                    pifKeys.append('"' + bigToken + '"')
                    pifValues.append(-1)
                else:
                    bigToken = bigToken + " " + token
            elif token[0] == '"':
                quotes = not quotes
                bigToken = token[1:]
            elif token[0].isnumeric() or token[0] == '-' or token[0] == '+':
                isCorrect = True
                for i in range(1, len(token)):
                    if not (token[i].isnumeric()) or token[i] == '.':
                        error = True
                        isCorrect = False
                        print("Lexical error on line a")
                if isCorrect:
                    index += 1
                    self.__symbolTable.add(token)
                    pifKeys.append(token)
                    pifValues.append(-1)
            elif token[0].isalpha():
                isCorrect = True
                for i in range(1, len(token)):
                    if not token[i].isalpha() or token[i].isnumeric():
                        error = True
                        isCorrect = False
                        print("Lexical error on line " + token)
                if isCorrect:
                    index += 1
                    self.__symbolTable.add(token)
                    pifKeys.append(token)
                    pifValues.append(-1)
            else:
                error = True
                print("Lexical error on line " + token)
        if error:
            print("The program had errors !")
        else:
            print("Lexically correct")
        self.__symbolTable.listAll("ST.out")
        self.__symbolTable.printPif(pifKeys, pifValues, "PIF.out")

