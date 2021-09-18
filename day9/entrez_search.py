from Bio import Entrez
from constants import ENTEZ_EMAIL_ID
Entrez.email=ENTEZ_EMAIL_ID
handle = Entrez.esearch(db="nucleotide", retmax=100, term="BRCA", idtype="acc")
record = Entrez.read(handle)
handle.close()
print("No of records are present in Entrez",record["Count"])
print("Id list","===>",record["IdList"])

from automate_util import download_list_genbank_seq

download_list_genbank_seq(record["IdList"],"BRCA_query_result.fasta","fasta")

