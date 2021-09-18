import matplotlib.pyplot as plt
import numpy as np

data=np.linspace(0,10,100)

plt.plot(data,np.sin(data),linestyle="dotted",color="0.54",label="sin plot")
plt.plot(data,np.cos(data),linestyle="dashdot",color="0.9",label="cos plot")
plt.legend()
plt.show()