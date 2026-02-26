from datetime import date, datetime

today = date.today()
date_of_birth_input = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
try:
    date_of_birth = datetime.strptime(date_of_birth_input, '%d.%m.%Y').date()
except ValueError:
    exit('Дата рождения введена некорректна')
if date_of_birth > today:
    exit('Дата рождения не может быть в будущем')
days_passed = today - date_of_birth
print(f'Количество дней, прошедших со дня рождения до сегодняшнего дня: {days_passed.days}')
