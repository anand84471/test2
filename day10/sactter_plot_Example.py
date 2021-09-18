import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel(r"C:\ReadMyCourse\PFB Weekend Batch\day10\cancer_data_final.xlsx",engine="openpyxl")
print(data.head())

data_acl=data.loc[data["Cancer group/site"]=="Acute lymphoblastic leukaemia (ALL)"]
print(data_acl.head())
# plt.scatter(data_acl["Year"],data_acl["Mortality Count"],c=data_acl["Year"], 
# s=40*data_acl["Mortality Count"], alpha=0.6)
plt.errorbar(data_acl["Year"],data_acl["Mortality Count"],2,
color='black',elinewidth=3,capsize=10,ecolor='lightgray') #2 specifies the error
plt.show()
