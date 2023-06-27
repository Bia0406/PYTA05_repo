"""
1. Explica intr-un comentariu ce este o variabila de tip string.
"""
# Variabila de tip string este o cutiuta in interiorul careia putem scrie orice intre ghilimele.

"""
2. Defineste 3 variabile: oras, strada si nr.
a. Afiseaza aceste variabile intr-o propozitie, folosind concatenarea string-urilor.
b. Afiseaza aceste variabile intr-o propozitie, folosind f-strings.
"""

# oras = 'Arad'
# strada = 'Pelicanului'
# nr = '18'

# print('Locuiesc in ' + oras + ',' + ' pe strada ' + strada + ',' + 'la numarul' + ' ' + nr + '.')
# print(f'Locuiesc in {oras}, pe strada {strada},la numarul {nr}.')

"""
3. Se da variabila string, nume_complet = 'Pop Maria Ioana'.
a. Afiseaza numele de familie din string.
b. Afiseaza al doilea prenume.
c. Afiseaza de cate ori apare litera 'a' in nume_complet.
d. Inverseaza string-ul si afiseaza rezultatul.
e. Inlocuieste al doilea prenume cu 'Elena'.
f. Afiseaza caracterele de la indexul 5 la indexul 9 (inclusiv).
g. Afiseaza caracterele de la inceputul string-ului pana la index-ul 8 (inclusiv).
"""
# nume_complet = 'Pop Maria Ioana'

# print(nume_complet[0:3])
# print(nume_complet[10:15])
# print(nume_complet.count('a'))
# print(nume_complet[::-1])
# print(nume_complet.replace('Ioana', 'Elena'))
# print(nume_complet[5:10])
# print(nume_complet[:9:])

"""
4. Citeste de la tastatura culoarea preferata a utilizatorului si salveaza rezultatul intr-o variabila.
a. Determina lungimea inputului citit de la tastatura.
b. Determina tipul inputului citit de la tastatura.
c. Transforma inputul de la utilizator in text cu litere mari si afiseaza-l.
d. Transforma inputul de la utilizator in text care incepe cu litera mare si restul sunt litere mici.
Afiseaza rezultatul.
"""
# culoare = input("Culoarea mea preferata este : ")
# print(len(culoare))
# print(type(culoare))
# print(culoare.upper())
# print(culoare.capitalize())


"""
5. Se da variabila anotimp = 'primavara'. Verifica daca anotimp se termina in 'vara'.
"""
# anotimp = 'primavara'

# verif = anotimp[-4:]
# print(verif)

"""
6. Citeste de la tastatura pretul cosului de cumparaturi. Afiseaza pretul cu un discount de 25%.
"""

# cos_cumparaturi = int(input("Care este totalul cosului de cumparaturi?"))
# discount = cos_cumparaturi - cos_cumparaturi * 25/100
# print(f"Pretul platit cu discount este : {discount}.")


"""
7. Se da string-ul: zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'.
Transforma string-ul in lista, folosindu-te de o metoda ajutatoare de pe string.
"""
# zile_sapt = 'luni, marti, miercuri, joi, vineri, sambata, duminica'
# print(zile_sapt)
# print(type(zile_sapt))
# list_sapt = zile_sapt.split()
# print(list_sapt)
# print(type(list_sapt))

"""
8. Scrie un program care solicita utilizatorului sa introduca varsta sa
și returneaza un mesaj personalizat, in funcție de varsta introdusa.
Daca varsta este mai mare sau egala cu 18, programul trebuie sa afiseze
mesajul "Esti major si poti vota".
In caz contrar, programul trebuie sa afiseze mesajul "Esti minor si nu poti vota inca".
"""

# varsta = int(input("Introduceti varsta dvs: "))
# if varsta >= 18:
#     print('Esti major si poti vota!')
# else:
#     print('Esti minor si nu poti vota!')


"""
9. Scrie un program care primeste un pret de la tastatura si afiseaza
un mesaj daca prețul este mai mare sau mai mic decât 100 de lei.
"""

