import sys
# Gramatici regulate A -> aB | a | λ
# G = (N,T,S,P)
# N = multimea de simboluri netermminale
# T = multimea de simboluri terminale
# S apartine N simbolul de start
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

neterminals = {}
words = []
with open("gramatici/" + sys.argv[1],"r") as file:
    for line in file.readlines():
        line = line.split()
        if len(line) == 1: #we know is a word
            words.append(line[0])
        else: #we know is part of the langauge
            neterminals[line[0]] = [line[i] for i in range(1,len(line))]

S = next(iter(neterminals)) #the first neterminal
for word in words: #verify for word if it's in the language
    faster = 0 #if we accept the word faster than in the end 
    neterminals_current = [S]
    for poz in range(len(word)): #verify untill we are at the end of the word
        temp_neterm = []
        for neterminal_val in neterminals_current: #trece prin fiecare neterminal curent
            for element in neterminals[neterminal_val]:
                if len(element) == 2 and element[0] == word[poz]:#add neterminals to the temp_neterm
                    temp_neterm.append(element[1])
                if len(element) == 1 and element[0] == word[poz]: #daca ultima litera este corecta si in gramatica
                    if poz == len(word) - 1: 
                        print(f"{bcolors.OKGREEN}{word}{bcolors.ENDC} is accepted 👍😃")
                        faster = 1
                        break
        if neterminals_current == [] and poz != len(word) - 1:
            print(f"{bcolors.FAIL}{word}{bcolors.ENDC} is not accepted 😔😔")
            faster = True
            break
        neterminals_current = temp_neterm 
    if faster == False:
        for neterminal_val in neterminals_current:
            if 'λ' in neterminals[neterminal_val]:
                print(f"{bcolors.OKGREEN}{word}{bcolors.ENDC} is accepted 👍😃")
                break
        else:
            print(f"{bcolors.FAIL}{word}{bcolors.ENDC} is not accepted 😔😔")



    