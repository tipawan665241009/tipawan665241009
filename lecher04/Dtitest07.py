idemp = input("รหัสพนักงาน : ")
nameEMP = input("ชื่อพนักงาน : ")
salaryemp = flosat(input("เงินเดือนพนักงาน : "))
sum = salaryemp - (salaryemp * 7 / 100) - 500
print(F"รหัสพนักงาน {idemp}ชื่อพนักงาน{nameEMP} เงินเดือนสุทธิ์  {sum}")