# pret = int(input("Introduceti pretul: "))
# if pret > 100:
#     print('Ai primit un voucher de 10 lei deoarece ai depasit suma de 100 lei!')
# else:
#     print('Ai cumparat mai putin de 100 lei. Mai cumpara pentru a beneficia de voucher!')

"""
10. Citeste doua numere intregi de la tastatura. Printeaza produsul dintre cele doua numere
daca acesta este mai mic sau egal decat 1000, altfel printeaza suma lor.
"""
# x = int(input("x = "))
# y = int(input("y = "))
# produs = x * y
# suma = x + y

# if produs <= 1000:
#     print(f'Produsul numerelor este {produs}.')
# else:
#     print(f'Suma numerelor este {suma}.')

"""
11. Se dau doua liste:
lista_1 = [10, 20, 30, 40, 50, 10]
lista_2 = [1, 2, 3, 4, 5]
Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
In functie de rezultat, afiseaza un mesaj.
"""
# lista_1 = [10, 20, 30, 40, 50, 10]
# lista_2 = [1, 2, 3, 4, 5]

# if lista_1[0] == lista_1[-1]:
#     print('Primul si ultimul element sunt egale!')
# else:
#     print('Primul si ultimul element nu sunt egale!')


# if lista_2[0] == lista_2[-1]:
#         print('Primul si ultimul element sunt egale!')
# else:
#     print('Primul element si ultimul nu sunt egale!')

"""
12. Scrie un program care afiseaza de cate ori apare litera 'e' in
stringul str_1 = 'Emma is a sofware developer.'
"""
# str_1 = 'Emma is a sofware developer.'
# print(str_1.count('e'))

"""
13. Scrie un program in care citesti de la tastatura doua nr intregi,
numite base si exponent.
Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
Atentie: indiferent daca utilizatorul a introdus un numar pozitiv sau negativ
ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
hint: exploreaza functia abs() si vezi cum o poti folosi
"""

# base = int(input("Introduceti va rog primul numar: "))
# exponent = int(input("Introduceti va rog al doilea numar: "))

# puterea = base ** abs(exponent)
# print(f"Valoarea numarului {base}, la puterea {exponent} este {puterea}.")

"""
14. Scrie un program in care se citeste de la tastatura un string.
Daca string-ul are numar impar de caractere, afiseaza un string care
contine primul caracter, caracterul din mijloc si ultimul caracter
al string-ului citit de la tastatura.
Daca string-ul are numar par de caractere, afiseaza un string care contine doar primul
si ultimul caracter  al string-ului citit de la tastatura.
"""
# x = input("Introduceti un string: ")

# if len(x) % 2 != 0:
#     caracter1 = x[0]
#     index = int((len(x)-1)/2)
#     caracter2 = x[index]
#     caracter3 = x[-1]
#     print(f'{caracter1}, {caracter2}, {caracter3}')
# else:
#     caracter1 = x[0]
#     caracter3 = x[-1]
#     print(f'{caracter1} ,{caracter3}')


"""
15. Se dau doua variabile:
str1 = 'Abc'
str2 = 'Xyz'
Creeaza o variabila string, str3 formata din:
- primul caracter din str1 cu litera mica
- primul caracter din str2 cu litera mare
- al doilea caracter din str1 cu litera mare
- al doilea caracter din str2 cu litera mare
- al treilea caracter din str1 cu litera mare
- al treilea caracter din str2 cu litera mica
"""
# str1 = 'Abc'
# str2 = 'Xyz'

# str3 = str1.lower()[0] + str2.upper()[0] + str1.upper()[1] + str2.upper()[1] + str1.upper()[2] + str2.lower()[2]
# print(str3)


"""
16. Se da lista:
fruits = ["apple", "banana", "cherry"]
a. Schimba elementul 'apple' cu 'kiwi'.
b. Foloseste metoda append() pentru a adauga elementul 'oranges'.
c. Foloseste metoda insert() pentru a adauga elementul 'lemon' ca al doilea
element din lista.
d. Foloseste metoda remove() pentru a sterge elementul 'banana' din lista.
e. Foloseste un index negativ pentru a accesa ultimul element din lista.
f. Foloseste un index negativ pentru a accesa penultimul element din lista.
g. Afiseaza lungimea listei.
h. Foloseste slicing pe lista, astfel incat sa obtii o lista cu al doilea, al treilea
si al patrulea element.
"""
# fruits = ["apple", "banana", "cherry"]

