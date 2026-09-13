## گروه‌بندی سفارش‌ها

#لیست زیر اطلاعات سفارش‌هاست:

#orders = [\
#(“Ali”, “Laptop”),\
#(“Sara”, “Phone”),\
#(“Ali”, “Phone”),\
#(“Reza”, “Laptop”),\
#(“Sara”, “Laptop”),\
#(“Ali”, “Tablet”),\
#(“Reza”, “Phone”)\
#]

#**Dictionary**ای ایجاد کنید که مشخص کند هر مشتری چه محصولاتی سفارش داده است.

#**خروجی:**

#{\
#“Ali”: [“Laptop”, “Phone”, “Tablet”],\
#“Sara”: [“Phone”, “Laptop”],\
#“Reza”: [“Laptop”, “Phone”] }


orders = [
    ('Ali', 'Laptop'),
    ('Sara', 'Phone'),
    ('Ali', 'Phone'),
    ('Reza', 'Laptop'),
    ('Sara', 'Laptop'),
    ('Ali', 'Tablet'),
    ('Reza', 'Phone')
]

customer_orders = {}

# ساخت دیکشنری سفارش‌ها
for customer, product in orders:
    if customer in customer_orders:
        customer_orders[customer].append(product)
    else:
        customer_orders[customer] = [product]

# چاپ زیر هم
for customer, products in customer_orders.items():
    print(customer + ' : ')

    for product in products:
        print('-', product)

    print()