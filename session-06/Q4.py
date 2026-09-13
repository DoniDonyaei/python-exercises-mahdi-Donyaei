#اطلاعات کارمندان
#اطلاعات چند کارمند به صورت زیر ذخیره شده است:

#employees = {
#“E01”: {
#“name”: “Ali”,
#“age”: 28,
#“salary”: 3000
#},
#“E02”: {
#“name”: “Sara”,
#“age”: 32,
#“salary”: 4500
#},
#“E03”: {
#“name”: “Reza”,
#“age”: 25,
#“salary”: 2800
#}
#}

#برنامه‌ای بنویسید که:

#کارمندی که بیشترین حقوق را دارد پیدا کند.
#میانگین حقوق را محاسبه کند.
#کارمندان با حقوق بیشتر از 3000 را نمایش دهد.
#نام کارمندی که کمترین حقوق را دارد نمایش دهد.


employees = {
  'E01': {
      'name': 'Ali',
      'age': 28,
      'salary': 3000
    },
   'E02': {
      'name': 'Sara',
      'age': 32,
      'salary': 4500
    },
    'E03': {
        'name': 'Reza',
        'age': 25,
        'salary': 2800
    }
}

# کارمند با بیشترین حقوق
highest_id = max(employees, key=lambda employee_id: employees[employee_id]['salary'])
print('بیشترین حقوق:', employees[highest_id]['name'])
print('مقدار حقوق:', employees[highest_id]['salary'])

# میانگین حقوق
total_salary = 0

for employee in employees.values():
    total_salary = total_salary + employee['salary']

average_salary = total_salary / len(employees)
print('میانگین حقوق:', average_salary)

# کارمندان با حقوق بیشتر از 3000
print('کارمندان با حقوق بیشتر از 3000:')

for employee in employees.values():
    if employee['salary'] > 3000:
        print(employee['name'])

# کارمند با کمترین حقوق
lowest_id = min(employees, key=lambda employee_id: employees[employee_id]['salary'])
print('کمترین حقوق:', employees[lowest_id]['name'])