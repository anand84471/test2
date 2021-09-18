from Bio import SeqIO
from Bio.SeqUtils import GC

records=SeqIO.parse("ls_orchid.fasta","fasta")

for record in records:
    print(record.id,len(record.seq),round(GC(record.seq),2))