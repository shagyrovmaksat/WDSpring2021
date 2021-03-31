n = int(input())
m = 1
print(1, end = ' ')
while m < n:
   if(m < n):
      if (m * 2 > n):
         break
      else:
         m = m * 2
         print(m, end = ' ')