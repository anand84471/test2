# import pandas as pd
# excel_data=pd.read_csv("C:\D\ReadMyCourseLiveClasses\Python for Bioinformatics Batch 6\day6\year vs mortality count.csv")
# print(excel_data)

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[4,8,9,1])
plt.xlabel("Date")
plt.ylabel("Publications")
plt.title("Date vs publications plot")
plt.axis([1,30,2,40]) #specifying x range
# plt.savefig("date vs publication plot.png")
# plt.savefig("date vs publication plot.svg")
# plt.savefig("date vs publication plot.tiff")
# plt.savefig("date vs publication plot.pdf")
plt.show()
