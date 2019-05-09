piramide = []
step = 0
symbol = str('##')

number_of_steps = int(input('Введите количество ступеней в пирамиде? - ')) #Высота пирамиды

if number_of_steps > 23:
    print("Введите число, которое меньше 23: ")
    number_of_steps = int(input())
elif number_of_steps < 1:
    print("Введите число, которое больше 0: ")
    number_of_steps = int(input())

while step < number_of_steps:
    piramide.append(symbol[0])
    print(symbol.rjust(number_of_steps))
    step = step + 1
    symbol = symbol + '#'
