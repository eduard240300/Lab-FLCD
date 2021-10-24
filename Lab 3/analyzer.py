class Analyzer:
    def __init__(self):
        self.__tokenFile = "./input/token.in"
        f = open(self.__tokenFile, "r")
        self.__tokens = f.readlines()
        for i in range(len(self.__tokens)):
            self.__tokens[i] = self.__tokens[i][:-1]
        f.close()

    def checkProgram(self, fileName):
        PIF = open("PIF.out", "w")
        ST = open("ST.out", "w")
        file = open(fileName, "r")
        allChars=""
        while True:
            char = file.read(1)
            if not char:
                break
            allChars = allChars + char
        file.close()
        elements = allChars.split(" ")

        for element in elements:
            elemnt
        tempElements = allChars.split("\n")
        for element in tempElements:
            elements.append(element)
        tempElements = allChars.split("\t")
        for element in tempElements:
            elements.append(element)
        for element in elements:
            print(element)

