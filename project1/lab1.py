#Pe un rand se citeste tot alfabetul 
#Pe un rand se citesc toate starile : primul este starea intiala
# pe randurile urmatoare se citesc drumurile
#pe ultimul rand se citesc starile finale

with open("nfa.txt","r") as file:
    #citim alfabetul si starile
    alfabet = file.readline().split()
    stari = file.readline().split()

    #cream DFA-ul
    AUTO = {stare:{litera: [] for litera in alfabet} for stare in stari}

    #citim drumurile si punem datele in DFA
    for linie in file.readlines():
        linie = linie.split()
        if len(linie) == 1 and list(linie[0])[0] in alfabet:
            cuvant = linie[0]
        elif len(linie) != 1 and linie[1] in alfabet :
            AUTO[linie[0]][linie[1]].append(linie[2])
        else:
            for stare in linie:
                if stare not in AUTO.keys():
                    break
            else:
                stare_finala = linie
    

cuvant = list(cuvant)
print(AUTO)
drum = []
stare_curenta = [stari[0]][0]
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
