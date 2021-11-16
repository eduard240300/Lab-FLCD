from grammar import Grammar


def run_menu(gr):
    options = [gr.printNonTerminals, gr.printTerminals, gr.printProductions, gr.cfgCheck, gr.printProductionsForNonTerminal]
    while True:
        print("1. Show Non Terminals")
        print("2. Show Terminals")
        print("3. Show Productions")
        print("4. CFG Check ?")
        print("5. Show Productions For Non Terminal")
        print("0. Exit")

        choice = int(input(">> "))
        if choice > len(options):
            print("Invalid command!\n")
        if choice == 0:
            return
        if choice == 5:
            nonTerminal = str(input("Non Terminal: "))
            options[choice - 1](nonTerminal)
        else:
            options[choice - 1]()


if __name__ == '__main__':
    grammar = Grammar('g1.in')
    run_menu(grammar)