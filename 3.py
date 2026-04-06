import os

file_name = input('Введите путь к файлу: ')
if not os.path.isfile(file_name):
    exit('Файл не существует')
if os.path.splitext(file_name)[-1] != '.txt':
    exit('Файл должен иметь формат txt')
with open(file_name, encoding='utf-8') as file:
    participants_file = file.readlines()
participants = []
for participant in participants_file:
    line = participant.strip()
    if not line:
        continue
    participant = [x.strip() for x in line.split(',')]
    if len(participant) != 3:
        exit('Некорректный файл')
    try:
        participants += [[participant[0], int(participant[1]), int(participant[2])]]
    except ValueError:
        exit('Некорректный файл')
print('Отсортированный список участников')
print(sorted(participants, key=lambda participant: (participant[2], -participant[1])))
try:
    N = float(input('Введите число: '))
except ValueError:
    exit('Введено не число')
with open('res.txt', 'w', encoding='utf-8') as results:
    for participant in participants:
        if participant[1] > N:
            results.write(','.join([str(x) for x in participant]) + '\n')
