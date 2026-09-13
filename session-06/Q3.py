### شمارش حروف با Dictionary

#یک رشته دریافت کنید.
#با استفاده از **Dictionary** مشخص کنید هر حرف چند بار تکرار شده است.
#مثال خروجی:
#{\
#“p”: 1,\
#“r”: 2,\
#“o”: 1,\
#“g”: 2,\
#“a”: 1,\
#“m”: 2,\
#“i”: 1,\
#“n”: 1\
#}
#programming
#**نکته:** فاصله‌ها و کاراکترهای خاص را در نظر نگیرید.

text = input('لطفا یک جمله یا رشته وارد کنید :  ')

letter_count = {}

for char in text:
#char فقط حروف را بررسی میکنیم
    if char.isalpha():
        #lower برای بزرگ و کوچک مهم نبودن
        char = char.lower()  
        
        #برای شمارش حروف
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

print(letter_count)