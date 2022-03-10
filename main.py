import math
import time
from math import log10
from collections import Counter
from pympler import tracker
import contextlib
import matplotlib.pyplot as sca
import pandas as pd
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
                tailleGenome += pline
                lenFastq = len(tailleGenome)

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
    keys = np.array(list(occ.keys()))
    values = np.array(list(occ.values()))

    outkeys = np.log10(keys)
    outvalues = np.log10(values)


    sca.xlabel("n--Nombre d'occurrences")
    sca.ylabel("fn--Nombre de kmers")
    sca.title("Représentation du Spectrum")
    sca.scatter(outkeys,outvalues)
    sca.show()
    lenFasta = 0

    fasta = input("Veuillez entrer le nom du fichier du génome assemblé:")
    with open(fasta, 'r') as f:
        for line in f:
            line = line.strip()
            if line != '>':
                lenFasta += len(line)
            else:
                pass

    print("La longeur du fichier Fasta:",lenFasta)
    print("La longeur du fichier Fastq:", lenFastqFastq)

# ChronoEnd
    end = time.time()
# Calcul de la durée du Processus
    processTiming = end - start
    saver = input("What is the name of file you want to save the results in:")

    with open(saver, "w+") as rfile:
        with contextlib.redirect_stdout(rfile):
            print(newdict)
            print("La couverture est de:", lenFastq/lenFasta)

            print("Le temps du processus:", processTiming, "secondes,en minutes:", processTiming / 60)
            mem.print_diff()
            rfile.close()



# Author Mehdi Manjoura AKA MM98
# March 9, 2022

seq()
