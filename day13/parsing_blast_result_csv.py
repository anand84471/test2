import pandas as pd
data=pd.read_csv("C:\ReadMyCourse\PFB Weekend Batch\day13\KW1DR2YC013-Alignment-HitTable.csv")
#print(data.head(10))
PERCENTAGE_IDENTITY_CUTTOFF=75
EVALUE_CUTOFF=1.77e-62
BIT_SCORE_CUTOFF=254
# result=data.loc[
#     (data["IDENTITY"]>PERCENTAGE_IDENTITY_CUTTOFF) &
#     (data["EVALUE"]<EVALUE_CUTOFF)
#     ]
result=data.loc[
    ((data["IDENTITY"]>PERCENTAGE_IDENTITY_CUTTOFF) |
    (data["EVALUE"]<EVALUE_CUTOFF)) &
    (data["BIT SCORE"]>BIT_SCORE_CUTOFF)
    ]
file=open("balst_filtered_seq.fasta","w")
from Bio import SeqIO
fasta_sequences=SeqIO.parse("C:\ReadMyCourse\PFB Weekend Batch\day13\seqdump.txt",format="fasta")
for sequences in fasta_sequences:
    if sequences.id in list(result["HIT"]):
        file.write(">"+str(sequences.id)+"\n")
        file.write(str(sequences.seq)+"\n")
file.close()