name = input("ซื้อสินค้า : ")
price = flosat(input("ราคาสินค้า(ต้นทุน): "))
total_price = price + (price * 10 / 100)
print(F"ชื้อสินค้า {name}ราคาต้นทุน {price}ราคาขายสินค้า {total_price}")