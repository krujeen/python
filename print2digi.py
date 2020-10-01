a,b,c = [int(e) for e in input().split()]

result = a*b/c


# แสดง ทศนิยม 2 ตำแหน่ง ด้วยคำสั่ง round
print (round(result,2),"cm.")

# แสดง ทศนิยม 2 ตำแหน่ง ด้วย %.2f
print ('%.2f cm.'%(result))
