#برنامه ای بنویسید که یک متن دریافت نمایید اکر متن شامل هر کدام از کلامت زیر بود 
#["hack", "fraud", "scam", "password", "atack"] 
#ان کلمه را پیدا وتعداد نقدار ان را نمایش دهید 
#Input: 
#This is a password atack and another password atack
#Output: 
#password -> 2 
#attack -> 2

voroodi = input('متن خود را وارد کنید : ').lower()
word = ['hack','fraud','scam','password','attack']

words = voroodi.split()

for text in word :
    count = words.count(text)
    
    if count > 0 :
        print(text ,'--->',count)