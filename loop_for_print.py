#for Loop มีรูปแบบ for i in range: เช่น วนลูปปริ้น 0-10
for i in range(11):
  print(i)

  
    #for Loop มีรูปแบบ for i in range: เช่น วนลูปปริ้น 1-10
for i in range(1,11):
	print(i)

	
#for Loop มีรูปแบบ for i in range: เช่น วนลูปปริ้น 11-20
for i in range(11,21):
	print(i)

		
#for Loop มีรูปแบบ for i in range: เช่น วนลูปปริ้น 2 - 20 เฉพาะเลขคู่ (เพิ่มทีละ 2)
for i in range(2,21,2):
	print(i)
	
	
#for Loop มีรูปแบบ for i in range: เช่น วนลูปปริ้น 1-5 เมื่อครบแล้วให้แสดงว่า เสร็จสิ้น
for x in range(6):
  print(x)
else:
  print("เสร็จสิ้น")


#แสดงผลไม้ ใน list ยกเว้น กล้วย เพราะมีเงื่อนไข if ให้ continue ข้ามไป เมื่อเจอ banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
