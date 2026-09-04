#برنامه ای بنویسید که یک جمله دریافت کند و طولانی ترین کلمه را پیدا کند.اکر چند کلمه طول یکسان داشتند اولین کلمه را نمایش بده
#Input: 
#Python programming is extremely interesting 
#Output: 
#extremely 
#Length: 9 

voroodi = input('لطفا یک جمله وارد کنید : ')
words = voroodi.split()
longest_word = ''

for word in words :
    if len(word) > len(longest_word):
        longest_word = word 
        
print('longest word : ', longest_word )
print('lenght : ',len(longest_word))