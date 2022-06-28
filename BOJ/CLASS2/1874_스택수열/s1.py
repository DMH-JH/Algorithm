N = int(input())
num_list = list(range(1, N+1))
arr = []
stack = []
ans = []
impossible = False

for _ in range(N):
    arr.append(int(input()))

j = 0
for i in range(N):
    stack.append(num_list[i])
    ans.append('+')

    while stack and stack[-1] == arr[j]:
        stack.pop(-1)
        ans.append('-')
        j += 1


if stack:
    print('NO')
else:
    for c in ans:
        print(c)
