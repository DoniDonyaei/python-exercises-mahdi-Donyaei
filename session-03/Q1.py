#بزرگ‌ترین عدد لیست زیر را پیدا کنید
#[15,50,70,1,90,20,4,108,6]

numbers =[15,50,70,1,90,20,4,108,6]
#اولین عدد رو بزرگترین در نظر میگیریم در ابتدا
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number     
        #گر شرط درست بود عدد جدید را میریزیم تو largest
print ('بزرکترین عدد این لیست ',largest,'است')