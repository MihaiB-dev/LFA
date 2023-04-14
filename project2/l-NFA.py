import itertools
import sys
def union_lists(*lists):
     
    # use the chain() function from itertools to concatenate all the lists
    concatenated_list = list(itertools.chain(*lists))
     
    # use the set() function to remove duplicates and convert the concatenated list to a set
    unique_set = set(concatenated_list)
     
    # convert the set back to a list and return it as the final union
    final_union = list(unique_set)
    return final_union

with open("λ-NFA/" + sys.argv[1],"r") as file:
    #read the alphabet and the states
    alphabet = file.readline().split() # read the alphabet
    states = file.readline().split() # read the states
    word = None
    #create the automata
    AUTO = {state:{letter: [] for letter in alphabet} for state in states}

    #read the roads and put the data into DFA
    for line in file.readlines():
        line = line.split()
        if len(line) == 1 and list(line[0])[0] in alphabet: #see if it's a word
            word = line[0]
        elif len(line) != 1 and line[1] in alphabet : #see if they are roads
            AUTO[line[0]][line[1]].append(line[2])
        else:
            for state in line:
                if state not in AUTO.keys():
                    break
            else:
                final_state = line

#create all the lambda-closuresle for states
#logic : for each state, it goes for each lambda road that he finds till it's formed a lambda-closures.
closures = {state:[] for state in states}
i = 0
for state in states:
    closures[state].append(states[i])
    current_state = [states[i]]
    verify = True # it will be False when there are no other roads with Lambda
    while verify:
        temp = []
        for el in current_state:
            if  AUTO[el]['L'] != []:
                temp.extend(AUTO[el]['L'])
        if temp == []: # if it didn't find another road with lambda
            verify = False
        current_state = temp
        closures[state].extend(temp)
        closures[state] = list(set(closures[state])) # remove all dublicates, 
        #if we have some roads with lambda which will contribute to a cycle, then we will have an infinite while.
        # So we must take out all the dublicates before going to the next step.
    i+=1

#tabel l-nfa
l_NFA = {state:{letter: [] for letter in alphabet if letter != "L"} for state in states}

for state in l_NFA:
    for letter in l_NFA[state]:
        #λ* it's already done in closures

        #Go with all states to each letter and verify if they appear in AUTO
        for local_state in closures[state]:
            if AUTO[local_state][letter] != []:
                l_NFA[state][letter]= union_lists(l_NFA[state][letter],AUTO[local_state][letter])
        #l*
        close_final = l_NFA[state][letter] # l* a
        temp = []
        for local_state in close_final:
            temp = union_lists(temp,closures[local_state]) 
        l_NFA[state][letter] = temp
    
#Create DFA
DFA_final = {} #λ-NFA -> DFA
DFA_final_states = []

def create_DFA(current_state):
    litere = {}
    for letter in alphabet[1:]:
        temp = []
        for local_state in current_state:
            temp = union_lists(temp,l_NFA[local_state][letter])
        litere[letter] = sorted(temp)

    string_of_states = "".join(sorted(current_state))
    DFA_final[string_of_states] = litere

    for letter in alphabet[1:]:
        state_letter = DFA_final[string_of_states][letter]
        if "".join(state_letter) not in DFA_final:
            create_DFA(state_letter)

    for local_state in current_state: #verify if the state is final.
        if local_state in final_state:
            DFA_final_states.append(string_of_states) #add the final states
            break

create_DFA(closures[states[0]]) #starts with the initial state

    
with open("DFA.dot","w") as file:
    file.write("""digraph finite_state_machine {
      fontname="Helvetica,Arial,sans-serif"
      edge [fontname="Helvetica,Arial,sans-serif"]
      rankdir=LR;
      node [shape = doublecircle];""")
    file.write(f" {' '.join(DFA_final_states)};\n node [shape = circle];\n")
    #trecem prin fiecare drum:
    for state in DFA_final:
        for letter in DFA_final[state]:
            if DFA_final[state][letter]!=[]:
                file.write(f"{state} -> {''.join(DFA_final[state][letter])} [label = \"{letter}\"];\n")
    file.write("}")


from subprocess import check_call
check_call(['dot','-Tpng','DFA.dot','-o','DFA.png'])