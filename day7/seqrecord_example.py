from Bio import SeqIO
obj_seqrecord=SeqIO.read("sequence.gb","genbank")

#id
print(obj_seqrecord.id)

#name
print(obj_seqrecord.name)
#des
print(obj_seqrecord.description)

#seq
#print(obj_seqrecord.seq)

#translation
aa_chanis_list=str(obj_seqrecord.seq.translate()).split("*")
print(len(aa_chanis_list))

unique_aa_chains=set(aa_chanis_list)
print(len(unique_aa_chains))

lengths=[]
lysine_percentages=[]
for aa in unique_aa_chains:
    if len(aa)!=0:
        lengths.append(len(aa))
        lysine_percentages.append(100*aa.count("K")/len(aa))

import matplotlib.pyplot  as plt
#plt.plot(lengths)
plt.plot(lysine_percentages)
plt.show()




