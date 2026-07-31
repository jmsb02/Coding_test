import sys
import heapq
from math import inf

input = sys.stdin.readline

n, m, k = map(int, input().split())

# 인접리스트
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 최단 거리 리스트 생성 및 초기화
D = [[] for _ in range(n + 1)]
# distance[node]를 heap으로 관리 -> K개 중 가장 나쁜 값, 즉 가장 큰 거리를 빠르게 교체하기 위해서
heapq.heappush(D[1], 0)


# queue : 거리 상태를 실제로 꺼내서 다음 노드로 확장하기 위한 탐색 대기열
queue = []
heapq.heappush(queue, (0, 1))  # 누적 거리, 현재 노드

while queue:
    # 0, 1 (queue에서 누적 거리가 가장 짧은 경로를 꺼낸다.)
    distance, node = heapq.heappop(queue)

    # [(2,2), (3,7), (4,5), (5,6)] 인접한 노드 탐색
    for next_node, weight in graph[node]:
        # 여러 경로가 생길 수 있으니 여러 누적 거리를 보관 (1 -> 3 = 7, 1 -> 2 -> 3 = 6...)
        new_distance = distance + weight

        # next_node까지 도착하는 거리들이 K개 보다 작으면 저장
        if len(D[next_node]) < k:
            # -로 저장하는 이유 : heapq가 기본적으로 가장 작은 값을 앞에 두기 때문 (자동으로 오름차순 정렬)
            heapq.heappush(D[next_node], -new_distance)
            heapq.heappush(queue, (new_distance, next_node))

        else:  # k개 다 차있다면 비교해서 짧으면 넣어주고 아니면 버려준다.
            # D[next_node]는 거리를 음수로 저장해서 가장 긴 거리랑 비교 (ex. -10(얘), -6, -3...)
            if new_distance < -D[next_node][0]:  # 짧으면 바꿔줘야 함
                heapq.heappop(D[next_node])  # -10 제거
                heapq.heappush(D[next_node], -new_distance)  # -6 저장
                heapq.heappush(queue, (new_distance, next_node))  # queue 삽입

for i in range(1, n + 1):
    if len(D[i]) == k:
        print(-D[i][0])
    else:
        print(-1)
