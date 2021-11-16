https://github.com/eduard240300/Lab-FLCD

# FiniteAutomata

### Interface: 
-	#### `printStates(): Void => Prints the states`
-	#### `printFinalStates(): Void => Prints the final states`
-	#### `printAlphabet(): Void => Prints the alphabet`
-	#### `printTransitions(Void): Prints the transitions`
-	#### `isAccepted(Sequence): Boolean => Returns True if the FA is DFA and the parameter is an accepted sequence, False otherwise`
	
### BNF: 
-	#### `Q = letter number`
-	#### `sqOfQ = Q | Q "," sqOfQ`
-	#### `SInput = "S={" sqOfQ "}"`
-	#### `E = number`
-	#### `sqOfE = E | E "," sqOfE`
-	#### `EInput = "E={" sqOfE "}"`
-	#### `Q0Input = "q0={" Q "}"`
-	#### `FInput = "F={" sqOfQ "}"`
-	#### `pair = Q ";" number`
-	#### `trans = pair ">" Q`
-	#### `sqOfTrans = trans | trans "," sqOfTrans`
-	#### `SInput = "S={" sqOfTrans "}"`
