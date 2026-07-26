import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n + 1)
res = []  # 결과도 담고 반환하는 리스트


def DFS():
    if len(res) == m:
        print(*res)
        return

    for i in range(1, n + 1):
        if visited[i] == False:
            visited[i] = True
            res.append(i)
            DFS()
            res.pop()
            visited[i] = False


DFS()
