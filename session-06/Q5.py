#اطلاعات دانش‌آموزان
#اطلاعات زیر را داریم:

#students = {
#“Ali”: [18, 17, 20],
#“Sara”: [15, 19, 18],
#“Reza”: [12, 14, 10],
#“Mina”: [20, 20, 19] }

#برنامه‌ای بنویسید که برای هر دانش‌آموز:

#میانگین را محاسبه کند.
#وضعیت قبولی را مشخص کند.
#بالاترین نمره او را پیدا کند.
#قانون:

#Average >= 15 → Passed
#Average < 15 → Failed

#خروجی:
#Ali
#Average: 18.33
#Status: Passed

#Sara
#Average: 17.33
#Status: Passed

#در پایان نیز:

#بهترین دانش آموز
#بالاترین میانگین
#را نمایش دهید.


students = {
    'Ali': [18, 17, 20],
    'Sara': [15, 19, 18],
    'Reza': [12, 14, 10],
    'Mina': [20, 20, 19]
}

best_student = ''
highest_average = 0

for name, grades in students.items():
    # محاسبه میانگین
    average = sum(grades) / len(grades)

    # بالاترین نمره
    highest_grade = max(grades)

    #  وضعیت قبولی
    if average >= 15:
        status = 'Passed'
    else:
        status = 'Failed'

    # نمایش اطلاعات 
    print(name)
    print('Average:', round(average, 2))
    print('Status:', status)
    print('Highest grade:', highest_grade)
    print()

    # پیدا کردن بهترین دانش‌آموز
    if average > highest_average:
        highest_average = average
        best_student = name

print('Best student:', best_student)
print('Highest average:', round(highest_average, 2))
