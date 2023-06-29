"""
Practica sesiunea 1_2
"""

# definim o variabila string
culoare = 'rosu'
# afisam in consola tipul variabilei culoare
# print(type(culoare)) # <class 'str'>

# definim o variabila int
numar = 20
# print(type(numar))

# definim o variabila float
numar2 = 20.5
# print(type(numar2))

# definim o variabila bool
este_inmatriculata = True
# print(type(este_inmatriculata))

# TYPE CASTING

numar1 = 10
numar2 = '10'

# Sunt numar1 si numar2 de acelasi tip?
# print(type(numar1))
# print(type(numar2))

numar2 = int(numar2)
# print(numar2)
# print(type(numar2))

# my_str = "10euro"
# my_str = int(my_str) # -> da eroare: ValueError
# print(my_str)

# int -> str
numar1 = 10
# print("before", type(numar1))
numar1 = str(numar1) # '10'
# print("after", type(numar1))

# float -> str
numar2 = 25.5
# print("before", type(numar2))
numar2 = str(numar2) # '25.5'
# print("after", type(numar2))

# int -> float
numar3 = 120
numar3 = float(numar3) # -> 120.0
# print(numar3)

# float -> int
numar4 = 30.6
numar4 = int(numar4)
# print(numar4)

my_str = "Ana are mere"
# print(bool(my_str)) # True

my_str2 = ""
# print(bool(my_str2)) # False

my_str3 = None
# print(bool(my_str3)) # False

x = 5
# print(bool(x)) # True

y = 0
# print(bool(y)) # False

z = -5
# print(bool(z))

w = 0.0
# print(bool(w)) # False

a = 1.2
# print(bool(a)) # True

b = 2.0
# print(bool(b)) # True

"""
EX8: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""

# a.
a = 5
# print(a)

# b.
# print(type(a)) # <class 'int'>

# c.
b = float(a)
# print(b) # 5.0

# d.
# print(type(b)) # <class 'float'>

# FUNCTIA INPUT

# input() # apelam functia input fara parametrii
# nume = input("Cum te numesti?")
# print(f"Numele meu este {nume}.")
# print(type(nume))

# varsta = int(input("Care este varsta ta?"))
# print(f"Varsta: {varsta}")
# print(type(varsta))
"""
EX7:
a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
"""

#a
# x = 80
# print(x)
# print(type(x))
#b
# y = 5.12
# print(y)
# print(type(y))
#c
# z = 'gri'
# print(z)
# print(type(z))
#d
# w = True
# print(w)
# print(type(w))
"""
EX9:
a. Defineste o variabila de tip string. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de la punctul a, in int si salveaza rezultatul intr-o noua variabila.
Ruleaza programul.
Ce observi?
"""
#a
# b = '25'
# print('b: ', b)
#b
# print(type(b))
#c
# c = int(b)
# print('c: ', c)


#functia input()
# input('Cum te numesti?')
# nume = input('Cum te numesti?')
# print(f"Numele meu este {nume}.")
# print(type(nume))

# varsta = int(input('Care este varsta ta?'))
# print(f'Varsta : {varsta}')
# print(type(varsta))

"""
EX10: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
# nume_produs = str(input('As dori sa cumpar: '))
# print(f'Am cumparat {nume_produs}.')

# String-urile - metode disp
# Index
# info = 'Afara sunt 2 grade'
# print(info[0]) # => 'A' (primul caracter din string se afla la indexul 0)
# print(info[1]) # => 'f'
# print(info[5]) # => ' ' (la indexul 5 avem un spatiu gol)

