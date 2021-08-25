import numpy as np

C = np.random.randn(5, 5)
V0 = np.random.randn(5, 5)
R = np.random.randn(5, 5)
A = np.dot(C, np.dot(V0, C.T))


# first1 = np.linalg.inv(C)
# first2 = np.linalg.inv(np.linalg.inv(R) + np.linalg.inv(A))
# first3 = np.linalg.inv(R) + np.linalg.inv(A)

# first = np.dot(first1, np.dot(first2, first3))

second3 = np.linalg.inv(R + A)
K = np.dot(V0, np.dot(C.T, second3))

first = np.dot(V0, np.dot(C.T, np.linalg.inv(R))) - np.dot(K, np.dot(A, np.linalg.inv(R)) )


print(first - K)

