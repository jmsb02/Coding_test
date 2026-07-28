N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))


for i in range(M):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B[i]:
            print(1)
            break
        elif A[mid] < B[i]:
            start = mid + 1
        elif A[mid] > B[i]:
            end = mid - 1
    else:
        print(0)
