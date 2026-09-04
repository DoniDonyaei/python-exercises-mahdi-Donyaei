#برنامه ای بنویسید که رشنه ای از کاربر بگیرد و موارد زیر را محاسبه کند
#ﺣﺮوف اﻧﮕﻠﯿﺴﯽ
# ﺣﺮوف ﺑﺰرگ
# ﺣﺮوف ﮐﻮﭼﮏ
# اﻋﺪاد
# ﻓﺎﺻﻠﻪ
# ﮐﺎراﮐﺘﺮﻫﺎي خاص
#Input: 
#Python 123! ABC 
#Output: 
#Leters: 9 
#Uppercase: 4 
#Lowercase: 5 
#Digits: 3 
#Spaces: 2 
#Special characters: 1

voroodi = input('لطفا یک رشته وارد کنید : ')
letter = 0
upper = 0
lower = 0
digits = 0
spaces = 0
special = 0

for i in voroodi :
    if 'A'<= i <='Z' :
        letter +=1
        upper +=1
        
    elif 'a' <= i <= 'z' :
        letter +=1
        lower +=1
        
    elif i.isdigit():
        digits+=1
        
    elif i == ' ' :
        spaces +=1
        
    else:
        special +=1
        
print('letter : ',letter)
print('upper : ',upper)
print('lower : ',lower)
print('digits : ',digits)
print('spaces : ',spaces)
print('special : ',special)
    