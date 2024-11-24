print('Введите первое число: ', end=' ')
first = input()
print('Введите второе число: ', end=' ')
second = input()
print('Введите третье число: ', end=' ')
third = input()
print('Количество одинаковых чисел: ', end=' ')
if first == second and second == third:
    print(3, end=' ')
elif first == second or first == third or second == third:
    print(2, end=' ')
else: print(0, end=' ')