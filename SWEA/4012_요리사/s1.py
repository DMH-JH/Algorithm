import sys
sys.stdin = open('input.txt')
from itertools import combinations


def calculate_taste(taste_diff, food_A, food_B):

    food_A_comb_list = list(combinations(food_A, 2))
    food_B_comb_list = list(combinations(food_B, 2))

    temp1 = 0
    temp2 = 0
    for comb_a in food_A_comb_list:
        temp1 += arr[comb_a[0]][comb_a[1]] + arr[comb_a[1]][comb_a[0]]

    for comb_b in food_B_comb_list:
        temp2 += arr[comb_b[0]][comb_b[1]] + arr[comb_b[1]][comb_b[0]]

    taste_diff.append(abs(temp1 - temp2))


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 요리의 시너지 정보가 들어있는 list
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 식재료 종류
    food_list = list(range(N))

    combi_list = list(combinations(food_list, N // 2))

    # 각 조합의 맛의 차이 값 저장 list
    taste_diff = []

    # 식재료 A와 B로 나누는 과정
    for comb in combi_list:
        food_A = comb
        food_B = food_list[:]
        for i in range(len(food_A)):
            food_B.remove(food_A[i])
        # print(list(food_A), food_B)

        calculate_taste(taste_diff, food_A, food_B)

    print('#{} {}'.format(tc, min(taste_diff)))




