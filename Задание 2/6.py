# -- coding: utf-8 --

x1 = int(input("Номер строки первой клетки:"))
y1 = int(input("Номер столбца первой клетки:"))
x2 = int(input("Номер строки второй клетки:"))
y2= int(input("Номер столбца второй клетки:"))
if (x1 + y1 + x2+y2) % 2 == 0:
    print('Да')
else:
    print('Нет')