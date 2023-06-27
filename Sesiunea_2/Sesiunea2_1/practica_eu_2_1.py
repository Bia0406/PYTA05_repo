# Liste
"""
EX1:
a. Defineste o lista cu 3 elemente.
b. Este lista o structura de date ordonata? De ce da/nu?
c. Acceseaza al doilea element din lista si afiseaza-l.
d. Afiseaza lungimea listei.
"""
# a
# lista = [1, 2, 3]
# b Da,este ordonata,se poate accesa dupa index.
# c
# print(lista[1])
# d
# print(len(lista))


"""
EX2:
a. Defineste o lista numita filme_preferate, cu cel putin 3 elemente.
b. Inverseaza lista folosind slicing. (ca la string)
c. Folosind if, verifica daca lista este goala sau nu,
si afiseaza un mesaj corespunzator pentru fiecare situatie.
"""

# a
# filme_preferate = ['Titanic', 'The Chosen', 'Patimile lui Isus']
# b
# print(filme_preferate[::-1])
# c
# lista1 = type(filme_preferate)
# if filme_preferate == lista1:
#     print('Lista este goala!')
# else:
#     print('Lista nu este goala!')

"""
EX3: Se da structura de date cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8].
a. Verifica tipul structurii de date dat.
b. Accesand metodele de pe lista, sorteaza lista cifre.
c. Verifica daca 9 este in lista cifre. Afiseaza un mesaj corespunzator.
"""

# cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
# a
# print(type(cifre))
# b
# cifre[1] = 1
# cifre[2] = 2
# cifre[3] = 3
# cifre[4] = 4
# cifre[5] = 5
# cifre[6] = 6
# print(cifre)
# c
# print(cifre[9]) => error

"""
EX4: Exploreaza metodele ajutatoare ale listelor.
"""
# cifre.append(9)
# print(cifre)
# cifre.insert(10, 15)
# print(cifre)
# cifre.pop()
# print(cifre)
# cifre.remove(0)
# print(cifre)
# cifre[0] = 0
# print(cifre)
# print(len(cifre))

# Dictionare

"""
EX5: 
a. Defineste un dictionar, numit student1, cu urmatoarele chei:
nume, prenume, varsta, an_studiu, facultate, medie. 
Valorile le alegi tu.
b. Afiseaza lungimea dictionarului.
c. Printeaza prenumele studentului.
d. Adauga o noua pereche cheie-valoare, cu tara in care studiaza studentul.
e. Verifica daca dictionarul contine cheia oras.
"""
# a
# student1 = {
#     'nume': 'Popa',
#     'prenume': 'Maria',
#     'varsta': 22,
#     'an_studiu': 3,
#     'facultate': 'Vasile Goldis',
#     'medie': 9.70
# }
# print(student1)
# b

# print(len(student1))
# c

# print(student1['nume'])
# print(student1['prenume'])
# d

# student1.update({'tara': 'Romania'})
# print(student1)

# e
# print(student1.get('oras', False))

"""
EX6:
a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume,
ingrediente, timp prepapare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""

# a
# reteta = {'nume': 'Dobos', 'ingrediente': 'faina,lapte,unt,ciocolata,oua', 'timp preparare': '120 min'}
# print(reteta)

# b

# reteta = {
#     'nume': 'Dobos',
#     'ingrediente': 'faina,lapte,unt,ciocolta,oua',
#     'timp preparare': '120 min'
# }
# print(reteta)

# c Nu se poate modifica!

"""
EX7:
a. Se da un dictionar cu contacte din agenda telefonica:
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
b. Aurel si-a schimbat numarul de telefon. Actualizeaza-l.
c. Ai obtinut numarul de telefon a lui Mihai. Adauga-l in contacte.
d. Maria a plecat in strainatate si nu mai are numar de telefon. Sterge-l.
e. Verifica daca ai numarul Mihaelei si afiseaza un mesaj corespunzator.
"""

# a

# contacte = {
#     'Maria': '0722898956',
#     'Aurel': '0755342298'
# }
# print(contacte)
#
# b

# contacte.update({'Aurel': '0728528528'})
# print(contacte)

# c
# v1
# contacte.update({'Mihai': '0755238238'})
# print(contacte)
# v2
# contacte['Mihai'] = '0755238238'
# print(contacte)

# d

# del contacte['Maria']
# print(contacte)

# e

# print(contacte.get('Mihaela', False))


