print("What language will you use?")
print("Enter 1 if English or 2 if Russian: ")
lang = int(input())
k = int(input("Enter key for encryption:"))
sentence = input("Enter your text for encryption:")
code = ""
if lang == 1:
    A_e = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz" #26*2 English alphabet
    for i in sentence:
        if i in A_e:
            code += A_e[(A_e.index(i) + k*2)%52] #Output  of the encrypted symbol
        else:
            code += i #Output of the symbol
if lang == 2:
    A_r = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя" #33*2 Russian alphabet
    for i in sentence:
        if i in A_r:
            code += A_r[(A_r.index(i) + k*2)%66]
        else:
            code += i
print(code)

