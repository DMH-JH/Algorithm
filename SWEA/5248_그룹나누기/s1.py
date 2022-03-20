import sys
sys.stdin = open('input.txt')

# 정점의 대표원소 찾기
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


T = int(input())

for tc in range(1, T+1):
    # 1 ~ N번 까지의 출석번호
    # M장의 신청서
    N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    group = []

    # range(N+1)을 list 화 시켜서, 대표원소 초기화
    p = list(range(N+1))

    for i in range(M):
        M1, M2 = M_list[i*2], M_list[i*2+1]

        # M2의 대표원소를 M1의 대표원소로 바꿈
        p[find_set(M2)] = find_set(M1)

    # 대표원소 리스트의 첫 번째 번호부터 대표원소 x를 찾고
    for i in range(len(p)):
        x = find_set(i)

        # x가 group 에 중복되지 않는다면, group 에 append
        if x not in group:
            group.append(x)

    # 출석번호는 1번부터 존재하기 때문에, group 에서 0번은 제외하고
    # group 의 길이 - 1이 정답이 됩니다.
    print('#{} {}'.format(tc, len(group)-1))
