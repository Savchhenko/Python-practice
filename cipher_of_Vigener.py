import re #reuglar expressions
A = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
a = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
sentence = str(input("Enter your text for encryption: "))
k = str(input("Enter a code word:"))
code = ""
j = 0
for i in sentence :
    if re.search(r"[А-Я]", i) or re.search(r"[а-я]", i):
        if i in a:
            index = (a.index(i) + a.index(k[j])) % 33
            code += a[index]
        else:
            index = (A.index(i) + a.index(k[j])) % 33
            code += A[index]
        if j == len(k) - 1:
            j = 0
        else:
            j += 1
    else:
        code += i

print(code)
