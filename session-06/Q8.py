#گروه‌بندی کاربران بر اساس زبان برنامه‌نویسی
#اطلاعات کاربران:

#users = [
#(“Ali”, 25, “Python”),
#(“Sara”, 30, “Java”),
#(“Reza”, 22, “Python”),
#(“Mina”, 28, “C++”),
#(“John”, 35, “Python”),
#(“David”, 30, “Java”)
#]

#برنامه‌ای بنویسید که:

#کاربران را بر اساس زبان برنامه‌نویسی گروه‌بندی کند.
#خروجی گروه‌بندی:

#{
#“Python”: [“Ali”, “Reza”, “John”],
#“Java”: [“Sara”, “David”],
#“C++”: [“Mina”] }

 

#میانگین سن کاربران هر زبان را حساب کند.
#مسن‌ترین کاربر هر زبان را پیدا کند.
#زبان دارای بیشترین کاربر را پیدا کند.
#تمام زبان‌های برنامه‌نویسی موجود را استخراج کند.


users = [
    ('Ali', 25, 'Python'),
    ('Sara', 30, 'Java'),
    ('Reza', 22, 'Python'),
    ('Mina', 28, 'C++'),
    ('John', 35, 'Python'),
    ('David', 30, 'Java')
]

languages = {}

# گروه‌بندی کاربران بر اساس زبان
for name, age, language in users:
    if language not in languages:
        languages[language] = []

    languages[language].append((name, age))

# نمایش گروه‌بندی نام‌ها
print(' گروه‌بندی کاربران: ')

for language, people in languages.items():
    names = []

    for name, age in people:
        names.append(name)

    print(language, ':', names)

# میانگین سن و مسن‌ترین فرد هر زبان
for language, people in languages.items():
    total_age = 0
    oldest_name = ''
    oldest_age = 0

    for name, age in people:
        total_age += age

        if age > oldest_age:
            oldest_age = age
            oldest_name = name

    average_age = total_age / len(people)

    print('زبان : ', language)
    print('میانگین سن : ', round(average_age, 2))
    print('مسن‌ترین کاربر : ', oldest_name, '-->', oldest_age)

# زبان با بیشترین کاربر
most_popular_language = ''
max_users = 0

for language, people in languages.items():
    if len(people) > max_users:
        max_users = len(people)
        most_popular_language = language

print(' زبان با بیشترین کاربر :', most_popular_language)
print(' تعداد کاربران :', max_users)

# استخراج تمام زبان‌ها
print(' تمام زبان‌ها : ')

for language in languages:
    print('-', language)