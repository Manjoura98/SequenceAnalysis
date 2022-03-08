import time
from math import log10
from collections import Counter
from pympler import tracker
import contextlib
import matplotlib.pyplot as sca
fname = input("What file do you want to work with:")
hope = int(input("What is your k:"))
mem = tracker.SummaryTracker()
# ChronoStart
start = time.time()
# OuvertureDuFichier
with open(fname, "r") as file:
    # DéclarationDuDictio
    newdict = {}
    # InitialisationDeLaPremièreLigneAtraiter
    nLine = 1
    # IterationSurLesLignesDuFichierPourTraiterLesLignesDesSéquences
    for i, line in enumerate(file):
        pline = line.replace('N', '')
        # CommencerÀLaLigneAvecIndex=1 ---> nLine
        if i == nLine:
            # CalculDuNombreDesKmers
            numbKmers = len(pline) - hope + 1
            print("Le nombre des kmers:", numbKmers)
            print("La longueur de la séquence dans la ligne:", i, "est:", len(pline), "nucléotides!")
            print("La séquence est la suivante:", pline)
            # PourLe S commençant de la position 0 et avec un hope de longeur k, jusquau dernier kmer, Split to Kmers of HopeLength,PisIncrémenter s
            for s in range(0, len(pline) - hope):
                sub = pline[s:s + hope]
                if sub in newdict:
                    newdict[sub] += 1
                    # Sinon ajouter la première Ocurrence
                else:
                    newdict[sub] = 1
                # Passer à la prochaine ligne de séquence
            nLine = nLine + 4
occ = Counter(newdict.values())
a = []
b = []
for i in occ:
    a.append(log10(i))
    b.append(log10(occ[i]))
for j in range(len(a)):
    if a[i] == 0:
        a.remove(a[i])
        b.remove(b[i])
sca.xlabel("f(n)--Nombre d'occurrences")
sca.ylabel("n--Nombre de kmers")

sca.hist(a,b)
sca.show()

# ChronoEnd
end = time.time()
# Calcul de la durée du Processus
processTiming = end - start
saver = input("What is the name of file you want to save the results in:")
with open(saver, "w+") as rfile:
    with contextlib.redirect_stdout(rfile):
        print(newdict)

        print("Le temps du processus:", processTiming, "secondes,en minutes:", processTiming / 60)
        print("Nombre d'occurrences-f(n)-- après application du log:","Nombres de kmers(n)-- après application du log:")
        print("*"*40)
        for i in range(len(a)):
            rfile.write(str(a[i])+ " "*10 + str(b[i]) + "\n")
        print("La représentation graphique pour le kmer égal à:", hope, "est:")
        sca.savefig('figureKmer.png')
        mem.print_diff()
        rfile.close()

# Author Mehdi Manjoura AKA MM98
# March 7, 2022

