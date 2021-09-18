from Bio.Align.Applications import ClustalwCommandline
#build the commandline
clustalw_cline = ClustalwCommandline("clustalw2", infile=r"C:\ReadMyCourse\PFB Weekend Batch\day13\seqdump.txt")
print(clustalw_cline)
#output: clustalw2 -infile=opuntia.fasta
#donwload clustal from http://www.clustal.org/download/current/
#clustal file path = C:\Program Files (x86)\ClustalW2\
stdout, stderr = clustalw_cline()