M, N = map(int, input().split())
A = [0] * (N + 1)
for i in range(2, N + 1):
    A[i] = i

for i in range(2, int(N**0.5) + 1):
    if A[i] == i:
        for j in range(i * i, N + 1, i):
            A[j] = 0

for i in range(M, N + 1):
    if A[i] != 0:
        print(A[i])
