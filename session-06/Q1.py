#برنامه‌ای بنویسید که:
#- گران‌ترین محصول را پیدا کند.
#- ارزان‌ترین محصول را پیدا کند.
#- میانگین قیمت محصولات را حساب کند.
#- محصولاتی که قیمتشان بیشتر از 500 است را نمایش دهد.
#- مجموع قیمت تمام محصولات را حساب کند.

products = {
  'laptop': 1200,
  'phone': 800,
  'tablet': 500,
  'headphone': 150,
  'mouse': 50
  }

# گران‌ترین محصول
most_expensive = max(products, key=products.get)
print('گران‌ترین محصول:', most_expensive, '-', products[most_expensive])

# ارزان‌ترین محصول
cheapest = min(products, key=products.get)
print('ارزان‌ترین محصول:', cheapest, '-', products[cheapest])

# مجموع و میانگین قیمت‌ها
total_price = sum(products.values())
average_price = total_price / len(products)

print('مجموع قیمت‌ها:', total_price)
print('میانگین قیمت‌ها:', average_price)

# محصولات با قیمت بیشتر از 500
print('محصولات گران‌تر از 500:')
for product, price in products.items():
    if price > 500:
        print(product, '-', price)