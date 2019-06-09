
dict = {
    "Zuse": "Plankalkul", "Hopper": "COBOL", "Hickej": "Clojure", "Hyde": "Assembly", "Wall": "Perl", "Thompson": "C", "Turner": "SASL", "Stroustrup": "C++", "Syme": "F#", "Ritchie": ["C", "B", "BCPL", "FORTRAN"], "Pestov": "Factor", "Papert": "Logo", "Ousterhout": ["Tcl", "Tk"], "Oliveira": ["boo", "Bamboo"], "Nygaard": "simula", "Naur": "Algol", "Moore": "Fort", "Meyer": "Eiffel", "Merrill": "FOCAL", "McCarthy": "Lisp", "Matsumoto": "Ruby", "Luckham": "Lisp", "Lerdorf": "PHP", "Kernighan": "C", "Kemeny": "BASIC", "Iverson": "APL", "Ierusalimschy": "Lua", "Hui": "J", "Hejlsberg": ["Turbo Pascal", "Delphi"], "Griswold": ["SNOBOL", "SL5", "Icon"], "Graham": "Lisp", "Gosling": "Java", "Farber": "SNOBOL", "Dahl": "Simula", "Cox": "Objective-C", "Colmerauer": "Prolog", "Chambers J.": ["S", "R"], "Chambers C.": "Self", "Bright": ["C++", "D"], "Booth": "Assembler", "Backus": "FORTRAN", "Ashkenas": ["JavaScript", "CoffeeScript", "LiveScript"], "Armstrong": "Erlang"
}  # dictionary of programming languages creators

print("Enter 1 if you want to search by сreator name\nor\nEnter 2 if you want to sort the dictionary:\n ")
choice = int(input()) #operation selection variable

#searching by name
if choice == 1:
    while(1):
        print("Enter name of creator: ")
        name_cr = str(input())
        if name_cr in dict:
            print(name_cr, ":", dict[name_cr])
            print("------------------------------------")
            print("Do you want to continue? 1 -yes, 2 - no\n")
            k = int(input())
            if k == 2:
                break
        else:
            print("Try again")

#sorting
if choice == 2:
    sort = list(dict.keys())
    for i in sorted(sort):
        print(i, ":", dict[i])







