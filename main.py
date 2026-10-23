from shop.prices import total
from shop.discounts import apply_discount


bill = total(50,3)
print("Oreginal bill :",bill)
print("After Discount",apply_discount(bill))
