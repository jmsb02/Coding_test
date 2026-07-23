import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
deq = deque()
A = list(map(int, input().split()))

for i in range(n):  # 각 원소마다 최솟값 출력해야 하기 때문

    while deq and deq[-1][1] > A[i]:
        deq.pop()
    deq.append((i, A[i]))

    if deq[0][0] < i - m + 1:
        deq.popleft()

    print(deq[0][1], end=" ")
