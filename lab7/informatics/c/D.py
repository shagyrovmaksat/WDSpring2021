s = input().split()
cnt = 0
for i in range(1, len(s)):
    if int(s[i]) > int(s[i-1]):
        print(s[i], end = ' ')