import random

#مقدار دهی اولیه امتیاز ها 
user_wins = 0 
computer_wins = 0

options = ['سنگ','کاغذ','قیچی']
while True:
    user_input = input(" انتخاب کنید : سنگ و کاغذ و قیچی یا خروج  : ")
    if user_input == 'خروج':
        break
    
    if user_input not in options :
        print('گزینه ی صحیح را انتحاب کنید')
        continue
    #اگر ورودی کاربر غیر از این ها بود دوباره میپرسیم با continue

    random_number = random.randint(0,2)
                    #سنگ 1و کاغذ 1و قیچی2
    computer_pick = options[random_number]
    print("انتخاب کامپیوتر : ", computer_pick, ' است')
    
    if user_input == 'سنگ' and computer_pick == 'قیچی' :
        print('**شما برنده شدید **')
        user_wins +=1
        continue
    
  
    elif user_input == 'کاغذ' and computer_pick == 'سنگ' :
        print('**شما برنده شدید **')
        user_wins +=1
        


    elif user_input == 'قیچی' and computer_pick == 'کاغذ' :
        user_wins +=1
        print ('** شما برنده شدید **')
        
    elif user_input == computer_pick :
        print('برابر شدید :(')
        continue 
        
        
    else:
        print('شما باختید :(')
        computer_wins +=1
        
#نتیچه نهایی قبل خروج

print('شما ',user_wins,' بار برنده شدید')
print('کامپیوتر ',computer_wins ,' بار بنده شد ')
        
print('خدا نگهدار')