import math  # math.sqrt(x)

a,b,c = [int(e) for e in input().split()]


result1 = (-b+(math.sqrt(b*b-4*a*c)))/(2*a)
result2 = (-b-(math.sqrt(b*b-4*a*c)))/(2*a)
print (result1,' ',result2)
