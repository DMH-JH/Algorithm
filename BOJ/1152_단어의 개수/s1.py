# 단어의 개수 - 브2
str1 = input()

strip_str = str1.strip()
if len(strip_str):
    answer = 1
    for c in strip_str:
        if c == ' ':
            answer += 1
else:
    answer = 0

print(answer)
