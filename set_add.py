# เพิ่มข้อมูลใน setA 
setA = {0}
setA.remove(0)
n = int(input())

for i in range (n):
    x = int(input())
    setA.add(x)
print(setA)




# setA 
setA = {0}
setA.remove(0)
# อ่านข้อมูลหลาย ๆ ตัวที่ผู้ใช้ป้อนเข้ามาในบรรทัดเดียวกัน โดยข้อมูลแต่ละตัวคั่นด้วยช่องว่าง  แปลงเป็น integer แล้วเก็บไว้ใน list 
setA = {int(e) for e in input().split()}

for x in setA:
  print(x)



