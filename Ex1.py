import numpy as np
from backend import show_tensor

S5A = np.load('S5A.npy')
S5B = np.load('S5B.npy')
S5C = S5A*S5B
C_Trans = np.matrix.transpose(S5C)
C_Inv = np.linalg.inv(S5C)


show_tensor({'A': S5A})
show_tensor({'B': S5B})
show_tensor({'C': S5C})
show_tensor({'CTrans': C_Trans})
show_tensor({'C_Inv': C_Inv})
