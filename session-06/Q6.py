#تحلیل اطلاعات فروش
#اطلاعات فروش به شکل Tuple ذخیره شده است:

#sales = (
#(“Ali”, “Laptop”, 1200),
#(“Sara”, “Phone”, 800),
#(“Ali”, “Phone”, 800),
#(“Reza”, “Laptop”, 1200),
#(“Sara”, “Laptop”, 1200),
#(“Ali”, “Mouse”, 50)
#)

#هر Tuple شامل موارد زیر است:

#(customer, product, price)
#برنامه‌ای بنویسید که مشخص کند:

#هر مشتری چقدر خرید کرده است.
#کدام مشتری بیشترین خرید را داشته است.
#هر محصول چند بار فروخته شده است.
#مجموع درآمد فروشگاه چقدر است.
#مثال خروجی:

#Ali → 2050
#Sara → 2000
#Reza → 1200

#Total sales: 5250


sales = (
    ('Ali', 'Laptop', 1200),
    ('Sara', 'Phone', 800),
    ('Ali', 'Phone', 800),
    ('Reza', 'Laptop', 1200),
    ('Sara', 'Laptop', 1200),
    ('Ali', 'Mouse', 50)
)

customer_total = {}
product_count = {}
total_sales = 0

for customer, product, price in sales:
    # مجموع خرید هر مشتری
    if customer in customer_total:
        customer_total[customer] += price
    else:
        customer_total[customer] = price

    # تعداد فروش هر محصول
    if product in product_count:
        product_count[product] += 1
    else:
        product_count[product] = 1

    # مجموع درآمد فروشگاه
    total_sales += price

# نمایش مجموع خرید هر مشتری
print('خرید هر مشتری: ')
for customer, total in customer_total.items():
    print(customer, ' --> ', total)

# مشتری با بیشترین خرید
best_customer = max(customer_total, key=customer_total.get)
print('مشتری با بیشترین خرید:', best_customer)
print('مبلغ خرید:', customer_total[best_customer])

# تعداد فروش هر محصول
print('تعداد فروش محصولات:')
for product, count in product_count.items():
    print(product, ' --> ', count)

# مجموع درآمد فروشگاه
print('Total sales: ', total_sales)