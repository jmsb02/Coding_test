import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 1. 리스트 초기화 (2^k>=N의 k의 최솟값을 구하고, 2^k * 2만큼의 트리 리스트를 만든다)
k = 0
while 2**k < N:
    k += 1

lis = [0] * (2**k * 2)

# 리프 노드에 데이터 넣기
for i in range(N):
    tmp = int(input())
    lis[2**k + i] = tmp

# 리스트 값 삽입 (구간합)
for i in range(2**k - 1, 0, -1):  # 1까지인데 range특성상 -1해줘서 0까지암
    lis[i] = lis[2 * i] + lis[2 * i + 1]


# a==1일 때 update하는 함수 (b에 c의 값을 넣는다)
def update(b: int, c: int):
    # 질의 idx를 tree에 맞게 변경
    idx = b + 2**k - 1
    lis[idx] = c  # 리프노드 값은 여기서 업데이트 됨
    while idx != 1:  # 루트노드가 아닐 때까지 부모 노드로 올라가면서 업데이트를 해준다.
        next_idx = idx // 2
        lis[next_idx] = lis[2 * next_idx] + lis[2 * next_idx + 1]
        idx = next_idx


# a==2일 때 sum하는 함수 (질의 값 구하기)
def sumation(b: int, c: int):
    b_idx = b + 2**k - 1
    c_idx = c + 2**k - 1
    result = 0
    while b_idx <= c_idx:
        if b_idx % 2 == 1:
            result += lis[b_idx]
            b_idx += 1
        if c_idx % 2 == 0:
            result += lis[c_idx]
            c_idx -= 1
        # 마지막에 하는 이유 : 현재 단계에서 선택할 노드가 없더라도, 더 큰 구간 단위로 검사하려면 부모 단계로 올라가야 하기 때문
        b_idx //= 2
        c_idx //= 2
    return result


# 2. 질의값 구하기
for i in range(M + K):  # N+2 ~ N+M+K+2
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        print(sumation(b, c))

# * 인덱스 처리시 // (몫만 구하는 나눗셈) 사용
