from Bio import SeqIO

usa_record=SeqIO.read("sequence_usa.gb","genbank")
china_record=SeqIO.read("sequence.gb","genbank")

aa_usa=str(usa_record.seq.translate()).split("*")
aa_china=str(china_record.seq.translate()).split("*")

print(len(aa_usa),len(aa_china))
common_peptides=set(aa_china)&set(aa_usa)
print(len(common_peptides))

lengths=[]
for aa in common_peptides:
    if len(aa)!=0:
        lengths.append(len(aa))
import matplotlib.pyplot  as plt
#plt.plot(lengths)
plt.plot(lengths)
plt.show()
