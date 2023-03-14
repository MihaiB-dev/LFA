#Pe un rand se citeste tot alfabetul : primul este starea intiala
#Pe un rand se citesc toate starile
# pe randurile urmatoare se citesc drumurile
#pe ultimul rand se citesc starile finale

with open("input.txt","r") as file:
    #citim alfabetul si starile
    alfabet = file.readline().split()
    stari = file.readline().split()

    #cream DFA-ul
    DFA = {stare:{litera:[] for litera in alfabet} for stare in stari}

    #citim drumurile si punem datele in DFA
    for linie in file.readlines():
        linie = linie.split()
        if linie[1] in stari:
            DFA[linie[0]][linie[1]].append(linie[2])
        elif len(linie) != 1:
            for stare in linie:
                if stare not in DFA.keys():
                    break
            else:
                stare_finala = linie
        else:
            cuvant = linie[0]
