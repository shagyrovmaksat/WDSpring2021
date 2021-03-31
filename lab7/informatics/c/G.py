a = [int(i) for i in input().split()]
indMax = 0
valMax = a[indMax]
for i in range(1, len(a)):
    if a[i] > valMax:
        valMax = a[i]
        indMax = i
print(valMax, indMax)