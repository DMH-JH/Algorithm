import sys
sys.stdin = open('input.txt')
# N : 스위치 개수
N = int(input())
status = [9]
status += list(map(int, input().split()))
student_cnt = int(input())
student_info = []
for _ in range(student_cnt):
    student_info.append(list(map(int, input().split())))

for i in range(student_cnt):
    # 학생이 남자라면
    if student_info[i][0] == 1:
        j = 1
        while (student_info[i][1] * j) <= N:
            status[student_info[i][1] * j] = int(not status[student_info[i][1] * j])
            j += 1
    # 학생이 여자라면
    if student_info[i][0] == 2:
        status[student_info[i][1]] = int(not status[student_info[i][1]])
        x1 = student_info[i][1]-1
        x2 = student_info[i][1]+1
        while x1 in range(N+1) and x2 in range(N+1) and status[x1] == status[x2]:
            status[x1] = int(not status[x1])
            status[x2] = int(not status[x2])
            x1 = x1 - 1
            x2 = x2 + 1
for i in range(1, N+1):
    print(status[i], end=' ')
    if i % 20 == 0:
        print()