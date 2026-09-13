## تحلیل موجودی محصولات

#اطلاعات محصولات:

#products = {\
#“P01”: (“Laptop”, 1200, 5),\
#“P02”: (“Phone”, 800, 0),\
#“P03”: (“Tablet”, 500, 12),\
#“P04”: (“Mouse”, 50, 25),\
#“P05”: (“Keyboard”, 100, 0)\
#}

#ساختار هر محصول:

#(Product Name, Price, Stock)

#برنامه‌ای بنویسید که:

#- محصولات موجود را نمایش دهد.
#- محصولات ناموجود را نمایش دهد.
#- ارزش کل موجودی هر محصول را محاسبه کند.

#Price × Stock

#- محصول دارای بیشترین ارزش موجودی را پیدا کند.
#- ارزش کل انبار را محاسبه کند.


products = {
    'P01': ('Laptop', 1200, 5),
    'P02': ('Phone', 800, 0),
    'P03': ('Tablet', 500, 12),
    'P04': ('Mouse', 50, 25),
    'P05': ('Keyboard', 100, 0)
}

total_warehouse_value = 0
highest_value = 0
highest_value_products = []

print('محصولات موجود : ')

for product_id, product_info in products.items():
    name, price, stock = product_info

    if stock > 0:
        print('-', name)

print('محصولات ناموجود : ')

for product_id, product_info in products.items():
    name, price, stock = product_info

    if stock == 0:
        print('-', name)

print('ارزش موجودی هر محصول : ')

for product_id, product_info in products.items():
    name, price, stock = product_info

    inventory_value = price * stock
    total_warehouse_value += inventory_value

    print(name, ' : ', inventory_value)

    
    if inventory_value > highest_value:
        highest_value = inventory_value
        highest_value_products = [name]

    elif inventory_value == highest_value:
        highest_value_products.append(name)

print('محصولات با بیشترین ارزش موجودی : ')

for name in highest_value_products:
    print('-', name)

print('بیشترین ارزش:', highest_value)
print('ارزش کل انبار : ', total_warehouse_value)