s = input().split()
for i in range(1, len(s)):
    if int(s[i]) > 0 and int(s[i-1]) > 0 or int(s[i]) < 0 and int(s[i-1]) < 0:
        print(s[i-1], s[i], end = ' ')
        break