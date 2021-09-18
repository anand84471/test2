import matplotlib.pyplot as plt
plt.plot([1,3,7,9,11],[1,2,3,4,78])
plt.axis([1,50,1,100])
plt.xlabel("Date")
plt.ylabel("publications")
plt.title("Date vs publications plot")
plt.savefig("date vs publications plt.tiff")
plt.show()