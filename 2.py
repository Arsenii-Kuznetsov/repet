try:
    N = int(input('Введите натуральное число N: '))
except ValueError:
    exit('Введено не натуральное число')
if N < 1:
    exit('Введено не натуральное число')
print('Последовательность')
print(N, end='')
peak_sequence, number = N, 1
while N != 1:
    print(' -> ', end='')
    if N % 2 == 0:
        N //= 2
    else:
        N *= 3
        N += 1
        peak_sequence = max(peak_sequence, N)
    print(N, end='')
    number += 1
print()
print(f'Количество элементов в последовательности: {number}, пик последовательности: {peak_sequence}')