# fruits.remove('apple')
# fruits.insert(0, 'kiwi')
# print(fruits)

# fruits.append('oranges')
# print(fruits)

# fruits.insert(1, 'lemon')
# print(fruits)

# fruits.remove('banana')
# print(fruits)

# print(fruits[-1])

# print(fruits[-2])

# print(len(fruits))

# print(fruits[1::1])


"""
17. Inverseaza lista my_list = [100, 200, 300, 400].
"""

# my_list = [100, 200, 300, 400]
# print(my_list[::-1])

"""
18. Lista de cumparaturi:
Se citeste de la tastatura o lista de cumparaturi. Utilizatorul introduce
lista de cumparaturi ca un string, cu alimentele separate prin virgula,
ATENTIE: fara spatii
Exemplu:rosii,castraveti,branza,oua
a. Sa se transforme string-ul citit de la tastatura intr-o lista. (vezi metode ajutatoare string).
b. Sorteaza lista de cumparaturi si printeaza lista sortata.
c. Adauga un aliment nou in lista de cumparaturi.
d. Sterge un aliment din lista de cumparaturi.
e. Modifica elementul de la pozitia 0 din lista.
f. Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
Daca nu, afiseaza mesajul "Iti recomandam rosiile de asemenea".
"""

# cumparaturi = str(input('Introduceti lista de cumparaturi : '))
# cumparaturi = cumparaturi.replace(' ', ' ')
# print(cumparaturi)

# lista_cumparaturi = [cumparaturi]
# print(lista_cumparaturi)

# print(lista_cumparaturi.sort())

# aliment1 = str(input("Introduceti un aliment nou : "))
# lista_cumparaturi.append(aliment1)
# print(lista_cumparaturi)

# print(lista_cumparaturi.pop())
# print(lista_cumparaturi)

# lista_cumparaturi.insert(0, "lapte")
# print(lista_cumparaturi)

# if lista_cumparaturi != 'rosii':
#     print("Aliment sanatos!")
# else:
#     print("Iti recomandam rosiile de asemenea!")

"""
19. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
Converteste lista la string si afiseaza string-ul. A se vedea metoda join(). (search on google)
"""

# fructe = ['capsuni', 'mere', 'lamai']

# string = ','
# fructe_convert = string.join(fructe)
# print(fructe_convert)

"""
20. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
Afiseaza elementul cu valoarea maxima din string. (google- functia max())
"""

# numere = [1, 2, 3, 4, 56, 22, 5]
# print(max(numere))

"""
21. Se da lista preturi = [12.3, 34.5, 22].
Calculeaza suma elementelor din lista preturi. (google - functia sum())
"""

# preturi = [12.3, 34.5, 22]
# print(sum(preturi))

"""
22. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza valoarea cheii city.
b. Kelly a fost promovata. Salariul ei este acum de 10000 lei. Fa modificarea si in dictionar.
c. Sterge varsta din dictionar.
d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
"""

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# print(sample_dict['city'])

# sample_dict['salary'] = 10000
# print((sample_dict['salary']))

# del sample_dict['age']
# print(sample_dict)


# sample_dict.update({"employment_date": "4 june 2023"})
# print(sample_dict)

# print(sample_dict.get('country', 0))
# sample_dict['country'] = 'Romania'
# print(sample_dict)

"""
23. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza toate cheile din dictionar. (HINT: metoda keys())
b. Afiseaza toate valorile din dictionar. (HINT: metoda values())
c. Verifica lungimea dictionarului.
"""
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# print(sample_dict.keys())

# print(sample_dict.values())

# print(len(sample_dict))

"""
24. Gasirea unui element intr-un dictionar
Se da dictionarul:
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia cautata.
Verifica daca aceasta se gaseste sau nu in dictionar.
"""

# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }

