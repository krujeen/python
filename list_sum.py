a = []                         # กำหนด list a สำหรับเก็บข้อมูล
b = []                         # กำหนด list b สำหรับเก็บข้อมูล
n = int(input())               # รับค่า n เพื่อกำหนดจำนวนรอบที่รับค่า
for i in range (n):            # วนลูปรับค่าจำนวน n รอบ
    a.append(int(input()))     # รับค่าแล้วเพิ่มไว้ใน list a
    b.append(int(input()))     # รับค่าแล้วเพิ่มไว้ใน list b
for i in range (n):
    print("No",i," : ",a[i]+b[i]) # แสดงผลรวม ของ list a และ b ทีละคู่
