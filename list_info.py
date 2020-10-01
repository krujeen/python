# เก็บและแสดงข้อมูลใน list1
list1 = ["apple", "banana", "cherry"]
print(list1)


# แสดงข้อมูลตัวแรกของ list1
print(list1[0])


# แสดงข้อมูลตัวสุดท้ายของ list1
print(list1[-1])


# แสดงข้อมูลตัวที่ 0 ถึง 3 ของ list2
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list2[:4])

# แสดงข้อมูลตัวที่ 2 ถึง 4 ของ list2
print(list2[2:5])

# แสดงข้อมูลตัวที่ 2 เป็นต้นไปของ list2
print(list2[2:])


# แสดงข้อมูล 3 ตัวสุดท้ายของ list2
print(list2[-3:])


# เปลี่ยนข้อมูลตำแหน่งที่ 1 ใน list3 เป็น kiwi
list3 = ["apple", "banana", "cherry"]
list3[1] = "kiwi"
print(list3)
