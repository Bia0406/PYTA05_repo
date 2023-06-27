# Set
"""
EX8: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""
# my_set = {1, 2, 3, 4}
# a
# my_set.add(5)
# print(my_set)

# b
# my_set.add(6)
# print(my_set)

# c
# my_set.add(1)
# print(my_set)
# 1 exista deja in set, nu se mai adauga pt ca seturile au elemente unice!

# d
# my_set.remove(4)
# print(my_set)

# e
# my_set.pop()
# print(my_set)

# print(type(my_set))
# Tuplu
"""
EX9:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""
# locatie = (44.34, 12.456)
# a
# print(type(locatie))
# b Este ordonata
# print(locatie[0])
# c Este imutabila
# d
# print(len(locatie))
# e
# val2 = locatie[1]
# if val2 > 13:
#     print('Val2 este mai mare decat 13!')
# else:
#     print('Val2 nu este mai mare decat 13!')

# Cicluri repetitive
# While/While else

"""
EX1: Se da numarul x = -5.
Foloseste un while pentru a afisa numerele negative pornind
de la -5.
La final, afiseaza un mesaj ca s-au afisat toate numerele
negative.
"""
# x = -5
# while x <= -1:
#     print('Numar negativ:', x)
#     x += 1

# print('S-au afisat toate numerele negative!')

"""
? EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""

# nota1 = int(input("Introduceti va rog nota 1: "))
# nota2 = int(input("Introduceti va rog nota 2: "))
# nota3 = int(input("Introduceti va rog nota 3: "))
# media_aritmetica = (nota1 + nota2 + nota3) / 3)

# while media_aritmetica < 0 and media_aritmetica == 0:
#     print("Note invalide!")
#     nota1 = int(input("Introduceti va rog nota 1: "))
#     nota2 = int(input("Introduceti va rog nota 2: "))
#     nota3 = int(input("Introduceti va rog nota 3: "))

# print(f"Media aritmetica este : {media_aritmetica}. ")

# For/For else
"""
EX3: Afiseaza toate numerele pare pana la 10.
"""
# v1
# for numar in range(0,11):
#     if numar % 2 == 0:
        # print(numar)
# v2
# for numar in range (0, 10, 2):
#     print(numar)

"""
EX4: Se da lista:
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
Afiseaza toate elementele din lista accesandu-le dupa index.
"""
# legume = ['spanac', 'castraveti', 'conopida', 'ardei']

# for index in range(len(legume)):
#     print(index)
#     print(legume[index])

# For each
"""
?EX5:
2. Se da lista:
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
Sa se afiseze toate produsele care au pretul mai mare de 5 lei.
"""

# produse = [
#     {
#         'nume produs': 'Rosii',
#         'pret': 5
#     },
#     {
#         'nume produs': 'Paine',
#         'pret': 8
#     },
#     {
#         'nume produs': 'Lapte',
#         'pret': 6
#     },
#     {
#         'nume produs': 'Cafea'
#     }
# ]
#
# for pret in produse:
#     print(pret)


# Break
"""
EX6: Sa se afiseze primul numar par din intervalul 1 - 10
(inclusiv capetele de interval).
"""
# for i in range(2,11):
#     if i % 2 == 0:
#         print(i)

"""
EX7:
Se da lista:
participanti = ['Maria', 'Ionela', 'Marius', 'Paul']
Folosind un ciclu repetitiv, cauta daca 'Marius' se afla in lista de participanti.
Dupa ce l-ai gasit intrerupe ciclul repetitiv.
"""
# participanti = ['Maria', 'Ionela', 'Marius', 'Paul']

# for Marius in participanti:
#         print('Marius este in lista!')
#         break

# Continue

"""
EX8: 1. Se da lista:
numere = [1, 2, 3, 4, 5, 6, 7]
Afiseaza toate elementele din lista numere,
cu exceptia numerelor 3 si 5
"""

# numere = [1, 2, 3, 4, 5, 6, 7]

# for numere in range(1, 8):
#     if numere == 3 or numere == 5:
#         continue
#     print(numere)




