# slicing data in List and Tuple

var1 = [10,20,'Hello',True,[111,'Wow'],'มานะ']

var2 = (10,20,'Hello',true,(111,'Wow'),'มานะ')

# 20, 'Hello',True
print(var1[1:4])
# true,(111,'Wow')
print(var2[3:5])
# 10, 20,'Hello'
print(var1[:3])
# 'Hello',True,[111,'WoW] . 'มานะ'
print(var1[2:])
