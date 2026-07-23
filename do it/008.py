import sys

input = sys.stdin.readline

n = int(input())
A = sorted(map(int, input().split()))
count = 0  # result

for k in range(n):
    find = A[k]  # 찾을 값, k = 지금 좋은 수인지 검사할 원소의 인덱스
    i = 0  # 맨 앞
    j = n - 1  # 맨 끝
    while i < j:  # 끝나는 조건

        # 목표값 A[k] 자기 자신을 합에 사용하지 않도록 해당 인덱스를 건너뜀
        # 예: A=[0,1,2]에서 1을 찾고 싶고 i=0,j=1일 때, 0+자기 자신(1)을 쓰지 않도록 k 인덱스를 건너뜀
        if i == k:
            i += 1
            continue
        if j == k:
            j -= 1
            continue

        if A[i] + A[j] > find:
            j -= 1
        elif (
            A[i] + A[j] < find
        ):  # j는 이미 마지막 인덱스이므로 j += 1 하면 배열 범위를 벗어남
            i += 1
        else:  # A[i] + A[j] == find
            # A[k]를 만들 수 있는 두 수를 찾았으므로 좋은 수 개수를 1 증가시키고, 중복 계산을 막기 위해 탐색 종료
            count += 1
            break
print(count)
