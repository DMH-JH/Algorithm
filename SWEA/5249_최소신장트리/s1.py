import sys
sys.stdin = open('input.txt')

# 정점의 대표원소 찾기
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []

    # 입력을 저장할때, w 가중치 기준으로 정렬하기 때문에
    # w를 첫번째 원소로 저장
    for _ in range(E):
        n1, n2, w = list(map(int, input().split()))
        edge.append([w, n1, n2])

    # weight 가중치를 기준으로 오름차순 정렬
    edge = sorted(edge)

    # make set
    p = list(range(V+1))

    mst_weight = []
    # N은 정점의 갯수를 나타내는 변수
    N = V+1     # 정점은 0번부터 V번 까지 존재하기 때문에, V+1 개의 정점

    for i in range(E):
        w, n1, n2 = edge[i]
        
        # n1의 대표원소와, n2의 대표원소가 다르다면
        # 즉, 서로 다른 그룹이기 때문에, 사이클이 생기지 않음
        if find_set(n1) != find_set(n2):
            # 사이클이 생기지 않는다면, 가중치를 append
            mst_weight.append(w)

            # n2의 대표원소를 n1의 대표원소로 바꾸어 MST에 포함
            p[find_set(n2)] = find_set(n1)

            # 신장트리 : 정점 갯수-1 개의 간선으로 이루어진 트리
            if len(mst_weight) == N-1:
                break

    print('#{} {}'.format(tc, sum(mst_weight)))
