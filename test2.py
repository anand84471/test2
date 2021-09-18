hittable_file_path= r"C:\python_Read my course\12092021\12092021\KW1DR2YC013-Alignment.txt"
PERCENTAGE_IDENTITY_CUTTOFF=75
EVALUE_CUTOFF=1.77e-62
file=open(hittable_file_path,"r")
for lines in file.readlines():
    if not lines.startswith("#"):
        percentage_identity=lines.split()[2] 
        evalue=lines.split()[-2]
        if float(percentage_identity)>PERCENTAGE_IDENTITY_CUTTOFF and float(evalue)<EVALUE_CUTOFF:
            print(lines.split()[1])