"""
EX11: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
# pret = float(input("Ce pret are produsul? "))
# print(f"Pretul produsului este {pret}")

# STRING - caracteristici si metode disponibile


# INDEX
info = 'Afara sunt 2 grade'
# print(info[0]) # => 'A' (primul caracter din string se afla la indexul 0)
# print(info[1]) # => 'f'
# print(info[5]) # => ' ' (la indexul 5 avem un spatiu gol)

# accesam caracterul 'e' de la ultima pozitie din string

# v1 - index pozitiv
# print(info[17])

# v2 - index negativ
# print(info[-1])

# accesam penultimul caracter din string
# print(info[-2])

# LUNGIMEA
# info = 'Afara sunt 2 grade'

# afisam lungimea string-ului info
# print(len(info)) # => 18

# SLICING

info = 'Afara sunt 2 grade'

# Extragem string-ul care incepe cu index-ul 0 pana la index-ul 1, inclusiv
# print(info[0:2]) # => 'Af'

# Extragem string-ul care incepe cu index-ul 0 pana la indexul 4, inclusiv
# print(info[0:5]) # => 'Afara'

# Daca nu specificam end_pos, se va extrage string-ul
# pana la ultimul caracter, inclusiv
# print(info[6:])  # => 'sunt 2 grade'

# Daca nu specificam start_pos, se va extrage string-ul
# incepand cu primul caracter.
# print(info[:5])  # => 'Afara'

# Inversare string
# print(info[::-1]# => 'edarg 2 tnus arafA'

#sa iau elementele din doi in doi
# setand pasul ca fiind 2 print(info[::-1]
# Slicing intr-un string si

cifre = "123456789"
# print(cifre[::2])
# print(cifre[0:5:2])
# print(cifre[:5:2])

"""
EX13: Se da string-ul prop2 = 'Masina e rosie.'
Afiseaza lungimea string-ului prop2.
"""
# prop2 = 'Masina e rosie.'
# print(len(prop2))

"""
EX14: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""

prop3 = 'Concertul va avea loc maine.'
# a.
primul_cuvant = prop3[:9]
# print(primul_cuvant)

# b.
# print(primul_cuvant[0:3])

# c.
# print(prop3[::-1])


# metode ajutatoare string

# str1 = 'bAnAnA'
# print(str1.upper()) # => 'BANANA' (tot cu litere mari)
# print(str1.capitalize())  # => 'Banana'
# print(str1.lower())
# print(str1.count('A'))
# print(str1.count('a'))
# print(str1.count('A', 0, 3))
# print(str1.replace('A', 'a'))
# print(str1.find('A'))
# print(str1.find('x'))

# String-ul este ORDONAT si IMUTABIL

# STRING = ORDONAT -> elementele pot fi accesate dupa index
my_str = "abc"
print(my_str[0])
# STRING = IMUTABIL - > string-ul nu poate fi modificat
my_str = "aabbcc"
result = my_str.replace("a", "x")
print(result)
print(my_str)

# my_str[1] = 'x'
# print(my_str)
my_str = "cde" # suprascriem
print(my_str)

"""
# EX15: Se da string-ul my_str = 'vacanta'.
# a. Foloseste metoda find() pentru a afla primul index la care se gaseste caracterul 'a'.
# b. Foloseste metoda count() pentru a afla de cate ori apare caracterul 'a' in my_str.
# c. Foloseste metoda capitalize() pentru a scrie cuvantul cu prima litera mare.
# d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
# """

#my_str = 'vacanta'
#a
# print(my_str.find('a'))
#b
# print(my_str.count('a'))
#c
# print(my_str.capitalize())
#d
# print(my_str.upper())

"""
EX16: Exploreaza urmatoarele metode ajutatoare ale string-ului:
a. endswith()
b. index()
c. lower()
d. replace()
e. strip()
"""

# my_str = 'Acasa'
#a
# print(my_str.endswith('a'))
#b
# print(my_str.index('c'))
#c
# print(my_str.lower())
#d
# print(my_str.replace('c', 'n'))
#e
# print(my_str.strip('a'))




# OPERATORI

# OPERATORI ARITMETICI

x = 2
y = 3

# # adunarea
# suma = x + y
# print(x + y) # 5
# # # scaderea
# print(y - x) # 1
# # # inmultirea
# print(x * y) # 6
# # # impartirea
# print(y / x) # 1.5
# # # restul impartirii
# print(y % x) # 1
# # # ridicarea la putere
# print(x ** y) # 2 la puterea 3 -> 8
# # # floor division
# print(y // x) # 3 // 2; 1.5 => 1
#
# # inmultirea pe string-uri
# my_str = 'a'
#
# # vreau sa afisez mesajul 'aaa'
# print(my_str + my_str + my_str)
# print(my_str * 3)

