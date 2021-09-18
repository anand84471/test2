hittable_file_path="C:\ReadMyCourse\PFB Weekend Batch\day13\KW1DR2YC013-Alignment.txt"
PERCENTAGE_IDENTITY_CUTTOFF=75
EVALUE_CUTOFF=1.77e-62
file=open(hittable_file_path,"r")
for lines in file.readlines():
    if not lines.startswith("#"):
        percentage_identity=lines.split()[2] 
        evalue=lines.split()[-2]
        if float(percentage_identity)>PERCENTAGE_IDENTITY_CUTTOFF and float(evalue)<EVALUE_CUTOFF:
            print(lines.split()[1])

# text="BE037100.1	XM_016034586.2	76.399	572	111	19	57	619	164	720	1.75e-72	287"
# print(text.split()[2])
# print(text.split()[-2])