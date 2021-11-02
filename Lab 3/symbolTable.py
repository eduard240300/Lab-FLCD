class symbolTable:
    def __init__(self):
        self.__hashMap = []
        self.__positions = 1
        self.__occupied_positions = 0
        for i in range(0, self.__positions):
            self.__hashMap.append(None)

    def resizeHashTable(self):
        oldPositions = self.__positions
        self.__positions *= 2
        oldHashMap = self.__hashMap
        self.__hashMap = []
        for i in range(0, self.__positions):
            self.__hashMap.append(None)
        self.__occupied_positions = 0
        for i in range(0, oldPositions):
            if oldHashMap[i] is not None:
                self.add(oldHashMap[i])

    def hash(self, symbol, index):
        hash1 = 0
        symbolAsString = str(symbol)
        for i in range(0, len(symbolAsString)):
            hash1 += ord(symbolAsString[i])
        return ((hash1 % self.__positions) + index) % self.__positions

    def find(self, symbol):
        hashValue = self.hash(symbol, 0)
        if self.__hashMap[hashValue] is None:
            return None
        else:
            index = 0
            while self.__hashMap[self.hash(symbol, index)] != symbol:
                if self.__hashMap[self.hash(symbol, index)] is None:
                    return None
                index += 1
            return self.hash(symbol, index)

    def listAll(self, filename):
        st = open(filename, "w")
        index = 0
        for token in self.__hashMap:
            if not(token is None):
                st.write(str(index) + " " + token + "\n")
            index = index + 1
        st.close()

    def printPif(self, pifKeys, pifValues, filename):
        pifFile = open(filename, "w")
        index = 0
        for key in pifKeys:
            if pifValues[index] == -1:
                pifFile.write(key + " " + str(self.find(key)) + '\n')
            else:
                pifFile.write(key + " " + str(pifValues[index]) + '\n')
            index = index + 1

    def add(self, symbol):
        if self.find(symbol) is not None:
            return self.find(symbol)
        else:
            index = 0
            while self.__hashMap[self.hash(symbol, index)] is not None:
                index += 1
            position = self.hash(symbol, index)
            self.__hashMap[position] = symbol
            self.__occupied_positions += 1
            if self.__occupied_positions > int(self.__positions * 3 / 4):
                self.resizeHashTable()
                return self.find(symbol)
            return position
