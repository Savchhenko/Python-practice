piramide = []
step = 0
symbol = str('##')

number_of_steps = int(input('Введите количество ступеней в пирамиде? - '))

while step < number_of_steps:
    piramide.append(symbol[0])
    print(symbol.rjust(number_of_steps))
    step = step + 1
    symbol = symbol + '#'
