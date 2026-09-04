#برنامه ای بنویسید که جمله دریافت کند و مشخص کنید کدام کلمه بیشترین نعداد تکرار را دارد
#Input: 
#python is easy and python is powerful and python is popular 
#python -> 3 

voroodi = input('لطفا جمله ی خود را وارد کنید : ')
words = voroodi.split()

max_word = ''
max_count = 0

for word in words :
    count = words.count(word)
    
    if count > max_count:
        max_count = count
        max_word = word
 
if max_count > 1 :
    
    print(max_word, "--->", max_count)

else :
    print('کلمه تکراری وجود ندارد !!!')
