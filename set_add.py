# เพิ่มข้อมูลใน setA 
setA = {0}
setA.remove(0)
n = int(input())

for i in range (n):
    x = int(input())
    setA.add(x)
print(setA)
