from Bio import Entrez
from constants import ENTEZ_EMAIL_ID
Entrez.email=ENTEZ_EMAIL_ID
handle = Entrez.esearch(db="protein", retmax=100, term="hydrogenimonaceae[Organism] AND gene[Text Word]", idtype="acc")
record = Entrez.read(handle)
print(record)