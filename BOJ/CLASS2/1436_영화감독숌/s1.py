N = int(input())
cnt = 0
ans = 0
i = 0

while True:
    if '666' in str(i):
        cnt += 1

    if cnt == N:
        ans = i
        break

    i += 1

print(ans)