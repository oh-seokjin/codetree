cnt = 0
for _ in range(5):
    n = int(input())
    if n%3 == 0:
        cnt += 1

if cnt != 0:
    print(1)
else:
    print(0)