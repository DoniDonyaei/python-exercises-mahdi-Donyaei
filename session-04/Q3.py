password = input (' لطفا رمز عبور خود را وارد کنید : ')
while True :
    if len(password) == 8 and password[:4].isalpha() and password[4:].isdigit():
        print (' رمز وارد شده معتبر است ')
        break
    else :
        print(' رمز وارد شده نامعتبر است ')
        password = input('لطفا رمز عبور خود را مجدد وارد کنید : ')
        