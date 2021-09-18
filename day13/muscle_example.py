#donwload muscle
#https://www.drive5.com/muscle/downloads.htm
from Bio.Align.Applications import MuscleCommandline
muscle_cline = MuscleCommandline(input=r"C:\ReadMyCourse\PFB Weekend Batch\day13\seqdump.txt", out="blast_seq_align.txt")
print(muscle_cline)
#muscle -in opuntia.fasta -out opuntia.txt
stdout, stderr = muscle_cline()