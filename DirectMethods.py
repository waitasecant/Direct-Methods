import numpy as np

n = int(input("Enter number of unknowns"))
A = np.zeros((n, n+1))
x = np.zeros(n)
print("Enter Augmented Matrix Coefficients")
for i in range(n):
    for j in range(n+1):
        A[i][j] = float(input(f"A[{i}][{j}]="))

U = A[:, :n]
b = A[:, n]

# Diagonal
D = np.diag(np.diag(U))
print("D=\n", D.round(2), "\n")
print("b=\n", b.round(2), "\n")

for i in range(n):
    x[i] = b[i]/D[i][i]
print("x=\n", x.round(2), "\n")

# Upper Triangular
U = np.triu(U, k=0)
print("U=\n", U.round(2), "\n")
print("b=\n", b.round(2), "\n")

for i in range(n-1, -1, -1):
    x[i] = (b[i]-sum(U[i][j]*x[j] for j in range(i+1, n)))/(U[i][i])
print("x=\n", x.round(2), "\n")
