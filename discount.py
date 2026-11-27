amount=float(input("Enter the amount:"))
if amount < 2000:
    discount_rate = 5
elif amount <=5000:
    discount_rate = 10
else:
    discount_rate = 15

discount=amount * (discount_rate / 100)
final_amount=amount - discount
print("------purchase bill")        
print("Amount: Rs.", amount)
print("Discount Rate:", discount_rate, "%")
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)    