import sys

input = sys.stdin.readline

n = int(input())
A = list()
for i in range(n):
    A.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

for i in range(n):
    print(A[i])
