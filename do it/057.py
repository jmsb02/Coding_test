from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]  # 인접 리스트
indegree = [0] * (n + 1)  # 진입 차수
build_time = [0] * (n + 1)  # 건물 건설 시간
result = [0] * (n + 1)  # 최종 완성 시간

for i in range(1, n + 1):
    lis = list(map(int, input().split()))  # 4 3 1 -1
    build_time[i] = lis[0]  # 건설 시간은 고정이니 값 넣어줌

    for j in range(1, len(lis) - 1):  # 인덱스 조정 & -1 자연스럽게 제외
        graph[lis[j]].append(i)  # ex) j = 1 lis[j] = 3 문제보면 lis[j] -> i
        indegree[i] += 1

queue = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)  # queuq = 다음에 처리할 건물 번호

# 각 건물의 완성 시간을 자기 건설 시간으로 초기화
result = build_time.copy()

while queue:
    node = queue.popleft()  # 1

    for next_node in graph[node]:  # 3
        # 기존에 계산한 next_node의 완성 시간 vs 이번 선행 건물을 거쳐 계산한 next_node의 완성 시간
        result[next_node] = max(result[next_node], result[node] + build_time[next_node])

        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

for i in range(1, n + 1):
    print(result[i])
