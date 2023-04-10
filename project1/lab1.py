import sys
#Pe un rand se citeste tot alfabetul 
#Pe un rand se citesc toate starile : !! primul este starea intiala !!
# pe randurile urmatoare se citesc drumurile
#pe ultimul rand se citesc starile finale

with open("nfa1.txt","r") as file:
    #citim alfabetul si starile
    alfabet = file.readline().split() # se citeste aflabetul
    stari = file.readline().split() # se citesc starile
    cuvant = None
    #cream automatul
    AUTO = {stare:{litera: [] for litera in alfabet} for stare in stari}

    #citim drumurile si punem datele in DFA
    for linie in file.readlines():
        linie = linie.split()
        if len(linie) == 1 and list(linie[0])[0] in alfabet: #vedem daca este cuvant
            cuvant = linie[0]
        elif len(linie) != 1 and linie[1] in alfabet : #vedem daca sunt drumurile
            AUTO[linie[0]][linie[1]].append(linie[2])
        else:
            for stare in linie:
                if stare not in AUTO.keys():
                    break
            else:
                stare_finala = linie

#print(AUTO)
drum = [] # se reface drumul treptat
stare_curenta = [[stari[0]][0]] #initializam cu prima stare
drum.append(stare_curenta)

if cuvant is None: #check if the first node is the final one
    for stare in stare_curenta:
        print(stare,stare_finala)
        if stare in stare_finala:
            print(f"Input: lambda acceptat, {', '.join([' '.join(el) for el in drum])}")
            sys.exit()
    print("Input : lambda nu este acceptat")
    sys.exit()

cuvant = list(cuvant) #imparte cuvantul intr-o lista de litere

# print(stare_curenta)

ok = False
for poz in range(0, len(cuvant)):
    mult_stari = [] #array with states (NFA)

    verify = False  #verify if the road is possible
    for stare in stare_curenta:#goes with each state (for NFA)
        if  AUTO[stare][cuvant[poz]] != []:#verify if it is a transition
            verify = True
            mult_stari.extend(AUTO[stare][cuvant[poz]])#add all the transitions (NFA)

    if verify == False: #if there are no transitions, then it will get out from the main for and print not accepted
        break
    
    if poz == len(cuvant) - 1:#if the word is finished then it will verify if one of the current states is final
        for el in mult_stari:
            if el in stare_finala:
                print(f"Input: {''.join(cuvant)} acceptat , drum : {', '.join([' '.join(el) for el in drum])}, {' '.join(mult_stari)}")
                sys.exit()

    drum.append(mult_stari)
    stare_curenta = mult_stari


if ok == False:
    print(f"Input: {''.join(cuvant)} neacceptat")
