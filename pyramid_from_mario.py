step = 0
symbol = str('##')

number_of_steps = int(input('Enter the number of steps in the pyramid? - ')) #the height of the pyramid

if number_of_steps > 23:
    print("Enter a number that is less than 23: ")
    number_of_steps = int(input())
elif number_of_steps < 1:
    print("Enter a number that is greater than 0: ")
    number_of_steps = int(input())

while step < number_of_steps:
    print(symbol.rjust(number_of_steps))
    step = step + 1
    symbol = symbol + '#'

