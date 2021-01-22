n = int(input())
lists2 = []
sum = 0

for i in range(n):
    x = int(input())
    lists2.append(x)
    sum = sum+x

for i in range(n):
    if (i<n-1):
        print(lists2[i],end = '+')
    else :
        print(lists2[i],end = '=')
print(sum)
