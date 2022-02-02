
from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio.Data import CodonTable
from Bio import SeqFeature
from Bio import SeqIO

#fich = "/home/mehdim/Desktop/BioPython/chry5_S14_L001_R1_001.fastq"
#startlist = []
#with open("/home/mehdim/Desktop/BioPython/chry5_S14_L001_R1_001.fastq") as s:
    #for i in SeqIO.parse(s, "fastq"):
        #startlist.append(str(i.seq))


#file = open("/home/mehdim/Desktop/BioPython/chry5_S14_L001_R1_001.fastq")
#sequences = file.readlines()
#file.close()
#i = 2
#for i in len(sequences):
    #p = sequences[i]
    #print(p)
    #i += 3

with open("/home/mehdim/Desktop/BioPython/chry5_S14_L001_R1_001.fastq") as file:
    nLine = 1
    for i, line in enumerate(file):
        if i == nLine:
            print(line)
            longueur = len(line)
            print(longueur)
            nLine = nLine + 4

    




#while p in len(sequences):
    #print(p)
    #p += 4



#print(startlist)

#print (len(startlist[0]))

#my_seq = "ATGCATGCAAGGAAAAAATTTTGCGGGGGCTATATATATATATATAGG";

#print(GC(my_seq))

#seqq = ["AAATTTGG","AAAAAAGTCGTTTA"]

#p = ""

#for i in seqq:
    #p += i;

#print(p)

#space = "N"*10

#print (space.join(seqq))

#dna = Seq("ATGTAGCGCATTAGCGCG")
#mrna = dna.transcribe()
#protein = mrna.translate()

#print(mrna)
#print(protein)

#standard_table = CodonTable.unambiguous_dna_by_name["Standard"]

#print (standard_table)

#print (standard_table.stop_codons)



#var0 = len(my_seq);
#var1= my_seq.count("G");

#var2= my_seq.count("C");

#freq = (var1 + var2)/2;

#print (freq)

#for index,letter in enumerate(my_seq):
    #print ("%i = %s" %(index,letter))




#for index,letter in enumerate(my_seq,5):
    #print ("%i = %s" %(index,letter))
