#โปรมเเกมคำนวนหาพื้นที่วงกลม เส้นรอบวงกลม เเละปริมาณตรทรงกลม จากรัศมีที่ป้อนโดยผู้ใช้ทางเเป้นพิมพ์ เเละเเสดงผลพื้นที่ เส้นรอบ เเละปรืมาณทางหน้าจอ

#ขอ 5 ฟังช์ชั่น
import math
#inputRadius
def inputRadius() :
    # r = input('ป้อนรัศมี :)
    #retutn r

#r = float( 'ป้อนรัศมี :')
#return r

#return input('ป้อนรัศมี :')

return float( input('ป้อนรัศมี :'))

#calAreaCircle
def calAreaCircle( r ) :
    #area = math.pi = r **2
    #area = math.pi = r * r *
    #area = math.pi = math.pow(r,2)
    #ratuen area
    return math.pi * math.pow(r,2)

    #calRoundCi 2 *PI * r


#calCubecirle 4/3 * PI * r * r * r
def calAreaCircle(r) :
    #round = 2 * math.pi *r
    return 2 * math.pi * r


#scalcubeCircle 4/3 * pi *r*r*r
def caiCubcircle(r) : 
    #cube = 4/3* math.pi *r*r*r
    return 4/3 * math.pi *r*r*r


#showResuit ขอทั้งหมดทัศนิยม 4 ตำเเหน่ง
#พื้นที่วงกลม เส้นรอบวง ปริมาตรทรงกลมเป็น
def showResuit():
    radius = inputRadius()
    area = calAreaCircle(radius)
    perameter = calAreaCircle(radius)
    volume = calAreaCircle(radius)
    print('Radius: ' '%.4f' %radius)
    print('Area:' '%.4f' %area)
    print('perameter:' '%.4f' %petameter)
    print('volume:' '%.4f' %volume)

showResult()
