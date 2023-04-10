with open("L-nfa.txt","r") as file:
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

#cream toate lambda-inchiderile pentru stari
#logica : pentru fiecare muchie trece prin muchiile cu Lambda si formeaza lambda-inchideri.
inchideri = [[] for stare in stari]
for i in range(len(inchideri)):
    inchideri[i].append(stari[i])
    stare_curenta = [stari[i]]
    verify = True # se va face fals atunci cand nu mai are sa treaca prin muchii cu Lambda
    while verify:
        temp = []
        for el in stare_curenta:
            if  AUTO[el]['L'] != []:
                temp.extend(AUTO[el]['L'])
        if temp == []: #daca nu a mai gasit nici o muchie cu Lambda
            verify = False
        stare_curenta = temp
        inchideri[i].extend(temp)
        inchideri[i] = list(set(inchideri[i])) # remove la dublicate, 
        #daca avem un sir de muhcii lambda care fac un ciclu, vom avea un while infinit. 
        # Deci trebuie sa extragem dublicatele inainte de a trece la urmatoarea etapa.


    #trecem prin muchiile care au lambda pe ele si punem starile in lambda-inchidere.
    


print(inchideri)

# print(AUTO)
    