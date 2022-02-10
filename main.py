import time
from pympler import tracker
import contextlib

fname = input("What file do you want to work with:")
hope = input("What is your k:")

hope = int(hope)
mem = tracker.SummaryTracker()
# ChronoStart
start = time.time()
# OuvertureDuFichier
with open(fname, "r") as file:
        # DéclarationDuDictio
    newdict = {}
        # InitialisationDeLaPremièreLigneAtraiter
    nLine = 1
        # LaLongeurDuKmer

    hope = int(hope)
        # IterationSurLesLignesDuFichierPourTraiterLesLignesDesSéquences
    for i, line in enumerate(file):
        pline = line.replace('N', '')
            # ÇavaCommencerÀLaLigneAvecIndex=1 ---> nLine
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
        # Le dictionnaire avec le nombre d'occurences

# ChronoEnd
end = time.time()
# Calcul de la durée du Processus
processTiming = end - start
saver = input("What is the name of file you want to save the results in:")
with open(saver,"w+") as rfile:
    with contextlib.redirect_stdout(rfile):
        print(newdict)
        print("Le temps du processus:", processTiming, "secondes,en minutes:", processTiming / 60)
        mem.print_diff()
        rfile.close()


#Author Mehdi Manjoura AKA MM98
#Feb 8, 2022



