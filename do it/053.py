n, m = map(int, input().split())
A = [0] + [i for i in range(1, n + 1)]


def find(a: int):
    if A[a] == a:
        return A[a]
    else:
        A[a] = find(A[a])
        return A[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        A[root_b] = root_a


for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:  # a=1
        if find(b) != find(c):
            print("NO")
        else:
            print("YES")
