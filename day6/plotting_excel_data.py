import pandas as pd
import matplotlib.pyplot as plt

excel_data=pd.read_excel("cancer_data_final.xlsx",engine="openpyxl")
brain_cancer_data=excel_data.loc[excel_data["Cancer group/site"]=="Brain Cancer"]
all_data=excel_data.loc[excel_data["Cancer group/site"]=="Acute lymphoblastic leukaemia (ALL)"]
#plotting year vs mortality count
year_data=brain_cancer_data["Year"]
mortality_count_data=brain_cancer_data["Mortality Count"]

plt.plot(year_data,mortality_count_data)
plt.plot(year_data,all_data["Mortality Count"])
plt.xlabel("Year")
plt.ylabel("Mortality count")
plt.title("Year vs mortality count plot")
plt.show()