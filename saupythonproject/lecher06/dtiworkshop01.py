# dtiworkshop01.py
#โปรเเกรมคำนวณหาพื้นที่สามเหลียม โดยรับค่าฐาน เเละสูงทางเเป้นพิมพ์เเละเเสดงผลพื้นที่สามเหลียมที่คำนวณได้ทางหน้าจอ

#วิเคราะห์
#มองหา featur การทำงานว่ามีอะไร
#1. รับค่า ฐาน สูง
#2. คำนวณพื้นที่ เเละเเสดงผลออกมา

def inputBaseHigh() :
    base = float(input('ป้อนฐาน :') )
    high = float(input('ป้อนสูง :') )
    return base,high

def calAndShowTriangleArea(base,high) :
    are = base * high / 2
    print(f'สามเหลี่ยมฐานฐ{base :.2f} สูง {high :.2f} มีพื้นที่ {are:.2f}')

print('-------------------------------')
print('--* Calculate')
