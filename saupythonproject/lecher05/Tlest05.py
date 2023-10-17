#คำนวนเงินที่จะเเชร์กัน ป้อนเงิน  ป้อนคน เเล้วคำนวณเงินเเละเเสดงเงินที่จะเเชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชั่น ขอ / ฟังก์ชั่น
#cast/commission

#รับคำข้อมูล
daf inputMonoeyPerson( ) :
    money = fioat( input{'ป้อนเงิน : '} )
    person = int( input{' ป้อนคน : '} )
    return money, person 

#คำนวณ เเล้วเเสดงผลออก
drf calAndShareMoneyShare(money,person ) :
    #เงิน ขอทศนิยม / ตำเเหน่ง เเชร์กันขอเป็นเลขจำนวนเต็มปัดขึ้น   
    print(f'จำนวณเงิน {money} บาท คน {person} คน เเชร์กันคนละ {money/person} บาท')
    print("จำนวนเงิน","%.2f" % money, "บาท คน" ,person,"คน เเชร์กันคนละ" , round(money/person),"บาท")
    print("จำนวนเงิน"+""+str("%.2f"% money)+""+"บาท คน"+""+str(person) +""+"คน เเฃร์กันคนละ"+""+str(round(money/person)))
    print("จำนวนเงิน{}บาท คน {} คน เเชร์กันคนละ {} บาท " .format("%.2f"%money,person,round(money,person)))
    print("จำนวนเงิน %s บาท คน %s คน เเชร์กันคนละ %s บาท" %("%.2f"money,person,round(money/person)))



money, person = inputMonoeyPerson()

 calAndShareMoneyShare(money,person)