print("Enter price of things: ")
price = int(input())
print("Enter your money: ")
money = int(input())
s = money - price #change
print("Your change: ", s)
fifty = 0
ten = 0
five = 0
one = 0
while s != 0:
    if s - 50 >= 0:
        fifty = fifty + 1
        s = s - 50
    elif s - 10 >= 0:
        ten = ten + 1
        s = s - 10
    elif s - 5 >= 0:
        five = five + 1
        s = s - 5
    elif s - 1 >= 0:
        one = one + 1
        s = s - 1
print(fifty, " fifty coins ", ten, " ten coins ", five, " five coins ", one, " one coins")

