from finiteAutomata import FiniteAutomata


def run_menu(fa):
    options = [fa.printStates, fa.printAlphabet, fa.printTransitions, fa.printStates, fa.isAccepted]
    while True:
        print("1. Show States")
        print("2. Show Alphabet")
        print("3. Show All The Transitions")
        print("4. Show Final States")
        print("5. Is a sequence accepted?")
        print("0. Exit")

        choice = int(input(">> "))
        if choice > len(options):
            print("Invalid command!\n")
        if choice == 0:
            return
        if choice == 5:
            sequence = int(input("Sequence: "))
            options[choice - 1](sequence)
        else:
            options[choice - 1]()


if __name__ == '__main__':
    finite_automata = FiniteAutomata('fa.in')
    run_menu(finite_automata)
