#برنامه ای بنویسید و یک سیستم log in طراحی کنید که user , password  از کاربر بگیرد. کاربر حد اکثر 3 بار فرصت دارد
#اگر username o password اشتباه بود چیام زیر ارسال شود  به همراه تعداد تلاش ناموفق
#Wrong username or password 
#Atempts remaining: 2
#اگر درست بود پیام زیر را بد
#Login successful

username = input('لطفا نام کاربری خود را وارد کنید : ')
password = input('لطفا رمز عبور خود را وارد کنید : ')
print('**** مشخصات شما ثبت شد ****')

for atempt in range(3):
    username1 = input('برای ورود نام کاربری خود را وارد کنید : ')
    password1 = input ('لطفا رمز عبور هود را وارد کنید : ')
    
    if username == username1 and password == password1 :
        print('login successful ')
        break
    
    else :
        remaining = 2 - atempt 
        
        print('رمز عبور یا نام کاربری اشتباه است ')
        print('تلاش باقی مانده : ',remaining)
        
        if remaining == 0 :
            print('دیگر نمیتوانید تلاش کنید ')