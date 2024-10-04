n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
balls = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    balls[x-1][y-1] = 1
###

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def move():
    global balls

    for x in range(n):
        for y in range(n):
            if balls[x][y]:
                temp = []
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny) and board[x][y] < board[nx][ny]:
                        temp.append(board[nx][ny])
                    
                    if not temp:
                        break
                    else:
                        max_val = max(temp)
                        if temp.count(max_val) == 1:
                            for dx, dy in zip(dxs, dys):
                                nx, ny = x+dx, y+dy
                                if in_range(nx, ny) and board[nx][ny] == max_val:
                                    balls[x][y] -= 1
                                    balls[nx][ny] += 1
                                    break

def remove_collision():
    global balls

    for x in range(n):
        for y in range(n):
            if balls[x][y] >= 2 or balls[x][y] <= 0:
                balls[x][y] = 0

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# print(balls)
for _ in range(t):
    move()
    remove_collision()
    # print(balls)

cnt = 0

for i in range(n):
    cnt += sum(balls[i])

print(cnt)