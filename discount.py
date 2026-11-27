
amount = float(input("Enter purchase amount: "))

if amount < 2000:
    discount_rate = 5
elif amount <= 5000:
    discount_rate = 10
else:
    discount_rate = 15

discount = amount * discount_rate / 100
amount_after_discount = amount - discount

gst = amount_after_discount * 5 / 100
final_amount = amount_after_discount + gst

print("\n----- PURCHASE BILL -----")
print("Purchase Amount: Rs.", amount)
print("Discount:", discount_rate, "%")
print("Discount Amount: Rs.", discount)
print("Amount After Discount: Rs.", amount_after_discount)
print("GST (5%): Rs.", gst)
print("Final Payable Amount: Rs.", final_amount)
