#คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง เป็นการบ่งบอกว่ากสรทำงานนั้น ว่าเสร็จเเล้ว
def examplel () :
    print(111)
    print(222)
    return
    print(333)
    print(444)
    return

# Default Paramete
def dtiTest(x,y,x = 20 , a = 10) :
    print(f'{x} = {y} + {z} + {a} = {x+y+z+a}')


dtiTest(5,100)

dtiTest(9 , 8 , 10)