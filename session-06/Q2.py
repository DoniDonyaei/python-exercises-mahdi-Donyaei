#دیکشنری زیر تعداد موجودی محصولات را نشان می‌دهد:
#inventory = {
#“apple”: 20,
#“banana”: 5,
#“orange”: 0,
#“milk”: 12,
#“bread”: 0
#}
#برنامه‌ای بنویسید که محصولات را به دو دسته زیر تقسیم کند:
#- Available:
#  apple
# banana
# milk
# Out of stock:
# orange
# bread
#سپس تعداد محصولات موجود و ناموجود را نیز نمایش دهید.


inventory = {
   'apple': 20,
   'banana': 5,
   'orange': 0,
   'milk': 12,
   'bread': 0
  }

#دو لیست خالی برای جدا کردن محصولات
available = []
out_of_stock = []


#بررسی دونه به دونه محصولات
for product, count in inventory.items():
    if count > 0:
        available.append(product)
    else:
        out_of_stock.append(product)
        

print('Available:')
for product in available:
    print(product)

print('Out of stock:')
for product in out_of_stock:
    print(product)

#تعداد محصول 
print('تعداد محصولات موجود:', len(available))
print('تعداد محصولات ناموجود:', len(out_of_stock))       