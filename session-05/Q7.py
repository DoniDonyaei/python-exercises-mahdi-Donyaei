#برنامه ای بنویسید که کاراکتر های متوالی یکسان را فشرده کنید
#aaabbccccd   : ورودي
#a3b2c4d1 : ﺧﺮوﺟﯽ

voroodi = input('لطفا رشته ی خود را وارد کنید : ')
payan = ''
i=0

while i < len(voroodi):
    count = 1 
    
    while i + 1 < len(voroodi) and voroodi[i]==voroodi[i+1]:
        count += 1
        i+= 1 
        
    payan += voroodi[i] +str(count)
    i+=1
    
print(payan)