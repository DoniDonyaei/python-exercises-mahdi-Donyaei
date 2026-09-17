def process_order(customer, *products, **options):
    discount = options.get('discount', 0)
    tax = options.get('tax', 0)
    shipping = options.get('shipping', 0)

  #gheymat dehi mahsoolat
    prices = {
        'Laptop': 30000000,
        'Mouse': 500000,
        'Keyboard': 1000000
    }

    total_price = 0

    for product in products:
        total_price += prices.get(product, 0)

  #mohasebe takhfif 
    total_price = total_price - (total_price * discount / 100)

   #mohasbeye maliat
    total_price = total_price + (total_price * tax / 100)

   #mohasebe ye ersal
    final_price = total_price + shipping

    return {
        'customer': customer,
        'products': list(products),
        'discount': discount,
        'tax': tax,
        'shipping': shipping,
        'final_price': final_price
    }


order = process_order(
    'Ali',
    'Laptop',
    'Mouse',
    'Keyboard',
    discount=10,
    tax=9,
    shipping=200000
)

#print nahaei va zire ham 
for key, value in order.items():
    print(key, ':', value)