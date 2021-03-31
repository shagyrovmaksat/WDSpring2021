s = input().split()
cnt = 0
for i in range(0, len(s)):
    if int(s[i]) > 0:
        cnt += 1
print(cnt)