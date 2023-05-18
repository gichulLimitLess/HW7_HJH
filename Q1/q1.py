import numpy as np

#eig는 Eigenvalue와 Eigenvector 값을 가지고 있음
#index 0에 eigenvalue, index 1에 eigenvector
#matrix1_det는 matrix1의 행렬식
eig = np.linalg.eig
matrix1 = np.matrix([[1,2],[3,4]])
matrix1_det = np.linalg.det(matrix1)

eigenvalues = eig(matrix1)[0]
eigenvector = eig(matrix1)[1]
print("Eigenvalues: ",eigenvalues)
print("Eigenvectors: \n",eigenvector)
print("Determinant: ", matrix1_det)

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec1_2_res = np.cross(vec1, vec2)

print("Cross product: ", vec1_2_res)

matrix_a = np.matrix([[1,2,-2], [2,1,-5], [1,-4,1]])
matrix_b = np.matrix([[-15],[-21],[18]])
x = np.linalg.solve(matrix_a, matrix_b)

print("Solution: \n", x)