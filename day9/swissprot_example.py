from Bio import ExPASy
from automate_util import set_directory
set_directory()
handler=ExPASy.get_sprot_raw("O23729")
# print(handler.read(),file=open("O23729.swiss","w"))
from Bio import SeqIO
seqrecord=SeqIO.read(handler.read(),format="swiss")
print(seqrecord.id)
print(seqrecord.seq)
