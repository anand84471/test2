from bioinfokit import analys, visuz
import matplotlib.pyplot as plt
df = analys.get_data('volcano').data
df.head(2)
df.to_csv("gene_expression_data.csv")

# visuz.gene_exp.volcano(df=df, lfc='log2FC', plotlegend=True,
# pv='p-value',show=True, legendpos='upper right', valpha=0.1,
# genenames=({"LOC_Os09g01000.1":"EP", "LOC_Os01g50030.1":"CPuORF25", "LOC_Os06g40940.3":"GDH", "LOC_Os03g03720.1":"G3PD"}),
#     gstyle=2)

# visuz.gene_exp.volcano(df=df, lfc="log2FC", pv="p-value", geneid="GeneNames",
#     genenames=("LOC_Os09g01000.1", "LOC_Os01g50030.1", "LOC_Os06g40940.3", "LOC_Os03g03720.1"), gstyle=2 )


visuz.gene_exp.involcano(df=df, lfc="log2FC", pv="p-value", geneid="GeneNames", 
    genenames=({"LOC_Os09g01000.1":"EP", "LOC_Os01g50030.1":"CPuORF25", "LOC_Os06g40940.3":"GDH", "LOC_Os03g03720.1":"G3PD"}),
    gstyle=2)