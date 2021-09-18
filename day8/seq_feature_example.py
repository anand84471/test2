from Bio import SeqIO

record=SeqIO.read("sequence.gb","genbank")

#print(record.features)

no_of_features=len(record.features)
print(no_of_features)



# for featutres in record.features:
#     print(featutres.type,featutres.location)
#     print(featutres.extract(record.seq))

#extraction of sequence of the feature




for features in record.features:
    if features.type=="CDS":
        print(features.extract(record.seq).translate(table=2))
        print("--------------------------------------------------")

    
