import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
data=pd.read_csv(r"C:\ReadMyCourse\PFB Weekend Batch\day10\data.csv")
print(data.head())
#plotting yes no
sns.relplot(y="texture_mean", x="radius_mean", hue="diagnosis", data=data,style="diagnosis")
plt.show()