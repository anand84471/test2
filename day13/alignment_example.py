# from Bio import AlignIO
# alignment = AlignIO.read(r"C:\ReadMyCourse\PFB_practice\drug developement pipelines\seq_alignment_sample_file.aln", "clustal")
# print(alignment)



from Bio import Phylo
tree = Phylo.read(r"C:\ReadMyCourse\PFB Weekend Batch\day13\seqdump.dnd", "newick")
tree.rooted = True
# Phylo.draw_ascii(tree) #draw on commandline
Phylo.draw(tree, branch_labels=lambda c: c.branch_length) #plot with branch length
#Phylo.draw(tree)# to draw like plot