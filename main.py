#from numpy import array
#from numpy import argmax
#from keras.utils
import time

#ChronoStart
start = time.time()

#OuvertureDuFichier
with open("/home/mehdim/Desktop/BioPython/chry5_S14_L001_R1_001.fastq") as file:
    #DéclarationDuDictio
    newdict = {}
    #InitialisationDeLaPremièreLigneAtraiter
    nLine = 1
    #LaLongeurDuKmer
    hope = input("what is the size of the k desired:")
    hope = int(hope)
    #IterationSurLesLignesDuFichierPourTraiterLesLignesDesSéquences
    for i, line in enumerate(file):
        #ÇavaCommencerÀLaLigneAvecIndex=1 ---> nLine
        if i == nLine:
            #CalculDuNombreDesKmers
            numbKmers = len(line) - hope + 1
            print("La longueur de la séquence est de:", len(line), "Nucléotides")
            print("La séquence est la suivante:", line)
            print("Le nombre des kmers:", numbKmers)


            #PourLe S commençant de la position 0 et avec un hope de longeur k, jusquau dernier kmer, Split to Kmers of HopeLength,PisIncrémenter s
            for s in range(0, len(line)-hope):
                sub = line[s:s+hope]
                if sub in newdict:
                    newdict[sub] += 1
        #Sinon ajouter la première Ocurrence
                else:
                    newdict[sub] = 1

        #Passer à la prochaine ligne de séquence
            nLine = nLine + 4
        #Le dictionnaire avec le nombre d'occurences
    print(newdict)
    #ChronoEnd
    end = time.time()
    #Calcul de la durée du Processus
    processTiming = end - start
    print("Le temps du processus:", processTiming, "secondes,en minutes:", processTiming/60)
    





















