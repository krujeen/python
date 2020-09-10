a = int(input())
b = int(input())

if (a>=b) :
  n = a-b+1
else :  
  n = b-a+1

for i in range (n) :
  if (a<b):
    print (a,end=' ')
    a = a+1
  else :
    print (a,end=' ')
    a = a-1
