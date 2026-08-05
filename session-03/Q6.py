#میانگین
#از کاربر ۱۰ عدد دریافت کرده و میانگین آن‌ها را محاسبه کنید.

sum = 0 
for i in range(10):
    num=float(input('لطفا عدد خود را وارد کنید : '))
    i+=1
    sum = sum + num 
    
average = sum / 10 

print ('میانگین شما ',average,'است')