import sys

input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

fac = [0] * 21
fac[0] = 1
visited = [False] * 21

for i in range(1, N + 1):
    fac[i] = fac[i - 1] * i

# 4
# 1 3
if num[0] == 1:
    K = num[1]  # 3
    cnt = 1  # 묶음 번호 초기화
    # 첫 번째 자리부터 탐색하면서
    for i in range(1, N + 1):
        # 현재 자리에서 묶음 하나의 크기를 구해준다. (ex. 첫번째 자리 고정 = fac[3])
        cases = fac[N - i]
        # case * cnt = cnt번째 묶음의 끝번호 (뜻 K가 이 cases에 속할때까지 cnt 증가시켜주고)
        while K > cases * cnt:
            cnt += 1
        # 속한다면, K가 선택한 묶음 안에서 몇 번째인지 확인한다.(새 K = 기존 K - 앞에서 건너뛴 순열 개수)
        K = K - cases * (cnt - 1)

        # cnt번째 미사용 숫자를 실제 값으로 찾는 코드
        # 지금까지 안 쓴 숫자를 몇 개 발견했냐
        # ex [1,2,3,4]에서 2 사용, cnt = 2 -> 3이 나와야지 2가 나오면 안된다 <- order로 조정
        order = 0
        for j in range(1, N + 1):
            if not visited[j]:
                order += 1

                if order == cnt:
                    print(j, end=" ")
                    visited[j] = True
                    break

else:
    K = 1  # 최솟값 1로 설정

    for i in range(1, N + 1):
        cur = num[i]

        cnt = 0

        # 현재 숫자보다 작은 숫자만 본다 (ex. 4라면 1,2,3만 확인)
        for j in range(1, cur):
            # 그 중 이미 사용한건 뺴야함 (작은 미사용 숫자 개수를 센다)
            if not visited[j]:
                cnt += 1

        # 앞에 있는 묶음 수 * 묶음 하나 크기를 더한다.
        K += cnt * fac[N - i]

        visited[cur] = True
    print(K)
