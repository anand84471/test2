from Bio import Entrez
from os import chdir
chdir(r"C:\ReadMyCourse\PFB Weekend Batch\day9")
Entrez.email = "akr.cpibtc@gmail.com"

#rettype => {gb,fasta}
#retmode=>data exchange format =={ text,xml}
handler = Entrez.efetch(db="nucleotide", id="AY851612", rettype="fasta", retmode="text")
print(handler.read(),file=open("AY851612.fasta","w"))