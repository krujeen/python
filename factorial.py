def fac (n) :
    a = 1
    for i in range (1,n+1) :
        a = a*i
    return a

x = int(input())
sum = 0

for i in range (1,x+1):
    sum = sum+fac(i)  
    
print(sum)
