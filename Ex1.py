import numpy as np
from backend import show_tensor

S5A = np.load('S5A.npy')
S5B = np.load('S5B.npy')
S5C = S5A*S5B
S5C_Trans = np.matrix.transpose(S5C)
S5C_Inv = np.linalg.inv(S5C)


show_tensor({'A': S5A})
show_tensor({'B': S5B})
show_tensor({'C': S5C})
show_tensor({'CTrans': S5C_Trans})
show_tensor({'C_Inv': S5C_Inv})
