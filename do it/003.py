import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # 5, 3
A = [0] + list(map(int, input().split()))  # [0,5,4,3,2,1] 인덱스 조정
S = [0] * (n + 1)  # 합 배열 초기화

# 누적합 배열 생성
for i in range(1, n + 1):
    S[i] = S[i - 1] + A[i]

for i in range(m):
    a, b = map(int, input().split())
    print(S[b] - S[a - 1])