# In cazul impartirii, indiferent daca rezultatul
# va fi un numar intreg (adica fara virgula) sau un numar
# zecimal, rezultatul impartirii in Python va fi de tip float

# print(10 / 2) # nu va fi 5, ci va fi 5.0 (mereu va fi float)

# floor division

# 1. floor division intre doua numere intregi
# print(3 // 2) # 1 => numar intreg

# 2. floor division intre doua numere si avem cel putin unul din ele
# ca fiind float
# print(3.0 // 2) # 1.0

# 3. floor division cand rezultatul este negativ (cand un numar din operatia
# floor division este negativ
# print(-3 // 2) # -3 / 2 = -1.5 => -2

"""
EX1: Se dau doua variabile, a = 10, b = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""
# a = 10
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)
# print(a // b)

# Op logici

# x = 2
# print(x<5 and x<10)

# y = 20
# print(y > 1 or y < -5)

# print(not True)
# print(not 10>11)

"""
EX2: Pentru fiecare din exemplele de mai jos, scrie intr-un comentariu
rezultatul asteptat, apoi decomenteaza codul de la fiecare exemplu, pe rand
si ruleaza exemplele si verifica output-ul.
"""

# Exemplul 1:
# a = True
# b = False
# print(not(a))  # False
# print(not(b))  # True

# Exemplul 2:
# a = True
# b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)

# Exemplul 3:
# a = False
# b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)


# x = 2
# print(x < 5 and x < 10) # True and True -> True
# print(x > 6 and x < 10) # False and True -> False
#
# y = 20
# print(y > 1 or y < -5) # True or False - > True
# print(y < 5 or y == 3) # False or False -> False
#
# print(not True) # False
# print(not False) # True
#
# print(not 10 > 11) # True

# Operatori de comparare

# a = 2
# b = 10
# print(a == 2) # True
# print(a != b) # True
# print(a > 5) # False
# print(a < 4) # True
# print(a >= 2) # True

"""
EX3: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
"""
# num = 12
# a
# print(num >= 12 )
#b
# print(num > 5)
# print(num < 25)
#c
# print(num < 0)
# print(num < 20 )


# IF
# x = 10
# if x == 5:
#     print("x este egal cu 5") # indentare cod
#     print("si asta")
# else:
#     print("x nu este egal cu 5")


# if x < 20:
#     print("x este mai mic decat 20")  # indentare cod
# elif x > 20:
#     print("x e mai mare decat 20")
# else:
#     print("x e egal 20.")
# print("final document")

# if...elif...else

"""
EX4: Verifica daca varsta introdusa de utilizator este mai mare
decat 18 ani.
"""
# major = 18
# varsta = int(input('Cati ani ai?'))
# if varsta >= major:
#     print('Felicitari.Poti intra!')

"""
EX5: Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
"""
# pret = int(input('Introduceti pretul'))
# if pret <= 100:
#     print(f'Pretul este: {pret}')

# if...else
# x = 10
# if x == 5:
#     print("x este egal cu 5") # indentare cod
# else:
#     print("x nu este egal cu 5")

# constanta = are o valoare stabila, nu ne dorim sa o schimbe nimeni
# standardul este sa o scriem cu litere mari
# NOTA_DE_TRECERE = 4.5
# nota = float(input('Alege nota'))
# if nota >= NOTA_DE_TRECERE:
#     print(f'Ai luat nota {nota}')
#     print('Felicitari ai trecut examenul')
# else:
#     print(f'Ai luat doar nota {nota}')
#     print('Ne vedem la vara! Ai picat examenul')

"""
EX6:
a. Citeste un numar de la tastatura.
b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
"""
#a
# nr = 10
#b
# if nr % 2 == 0:
#      print('numar par')
# else:
#      print('numar impar')

"""
EX7:
a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
"""

#a
# viteza = 60
#b
# if viteza <= 50:
#     print('Viteza normala')
# c
# else:
#     print('Viteza depasita')

# robotelul telefonic
# optiune = int(input('alege o optiune'))
# if optiune == 0:
#     print('meniul anterior')
# elif optiune == 1:
#     print('ati ales ro')
# elif optiune == 2:
#     print('ati ales eng')
# else:
#     print('Nu am identificat optiunea, mai incearca.')

# x = 25
# if x < 20:
#     print('x este mai mic')
# elif x > 20:
#     print('x este mai mare')
# else:
#     print('x este egal')


# operatori de atribuire
x = 1

# +=
x += 3 # -> x = x + 3 => 1 + 3 => 4
print(x)

x -= 2 # -> x = x - 2 => 4 - 2 => 2
print(x)

"""
EX8: Citeste de la tastatura varsta utilizatorului si afiseaza categoria
de varsta in care se incadreaza.
Tine cont de aceste categorii de varsta:
- intre 0-18 ani: minor
- intre 18-65 ani: adult
- peste 65 ani: senior
"""
# varsta = int(input())
# if varsta < 18:
#     print('Esti minor!')
# elif varsta <= 65:
#     print('Esti adult!')
# else:
#     print('Esti senior!')

"""
EX9: Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
cosul de cumparaturi, in functie de totalul cosului de cumparaturi
Reducerea se aplica in felul urmator:
- Total este intre 100 si 200 lei -> reducere 10%
- Total intre 200 - 300 lei -> reducere 15%
- Total intre 300-400 -> reducere 20 %
- Total mai mare de 400 -> reducere 30 %.
a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
dupa aplicarea reducerii.
"""
#a
# cos_cumparaturi = int(input('Valoare cos cumparaturi:'))
#b
# if cos_cumparaturi < 100:
#     print('Ne pare rau, dar nu beneficiati de reducere!')
# elif cos_cumparaturi <= 200:
#     print('Felicitari! Aveti 10% reducere la cosul de cumparaturi!')
# elif cos_cumparaturi <= 300:
#     print('Felicitari! Aveti 15% reducere la cosul de cumparaturi!')
# elif cos_cumparaturi <=400:
#     print('Felicitari! Aveti 20% reducere la cosul de cumparaturi!')
# else:
#     print('Felicitari! Aveti 30% reducere la cosul de cumparaturi!')

#  Nested if conditions
'''
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
else:
    eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
else:
    go_shopping()
'''

"""
EX10:
a. Citeste de la tastatura nr de ore lucrate de un angajat intr-o saptamana.
b. Tinand cont ca numarul de ore standard de munca dintr-o saptamana este 40,
si se considera overtime, ce e peste 40 de ore, afiseaza bonusul pe care angajatul
il primeste si un mesaj sugestiv, tinand cont de urmatoarele criterii:
- bonusul este de 50 lei daca angajatul a lucrat intre 40 si 50 ore.
- bonusul este de 100 lei daca angajatul a lucrat mai mult de 50 de ore.
- daca s-a lucrat nr de ore standard, angajatul nu e eligibil pentru bonus.
"""
#a
# ore_lucrate = int(input('Ore lucrate:'))
#b
# if ore_lucrate < 41:
#     print('Nu poti beneficia de bonus!')
# elif ore_lucrate < 51:
#     print('Felicitari!Ai un bonus de 50 lei.')
# else:
#     print('Felicitari!Ai un bonus de 100 lei.')

"""
EX11:
a. Citeste de la tastatura varsta utilizatorului.
b. Spune-i utilizatorului daca are drept de vot in Romania.
Ia de la utilizator datele necesare.
criterii:
- utilizatorul are drept de vot daca este mai mare de 18 ani.
- utilizatorul are drept de vot daca locuieste in Romania.
"""
#a
# varsta = int(input('Cati ani ai?'))
# utilizator = str(input('Esti cetatean roman?'))
# raspuns1 = 'da'
# raspuns2 = 'nu'
# b
# if varsta >= 18:
#     print('Poti vota!')
# else:
#     print('Nu ai drept de vot!')
# if utilizator == raspuns1:
#     print('Poti vota!')
# else:
#     print('Nu ai drept de vot!')