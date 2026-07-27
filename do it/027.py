import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

cols = [False] * N  # 열 충돌 확인 리스트
dig1 = [False] * (2 * N - 1)  # 오른쪽 위 대각선 체크 리스트 (row+col)
dig2 = [False] * (2 * N - 1)  # 오른쪽 아래 대각선 체크 리스트 (row-col+(N-1))


def backtracking(row: int):
    global cnt  # 새 지역변수가 아닌 전역 변수 cnt 사용 선언
    if row == N:  # N = 4 0,1,2,3 돌고 4일때는 탈출해야 함 (row : 다음에 처리할 행 번호)
        cnt += 1
        return

    for col in range(N):  # 열 탐색
        # 열, 오른쪽 위 대각선, 오른쪽 아래 대각선이 아닐 경우에만 접근
        if not cols[col] and not dig1[row + col] and not dig2[row - col + (N - 1)]:
            cols[col] = dig1[row + col] = dig2[row - col + (N - 1)] = True  # 방문 처리
            backtracking(row + 1)  # 행 탐색
            # backtracking 후 다시 False 처리
            cols[col] = dig1[row + col] = dig2[row - col + (N - 1)] = False


backtracking(0)  # 0 행부터 시작
print(cnt)
