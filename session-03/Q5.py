#ماشین حساب
#دو عدد و یک عملگر (+ – * /) دریافت کنید و نتیجه را نمایش دهید.

num1 = float(input('لطفا عدد اول خود را وارد کنید : '))
operator = input('چه عملی میخواهید انجام دهید؟   + * / - : ')
num2 = float(input('لطفا عدد دوم خود را وارد کنید : ' ))
a=0
if operator == '+' :
    a = num1+num2

elif operator == '-' :
    a = num1-num2

elif operator == '*' :
    a = num1*num2 
    
elif operator == '/' :
        if num2==0:
            print('قابل اجرا نیست ')
        else:
            
            a = num1/num2
    
else:
    print('عملیات خواسته شده پشتیبانی نمیشود !!! ')
    
print (a)