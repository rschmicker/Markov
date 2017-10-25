#!/usr/bin/env python
import math
import random
import numpy as np
from numpy import linalg as LA

a0 = float(100)
b0 = float(0)

matrix = np.matrix([[1, 0], [1, 0]])
to_multi = np.matrix([[a0], [b0]])

LA.matrix_power(matrix, 2000)

ans = np.dot(matrix, to_multi)
print(ans)