# cheie = input('Introduceti o cheie: ')
# cheie1 = cheie.replace("", '')
# print(persoana.get(cheie1, 'Cheia cautata nu se gaseste in acest dictionar!'))

"""
25. Adaugarea unui element intr-un dictionar
Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul trebuie sa introduca cheia si valoarea pe care doreste sa
le adauge in dictionar.
Foloseste metoda update() (metoda ajutatoare pe dictionar)
"""

# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }

# cheie = input('Introduceti o cheie: ')
# valoare = input('Introduceti o valoare pentru cheia dvs: ')
# persoana.update({cheie : valoare})
# print(persoana)

"""
26. Stergerea unui element din dictionar
 Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia elementului de eliminat.
a. Elimina elementul, verificand prima data daca cheia se afla in dictionar,
si daca se afla, foloseste metoda del.
b. Elimina elementul, folosind metoda ajutatoare pop().
"""

# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }

# element = input('Introduceti elementul pe care vreti sa-l stergeti : ')
# if persoana.get(element, 0) == 0:
#     print('Elementul acesta nu exista!')
# else:
    # del persoana[element] # varianta pentru punctul a
    # persoana.pop(element) # varianta pentru punctul b
    # print('Element sters cu succes!')
# print(persoana)

"""
27. Concatenarea a doua dictionare.
Se dau doua dictioanare:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
Sa se concateneze cele doua dictionare folosind metoda update().
Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
perechi cheie:valoare in dictionar.
"""
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}

# dict1.update(dict2)
# print(dict1)

"""
28. Se da urmatoarea lista cu dictionare:
lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
a. Adauga perechea {'c':'3'} in primul dictionar din lista.
b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
c. Aduaga un nou dictionar ca element in lista, la indexul 1.
d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
"""
# lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]

# dict1 = lista[0]
# dict1.update({'c':'3'})
# lista[0] = dict1
# print(lista)

# lista.append({'g':'7', 'h': '8'})
# print(lista)

# lista.insert(1, {'i': '9', 'j': '10'})
# print(lista)

# dict2 = lista[1]
# if dict2.get('c', 0) == 0:
#     print('Cheia c nu se gaseste in dictionarul al doilea din lista!')
# else:
#     print('Cheia c se gaseste in dictionarul al doilea din lista!')

"""
29.
Se citeste de la tastatura un numar.
a. Printeaza un mesaj sugestiv daca numarul este par sau nu.
b. Daca numarul este multiplu de 4, afiseaza un mesaj sugestiv.
"""
# numar = int(input('Introduceti un numar: '))

# if numar % 2 == 0:
#     print("Numarul introdus de dvs este par!")
# else:
#     print("Numarul introdus de dvs este impar!")

# if numar % 4 == 0:
#     print("Numarul introdus de dvs este multiplu de 4!")
# else:
#     print("Numarul introdus de dvs nu este multiplu de 4!")

"""
30.
Se citesc de la tastatura doua numere, num si check. Verifica daca
num este divizibil cu check si afiseaza un mesaj corespunzator catre utilizator.
"""

# num = int(input('Introduceti un numar: '))
# check = int(input('Introduceti inca un numar: '))
# if num % check == 0:
#     print(f'{num} este divizibil cu {check}!')
# else:
#     print(f'{num} nu este divizibil cu {check}!')

"""
31. Se da dictionarul:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a. Foloseste metoda get() pentru a printa valoarea cheii 'model'.
b. Schimba valoarea cheii 'year' in 1970.
c. Adauga perechea cheie:valoare 'color':'red' in dictionar.
Adaug-o folosind accesarea dictionarului prin cheie (car['color']) si dand o valoare.
Adaug-o folosind metoda update()
d. Foloseste metoda pop() pentru a sterge 'model' din dictionar.
e. Foloseste metoda empty() pentru a 'goli' dictionarul.
"""

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(car.get('model', ''))

# car['year'] = 1984
# print(car)

# car['color'] ='blue'
# print(car)
# car.update({'color':'white'})
# print(car)

# car.pop('model')
# print(car)

# print(car)
# car.clear()
# print(car)