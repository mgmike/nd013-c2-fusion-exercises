import numpy as np

phi = 0.7
T = np.matrix([[phi, -1 * phi, 0,4],
              [phi, phi, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

z = np.matrix([2,0,0,1])
result = T * z.transpose()
print(result)