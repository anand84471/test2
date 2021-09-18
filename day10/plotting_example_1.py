import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("C:\ReadMyCourse\PFB Weekend Batch\day10\gene_expression_data.csv")

print(data.head())

curated_data=data.loc[(data["p-value"]<0.005)]
plt.plot(curated_data["log2FC"],curated_data["p-value"])
plt.show()
