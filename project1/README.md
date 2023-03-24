# Program which creates a DFA or NFA + verifies a word.

### Syntax for writing the input
  line 1: reads the alphabet separated by " ".  
  line 2: reads the states (the first one is the start state).  
  line 3 ... (n-2): reads the transitions.  
  line n-1: reads the final states.  
  line n: reads the word (optional).  
 
### Output (print in terminal)
  "Input" *word* acceptat *road*" -> if it's accepted.   
  or.  
  "Intput *word* neacceptat" -> if it's not accepted  
  e.g. of *road*: q1, q2 for DFA and q0 q1, q0 q1 q2 for NFA (each step is defined by ",")  
  
### Complexity : O(n+t) 
n -> number of letters in the word  
t -> number of states in the final road


### About the process:

The program reads from a file and gets the alphabet, states, a word and AUTO (DFA or NFA) as a dictionary. Then, AUTO will be populated with data (the transitions) 
```python
with open("nfa1.txt","r") as file:
    #citim alfabetul si starile
    alfabet = file.readline().split() # se citeste aflabetul
    stari = file.readline().split() # se citesc starile
    cuvant = None
    #cream automatul
    AUTO = {stare:{litera: [] for litera in alfabet} for stare in stari}
```

I thought about what if the user doesn't type a word. In this case, the program should see if the first node is the final one and print if the word(None) is accepted or not.
```python
drum = [] 
stare_curenta = [[stari[0]][0]] 

if cuvant is None: #check if the first node is the final one
    for stare in stare_curenta:
        if stare in stare_finala:
            print(f"Input: lambda acceptat, {', '.join([' '.join(el) for el in drum])}")
            sys.exit()
    print("Input : lambda nu este acceptat")
    sys.exit()
```

The code for verfying if the word is accepted or not:
```python
ok = False
for poz in range(0, len(cuvant)):
    mult_stari = [] #array with states (NFA)
    verify = False #verify if the road is possible
    for stare in stare_curenta: #goes with each state (for NFA)
        if  AUTO[stare][cuvant[poz]] != []: #verify if it is a transition
            verify = True
            mult_stari.extend(AUTO[stare][cuvant[poz]]) #add all the transitions (NFA)

    if verify == False: #if there are no transitions, then it will get out from the main for and print not accepted
        break
    
    if poz == len(cuvant) - 1: #if the word is finished then it will verify if one of the current states is final
        for el in mult_stari:
            if el in stare_finala:
                print(f"Input: {''.join(cuvant)} acceptat , drum : {', '.join([' '.join(el) for el in drum])}, {' '.join(mult_stari)}")
                sys.exit()

    drum.append(mult_stari) #append the current progress
    stare_curenta = mult_stari

if ok == False:
    print(f"Input: {''.join(cuvant)} neacceptat")
```

### Examples
Test for DFA : [Input DFA](https://github.com/MihaiB-dev/LFA/blob/main/project1/dfa.txt)  
Test for NFA : [Input NFA](https://github.com/MihaiB-dev/LFA/blob/main/project1/nfa1.txt)

```txt
#input DFA:
0 1 2 #alphabet
q0 q1 q2 q3 #states
q0 1 q0 |
q0 0 q1 |
q1 1 q0 | => transitions
q1 0 q2 | 
q2 2 q3 |
q1 q3   #final states
002     #word

#output: 
Input: 002 acceptat , drum : q1, q2, q3



#input NFA:
a b #alphabet
q0 q1 q2 q3 #states
q0 a q0 |
q0 b q0 |
q0 a q1 | => transitions
q1 b q2 |
q2 a q3 |
q3 b q3 |
q3 #final state
abab #word

#output:
Input: abab acceptat , drum : q0 q1, q0 q2, q0 q1 q3, q0 q2 q3
```
