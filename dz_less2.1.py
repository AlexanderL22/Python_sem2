# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
atr = int(input('Введите число для перевода в шестнадцатеричное представление: '))

SYSTEM_16 = 16
SPR = {0: '0', 1: '1',
       2: '2', 3: '3',
       4: '4', 5: '5',
       6: '6', 7: '7',
       8: '8', 9: '9',
       10: 'A', 11: 'B',
       12: 'C', 13: 'D',
       14: 'E', 15: 'F', }

print(hex(atr))

decstr = ''

while atr > 0:
    rem = atr % SYSTEM_16
    decstr = decstr + SPR[rem]
    atr = atr // SYSTEM_16
print(decstr[::-1])