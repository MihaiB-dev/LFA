import sys
#Pe un rand se citeste tot alfabetul 
#Pe un rand se citesc toate starile : !! primul este starea intiala !!
# pe randurile urmatoare se citesc drumurile
#pe ultimul rand se citesc starile finale

with open("dfa.txt","r") as file:
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

print(AUTO)
drum = [] # se reface drumul treptat
stare_curenta = [stari[0]][0] #initializam cu prima stare
drum.append(stare_curenta)

if cuvant is None: #check if the first node is the final one
    if stare_curenta in stare_finala:
        print(f"Input: lambda acceptat, {' '.join(drum)}")
        sys.exit()
    else:
        print("Input : lambda nu este acceptat")
        sys.exit()

cuvant = list(cuvant) #imparte cuvantul intr-o lista de litere

# print(stare_curenta)

ok = False
for poz in range(0, len(cuvant)):

    if  AUTO[stare_curenta][cuvant[poz]] != []:
        for stare in AUTO[stare_curenta][cuvant[poz]]:
            stare_curenta = AUTO[stare_curenta][cuvant[poz]][0]
            drum.append(stare_curenta)

        if stare_curenta in stare_finala and poz == len(cuvant) - 1:
            print(f"Input: {''.join(cuvant)} acceptat, {' '.join(drum)}")
            ok = True
            break
    else:
        break

if ok == False:
    print(f"Input: {''.join(cuvant)} neacceptat")
