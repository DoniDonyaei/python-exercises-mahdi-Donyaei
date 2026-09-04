#برنامه ای بنویسید که یک رشته دریافت کند وتمام کاراکتر هایی که بیش از یک بار تکرار شدند را حذف نماید به طوری که فقط اولین مقدار باقی بماند
#input : programming
#output : progamin

voroodi = input('لطفا رشته ی خود را وارد کنید : ').strip()
a =''

for i in voroodi:
    if i not in a:
        a+= i
        
print(a)