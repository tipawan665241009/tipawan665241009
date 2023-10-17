#โปรมเเกมตรวจสอบน้ำหนักรถบรรทุกของของด่านข้างน้ำหนักว่ารถบรรทุกนั้นมีน้ำหนักรถผ่านเกณฑ์หรือไม่
#หากน้ำหนักเกิน 1000kg ให้เเสดงข้อความว่า "รถน้ำหนักผ่านเกรณฑ์" เเต่หากน้ำหนักตั้งเเต่
#1000kg ลงมาให้เเสดงข้อความว่า "รถน้ำหนักผ่านเกรณฑ์" โดยให้ป้อนทะเบียนรถบรรทุก
#เเละน้ำหนักรถบรรทุกทางเเป้นพิมพ์         

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะไปสร้างเป็น function
# รับค่าทะเบียนรถ น้ำหนัก -> inputCarDetail
# ตรวจสอบน้ำหนักรถ เเละเเสดงผล -> checkCarAndShowWeight

def inputCarDetail():
    carNo = float(input('ป้อนทะเบียนรถ: '))
    carweight = float(input("ป้อนน้ำหนักรถ: "))
    return carNo, carweight

def checkCarAndShowWeight(carNo, carweight):
    if carweing > 1000:
        print (f'ทะเบียนรถ {carNo} น้ำหนักไม่ผ่านเกรณฑ์')
    else:
        print(f'ทะเบียนรถ {carNo} น้ำหนักผ่านเกรณฑ์')



print("----------------------")
print("TruckChecker")
print("----------------------")

CarNo, carweight = inputCarDetail()
print("-------------------------------")
checkCarAndShowWeight(carNo, carweight)
print("-------------------------------")