N = int(input())

str_list = [[] for _ in range(N)]

for i in range(N):
    str_list[i].append(input())
    str_list[i].append(len(str_list[i][0]))

str_list = sorted(str_list, key=lambda x : (x[1], x[0]))

ans = []
for i in range(N):
    if str_list[i][0] not in ans:
        ans.append(str_list[i][0])

for i in range(len(ans)):
    print(ans[i])


z