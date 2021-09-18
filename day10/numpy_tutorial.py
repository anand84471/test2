import numpy as np
import matplotlib.pyplot as plt

data=np.linspace(1,10,100)
print(data)

#sin
print(np.sin(np.array(data)))
print(np.cos(np.array(data)))


plt.plot(data,np.sin(np.array(data)))
plt.show()

