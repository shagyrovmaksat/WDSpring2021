def Xor(a, b):
    if(a == 1 and b == 0 or a == 0 and b == 1):
        return 1
    return 0
s = input().split()
a = int(s[0])
b = int(s[1])
print(Xor(a, b))