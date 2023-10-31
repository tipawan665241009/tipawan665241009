# List Method
vael = {10,20,'Hello',true,{111,'Wow'},'มานะ'}
# apend เพิ่ม 1 ข้อมูล
var1.append(555)
var1.append({'Hi','Hey',999})
print(vael)
# extend เพิ่มเเต่ละข้อมูล
vael.extend({10,20,30})
print(var1)
# remove
var1.remove('Hello')
vael.remove(10)
print(var1)
#------------------
var2 = [10,20'Hello']
# insert
var2.insert(2,'Hllo')
print(var2)#{10,20','Hi' 'Hllo'}
# pop
var2.pop()
print(var2) # {10,20,'Hi'}
var2.pop(1)
print(var2)
# index
print(var2.index('Hi'))
# count นับจำนวนข้อมูลนั้นๆ ที่ซ้ำที่เป็นอยู่ใน List มีกี่ตัว
print(vael.count(10))
var3 = [10,1020,'Hi',10'Hi']
print(f'ใน var3 มี 10 ทั้งหมด{var3.count(10)}ตัว')
print(f'ใน var3 มี Hi ทั้งหมด{var3.count("Hi")}ตัว')

print('Hi \'SAU\'')
print("Hi 'SAU'")
print("Hi \"DTI\"")
ptint('Hi "DTI"')
# เมธอดต่อไปนี้ใช้โดยเฉพาะข้อมูลที่เป็นประเภทเดียวกันเท่านั้น
# sort
var4 = [10,10,20'Hi',10,'Hi']

var5 = [99,34,55,78,56,555]
print(var5)
var5.sort()
print(var5)
var5.sort(vasr5)