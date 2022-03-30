T = int(input())

for _ in range(T):
    N = int(input())
    z_cnt = [0] * (N+1)
    o_cnt = [0] * (N+1)

    for i in range(N+1):
        if i == 0:
            z_cnt[i] = 1
            o_cnt[i] = 0
        elif i == 1:
            z_cnt[i] = 0
            o_cnt[i] = 1
        else:
            z_cnt[i] = z_cnt[i-1] + z_cnt[i-2]
            o_cnt[i] = o_cnt[i-1] + o_cnt[i-2]

    print(z_cnt[N], o_cnt[N])