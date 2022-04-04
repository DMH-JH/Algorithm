while True:
    ans = 'yes'
    input_str = input()
    if input_str == '0':
        break
    else:
        for i in range(len(input_str) // 2):
            if input_str[i] != input_str[-1-i]:
                ans = 'no'
                break
        print(ans)