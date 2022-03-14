import time
from collections import Counter
from pympler import tracker
import contextlib
import matplotlib.pyplot as sca
import numpy as np

def seq():
    fname = input("What file do you want to work with:")
    hope = int(input("What is your k:"))
    mem = tracker.SummaryTracker()
    # ChronoStart
    start = time.time()
    # OuvertureDuFichier
    with open(fname, "r") as file:
    # DéclarationDuDictio
        newdict = {}
        tailleGenome = ""
        nbrtotalKmers = 0
    # InitialisationDeLaPremièreLigneAtraiter
        nLine = 1
    # IterationSurLesLignesDuFichierPourTraiterLesLignesDesSéquences
        for i, line in enumerate(file):
            pline = line.replace('N', '')
        # CommencerÀLaLigneAvecIndex=1 ---> nLine
            if i == nLine:
            # CalculDuNombreDesKmers
                numbKmerspL = len(pline) - hope + 1
                print("La séquence est la suivante:", pline)
                tailleGenome += pline
                lenFastq = len(tailleGenome)
                nbrtotalKmers += numbKmerspL
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
    #comptage des occurences des nombres de kmers
    occ = Counter(newdict.values())
    #nombre d occurences, listé!
    keys = np.array(list(occ.keys()))
    #nombre de kmers,listé!
    values = np.array(list(occ.values()))
    #log des valeurs
    outkeys = np.log10(keys)
    outvalues = np.log10(values)

    #Représentation
    sca.xlabel("n--Nombre de kmers")
    sca.ylabel("fn--Nombre d'occurrences")
    sca.title("Représentation du Spectrum")
    #sca.annotate("Couverture: maximum local de la fonction", xytext = (1.73,4.70), xy=(2,6), arrowprops = {'facecolor':'black'})
    sca.scatter(outkeys,outvalues)
    sca.show()
    lenFasta = 0
    #longeur du génome assmemblé
    fasta = input("Veuillez entrer le nom du fichier du génome assemblé:")
    with open(fasta, 'r') as f:
        for line in f:
            line = line.strip()
            if line != '>':
                lenFasta += len(line)
            else:
                pass
# ChronoEnd
    end = time.time()
# Calcul de la durée du Processus
    processTiming = end - start
    saver = input("What is the name of file you want to save the results in:")

    with open(saver, "w+") as rfile:
        with contextlib.redirect_stdout(rfile):
            print(newdict,"\n","*"*40,"\n","Nombres de kmers dans le fichier:", nbrtotalKmers,"\n", "*"*40,"\n","La couverture est de:", lenFastq/lenFasta,"\n", "*"*40,"\n","n: nombre d'occurences:", keys,"\n", "*"*40,"\n","fn: nombre de kmers:", values, "\n","*"*40,"\n","Le temps du processus:", processTiming, "secondes,en minutes:", processTiming / 60)
            mem.print_diff()
            rfile.close()

# Author Mehdi Manjoura AKA MM98
# March 9, 2022
seq()

