#แสดงข้อมูลใน setA
setA = {"apple", "banana", "cherry"}
print(setA)


#แสดงข้อมูลใน setA ทีละตัว
setA = {"apple", "banana", "cherry"}
for x in setA:
  print(x)


# ตรวจสอบว่า มีข้อมูลใน setA หรือไม่ด้วย คำสั่ง in
setA = {"apple", "banana", "cherry"}
print("banana" in setA)


# เพิ่มข้อมูลใน setA 
setA = {"apple", "banana", "cherry"}
setA.add("orange")
print(setA)


# แก้ไขข้อมูลใน setA  
setA = {"apple", "banana", "cherry"}
setA.update(["orange", "mango", "grapes"])
print(setA)


# ลบ banana ออกจาก setA ด้วยคำสั่ง remove  แต่ถ้าไม่มี banana จะ error
setA = {"apple", "banana", "cherry"}
setA.remove("banana")
print(setA)


# ลบ banana ออกจาก setA ด้วยคำสั่ง discard แต่ถ้าไม่มี banana จะไม่ error
setA = {"apple", "banana", "cherry"}
setA.discard("banana")
print(setA)


# นับจำนวนข้อมูลที่มีใน setA
setA = {"apple", "banana", "cherry"}
print(len(setA))
