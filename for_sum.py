n = int(input())   #รับจำนวนรอบที่ต้องการเก็บใน list
lists2 = []        #ประกาศ list ว่าง
sum = 0            #เริ่มให้ค่า sum เท่ากับ 0

#รับค่าเอาไปเก็บ list
for i in range(n):
    x = int(input())    #รับจำนวนเต็มไปเก็บใน x
    lists2.append(x)    #เพิ่มค่าใน list
    sum = sum+x

for i in range(n):
    if (i<n-1):
        print(lists2[i],end = '+')
    else :
        print(lists2[i],end = '=')
print(sum)
