from Bio import Entrez
Entrez.email="akr.cpibtc@gmail.com"
import os
os.chdir(r"C:\ReadMyCourse\PFB Weekend Batch\day9")
def download_gen_bank_seq(genbank_id,output_file,download_format="gb"):
    if os.path.isfile(output_file):
        print("This file already exists")
        print("Please specify a new file path")
        return
    handler=Entrez.efetch(db="nucleotide",id=genbank_id,rettype=download_format,
    retmode="text")
    print(handler.read(),file=open(output_file,"w"))

# download_gen_bank_seq("AY851618","AY851618.fasta","fasta")
# download_gen_bank_seq("AY851614","AY851614.fasta","fasta")
# download_gen_bank_seq("AY851615","AY851615.fasta","gb")
# download_gen_bank_seq("AY851613","AY851616.fasta","gb")



def download_list_genbank_seq(list_ids,output_file,download_format):
    count=1
    for ids in list_ids:
        print(count,": Downloading seq details for ",ids)
        handler=Entrez.efetch(db="nucleotide",id=ids,rettype=download_format,retmode="text")
        print(handler.read(),file=open(output_file,"a"))
        count+=1
    


list_ids=["AY851618","AY851619","AY851620","AY851621"]

#download_list_genbank_seq(list_ids,"result.fasta","fasta")


def download_list_genbank_seq_from_file(file_path,output_file,download_format):
    file=open(file_path,"r")
    list_ids=[]
    for lines in file.readlines():
        list_ids.append(lines.rstrip()) #rstrip rmoves the new line character
    download_list_genbank_seq(list_ids,output_file,download_format)


#download_list_genbank_seq_from_file("ids.txt","ids_seq.fasta","fasta")




def set_directory():
    import os
    os.chdir(r"C:\ReadMyCourse\PFB Weekend Batch\day9")

    


