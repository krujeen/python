# แสดงเลข 1-10 แต่ เมื่อ i มีค่าเท่ากับ 5 ถูก break จึงแสดงได้เพียงเลข 1-4
i = 1
while i < 11:
  if (i == 5):
    break            # จะไม่ทำคำสั่งหลังจาก break แล้วออกจากลูป
  print(i)
  i += 1
  

# แสดงเลข 1-10 แต่ เมื่อ i มีค่าเท่ากับ 5 ถูก break จึงแสดงได้เพียงเลข 1-4
i = 0
while i < 10:
  i += 1
  if (i == 5):
    break             # จะไม่ทำคำสั่งหลังจาก break แล้วออกจากลูป
  print(i)
  

# แสดงเลข 1-10 แต่ เมื่อ i มีค่าเท่ากับ 5 ถูก continue คือข้ามเลข 5 ไป จึงแสดงได้เพียงเลข 1-10 ยกเว้นเลข 5
i = 0
while i < 10:
  i += 1
  if (i == 5):
    continue          # จะไม่ทำคำสั่งหลังจาก continue แล้วกลับเข้าไปวนลูปต่อ
  print(i)
