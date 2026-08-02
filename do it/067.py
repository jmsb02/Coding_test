import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = []  # 엣지 리스트
D = [i for i in range(V + 1)]  # 최단 거리 리스트

# 엣지 리스트 값 넣어주기
for i in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

# 가중치 기준으로 오름차순 정렬
edges.sort(key=lambda x: x[2])


# 값이 대표노드인지 확인 (인덱스랑 실제 값이 같은지 비교)
def find(a: int):
    if a == D[a]:
        return a
    else:
        return find(D[a])


def union(a: int, b: int):
    A = find(a)
    B = find(b)
    if A != B:
        D[B] = A


result = 0

for i in range(E):
    s, e, w = edges[i]
    if find(s) != find(e):
        union(s, e)
        result += w
print(result)
