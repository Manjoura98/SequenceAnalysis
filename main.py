import time
import math
from pympler import tracker
import contextlib
import matplotlib.pyplot as plt
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


revDict = {}

for key, value in newdict.items():
    if value not in revDict:
        revDict[value] = [key]
    else:
        revDict[value].append(key)
dix = {}
for b,a in revDict.items():
    print(b, len(list(filter(None,a))))
    dix[b] = len(list(filter(None,a)))

print(dix)

nOcc = [k for k in dix.keys()]
nKmers = [v for v in dix.values()]
logNocc = [math.log10(z) for z in nOcc]
logNkmers = [math.log10(t) for t in nKmers]
print(nOcc)
print(nKmers)
for i in range(len(logNkmers)-1,-1,-1):
    if logNkmers[i] == 0:
        logNkmers.remove(logNkmers[i])
        logNocc.remove(logNocc[i])
print(logNocc)
print(logNkmers)
print(len(logNocc))
print(len(logNkmers))

plt.scatter(logNkmers,logNocc)
plt.show()
# ChronoEnd
end = time.time()
# Calcul de la durée du Processus
processTiming = end - start
saver = input("What is the name of file you want to save the results in:")
with open(saver, "w+") as rfile:
    with contextlib.redirect_stdout(rfile):
        print(newdict)
        print(revDict)
        print("Le temps du processus:", processTiming, "secondes,en minutes:", processTiming / 60)
        print("Nombre de kmers:","Nombres des occurences:")
        print("*"*40)
        for i in range(len(nKmers)):
            rfile.write(str(nKmers[i])+ " "*10 + str(nOcc[i]) + "\n")
        mem.print_diff()
        rfile.close()

# Author Mehdi Manjoura AKA MM98
# Mar 8, 2022



