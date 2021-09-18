from Bio.Data import CodonTable

standard_ct=CodonTable.unambiguous_dna_by_id[1]
#standard_ct=CodonTable.unambiguous_dna_by_id["Standard"]
print(standard_ct)


mito_ct=CodonTable.unambiguous_dna_by_id[2]
print(mito_ct)
print(dir(mito_ct))
print(mito_ct.start_codons)
print(mito_ct.stop_codons)

print(mito_ct.names)

