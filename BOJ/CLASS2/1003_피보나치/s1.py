def fibo(n):
    global z_cnt
    global o_cnt
    if n == 0:
        z_cnt += 1
        return 0
    elif n == 1:
        o_cnt += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


T = int(input())

for _ in range(T):
    N = int(input())

    z_cnt = 0
    o_cnt = 0
    fibo(N)
    print(z_cnt, o_cnt)

