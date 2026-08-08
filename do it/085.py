import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 크기 = N + M
dp = [[0] * 201 for _ in range(201)]

# 조합 초기화 nC0 = nCn = 1
for i in range(201):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(1, 201):
    for j in range(1, i):  # 0 < r < n, ex. 4Cn이면 4C1 ~ 4C3까지만
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

# 전체 문자열 개수 < K -> -1 출력
if dp[N + M][N] < K:
    print(-1)
else:
    while not (N == 0 and M == 0):
        # a를 모두 사용한 경우, 남은 M개의 문자는 모두 z이므로 한 번에 출력
        if N == 0:
            print("z" * M, end="")
            break
        # z를 모두 사용한 경우, 남은 N개의 문자는 모두 a이므로 한 번에 출력
        if M == 0:
            print("a" * N, end="")
            break

        # a를 선택했을 때 전체 개수 중(N+M-1) 남아 있는 문자들로 만들 수 있는 경우의 수 (a가 N-1개, z가 M)
        T = dp[N + M - 1][N - 1]  # = dp[N+M-1][M]
        if K <= T:
            print("a", end="")
            N -= 1
        else:  # K > T (a 묶음을 넘어감 -> z 선택)
            K = K - T  # 새 K로 만들어주고
            print("z", end="")
            M -= 1
