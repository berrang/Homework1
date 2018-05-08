import numpy as np
import matplotlib.pyplot as plt


X = np.random.randn(1000) * 2
Y = np.sin(X)
sortArray = np.argsort(X)

# point plot
plt.plot(X[sortArray], Y[sortArray], c='b', label="sin")


plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.show()
