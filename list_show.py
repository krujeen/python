# รับข้อมูลแล้วเก็บเข้าไปใน list
lists1 = []
lists1 = [int(e) for e in input().split()]


# นับจำนวข้อมูลใน list
n = len(b)

# วนลูป เพื่อแสดงข้อมูลใน list ตามรูปแบบที่กำหนด
for i in range (0,n) :
    print (lists1[i],end = ', ')
