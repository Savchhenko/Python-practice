
print("Введите число:")
number_minutes = int(input()) #Вводим число минут,проведенных в душе

y = int(12) #Число бутылок с водой за 1 минуту
n = number_minutes * y  #Считаем число бутылок

print("В продолжении {0} минут вы расходуете воду в количестве {1} бутылок 0,5л".format(number_minutes, n))



