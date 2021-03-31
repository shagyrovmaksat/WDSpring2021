if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
for i in range(0,n-1):
    for j in range(i+1, n):
        if(arr[i] > arr[j]):
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

for i in range(n-1, 0, -1):
    if(arr[i-1] != arr[i]):
        print(arr[i-1])
        break