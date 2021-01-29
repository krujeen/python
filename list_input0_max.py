lists1 = []
x = 1

while (x != 0):
    x = int(input())
    if (x!=0) :
        lists1.append(x)

n = int(len(lists1))
print (n)

lists1.sort(reverse=True)
print (lists1[0])

for i in range (0,n) :
    print (lists1[i],end = ', ')
