from Bio.Seq import Seq, complement_rna

obj_seq=Seq("ATGATGATGTAAGTATAGATTAAGAGTAAA")
#count
count_a=obj_seq.count("A")
count_t=obj_seq.count("T")

print(count_t,count_a)

#transcibe
rna=obj_seq.transcribe()
print(rna)

#complement
complement_dna=obj_seq.complement()
print(complement_dna)

#reverse complement
reverse_com=obj_seq.reverse_complement()
print(reverse_com)

#back transcribe
dna=rna.back_transcribe()
print(dna,"\n",rna)


#translate

aa_chains=obj_seq.translate()
print(aa_chains)

print(obj_seq[0:].translate())
print(obj_seq[1:].translate())
print(obj_seq[2:].translate())


print(complement_dna[::-1].translate())
print(complement_dna[::-1][1:].translate())
print(complement_dna[::-1][2:].translate())


#translation with codon table
mit_codon_aac=obj_seq.translate(table=4,stop_symbol="--")
print(mit_codon_aac)

#stop_symbol="*", to_stop=False, cds=False, gap="-"

