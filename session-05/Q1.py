#برنامه ای بنویسید که یک رمز عبور از کاربر دریافت کند و موارد را بررسی کند:
    #حداقل 8 کاراکتر باشد
    #حداقل یک حرف بزرگ داشته یاشد
    #حداقل یک حرف کوچک داشته یاشد
    #حداقل یک عدد داشته باشد
    #حداقل یک کاراکتر خاص مثل% $ # @ داشته باشد
    #اگر رمز معتبر نبود دلیل نامعتبر بودن را نمایش دهید

while True:
    

    password = input ('لطفا رمز خود را وارد کنید : ')
    errors = []
    
    if len (password)<8:
        errors.append('رمز وارد شده حد اقل باید 8 کاراکتر داشته باشد !!!')

    if not any(i.isupper()for i in password ):
        errors.append('حد اقل در موارد وارد شده از یک حرف بزرگ استفاده کنید !!!')

    if not any(i.islower()for i in password ):
        errors.append('حد اقل در موارد وارد شده از یک حرف کوچک استفاده کنید !!!')
    
    if not any(i.isdigit()for i in password ):
        errors.append('در کاراکتر های وارد شده از عدد نیز استفاده کنید !!!')
    if not any (i in '@#$%' for i in password ):
        errors.append('لطفا از یک کاراکتر خاص در رمز استفاده کنید !!!')
    
    if errors:
        print('رمز نامعتبر است : ')
        for error in errors:
            print('-',error)
            
        print('مجدد وارد کنید  ')
        
    else:
        print('رمز معتبر است')
        break
