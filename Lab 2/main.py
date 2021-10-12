from symbolTable import symbolTable


def main():
    things = []
    mySymbolTable = symbolTable()
    while True:
        choice = input("(find/add/exit) : ")
        if choice == 'find':
            symbol = input("Input symbol : ")
            print("Position is : " + str(mySymbolTable.find(symbol)))
        elif choice == 'add':
            symbol = input("Input symbol : ")
            print("Symbol is at position : " + str(mySymbolTable.add(symbol)))
        elif choice == 'exit':
            break


if __name__ == "__main__":
    main()
