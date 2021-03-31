def min(a, b, c, d):
    m = [a, b, c, d]
    m.sort()
    return m[0]
s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
print(min(a,b,c,d))