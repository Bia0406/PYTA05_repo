""""
Practica sesiunea 2_1
"""

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


#
# descriere_masina = "Masina aleasa costa 20 000 euro si se poate achita in rate!”.
# descriere_masina = “Masina aleasa costa 20 000 euro si se poate achita in rate!"
#
# print(descriere_masina[:5])
# print(descriere_masina[-5:])
#
# my_str = "abcde"
# print(my_str.isnumeric()) # False
#
# my_str = "1234"
# print(my_str.isnumeric()) # True
#
# a = 1
# a += 1 # 1 + 1 = 2
# a *= 2 # 2 * 2 = 4
# a = a * 2 # 4 * 2 = 8
# print(a)
#
# str1 = "minge"
# str2 = "rosie"
# print(str1+str2)

# # LISTE
# # Exemplu de lista ordonata de numere intregi
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# # Output: [1, 2, 3, 4, 5]
#
# # Lista este ORDONATA
# # Fiecare element din lista poate fi accesat dupa index
# print(numbers[0]) # accesarea primului element din lista -> 1
# print(numbers[2]) # 3
# print(numbers[-1]) # 5
#
# print(numbers[::-1]) # inversarea unei liste
#
# # Lista este MUTABILA
# # Putem sa modificam, sa stergem si sa adaugam elemente intr-o lista
#
# cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
# print(cifre)
# # adaugam cifra 9 in lista cifre la finalul listei
# cifre.append(9)
# print(cifre)
#
# # adaugam 9 in lista cifre la indexul 2
# cifre.insert(2, 9)
# print(cifre)
#
# # stergem ultimul element din lista
# cifre.pop()
# print(cifre)
#
# # stergem elementul de la indexul 1 in lista cifre
# element_sters = cifre.pop(1)
# print(element_sters)
# print(cifre)
#
# # stergem prima aparitie a unui element in lista
# # dupa valoare
# cifre.remove(3)
# print(cifre)
#
# # cifre.remove(6) # -> ValueError
#
# caractere = ["a", "b", "a", "b", "c", "a"]
# print(caractere)
# caractere.remove("a")
# print(caractere)
# caractere.remove("a")
# print(caractere)
# caractere.remove("a")
# print(caractere)
#
# # actualizam valoarea unui element
# cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
# cifre[1] = 5
# print(cifre)
#
# print(type(cifre)) # <class 'list'>

# DICTIONARE

my_dict = {
    'nume_produs': 'produs_1',
    'pret': 23.00,
    'in_stoc': False
}

# my_dict = {'nume_produs': 'produs_1', 'pret': 23.00, 'in_stoc': False}

# print(my_dict)

contacte = ["0722345567", "0784553344", "0745332211"]

contacte = {
    'Ana': "0722345567",
    'Marius': '0784553344',
    'Maria': '0745332211'
}

contacte = [
    {
        'nume': 'Popa',
        'prenume': 'Ana',
        'nr_telefon': '0722345567',
        'adresa' : 'Strada Mihai Eminescu, 46',
        'adresa_mail': 'ana@popa.com',
        'varsta': 25,
        'are_masina': False
    }
]

# Dictionarul este NEORDONAT => elementele din dictionar nu
# sunt pastrate in memorie in ordinea in care au fost adaugate
# + NU putem sa accesam elementele dintr-un dictionar dupa index

# Dictionarul este MUTABIL => elementele din dictionar
# pot sa fie modificare, adaugate, sterse

contacte = {
    'Ana': '0722345678',
    'Marius': '0721549888',
    'Maria': '0765332967'
}

# dorim sa accesam numarul lui Marius
# accesam o valoare din dictionar furnizand cheia
# asociata cu acea valoare
# print(contacte['Marius'])

# dorim sa accesam numarul lui Alin
# dorim sa accesam valoarea aferenta cheii Alin
# -> DEZAVANTAJ: daca cheia nu exista in dictionar,
# si folosim aceasta sintaxa => obtinem eroare
# print(contacte['Alin']) # -> eroare: KeyError
# print("here")

# pentru a nu avea eroare in cazul in care
# cheia nu exista in dictionar,
# ne folosim de metoda ajutatoare get
# Metoda get ia ca si parametri:
# - primul parametru: cheia pentru care dorim sa ii aflam/returnam valoarea
# - al doilea parametru: spunem ce vrem sa se returneze daca nu s-a gasit cheia furnizata in dictinar
# print(contacte.get('Alin', "Nu am gasit numarul de telefon cerut"))


#
#
#
# Cate perechi cheie-valoare/elemente avem intr-un dictionar?
# print(len(contacte))

# Dictionarele sunt MUTABILE -> ca putem sa adaugam, modificam,
# stergem elemente din dictionar


person = {
    "name": "John",
    "age": 30,
    "city": ["New York", "Los Angeles"],
    "occupation": "teacher",
}

# ADAUGAREA unui element nou in dictionar
# v1
person['salary'] = 3000.00
# print(person)

# v2
person.update({"has_car": True}) # cream perechea cheie-valoare
# print(person)
person.update({"has_car": False}) # actualizam perechea cheie-valoare
# print(person)

person.update({
    "eyes_color": "green",
    "email": "john@gmail.com"
})

# print(person)

# MODIFICAREA unui element in dictionar
# v1
person['age'] = 31
# print(person)

# v2
person.update({"age": 32})
# print(person)

# STERGEREA unui element din dictionar
# v1
del person['city']
if person.get("city", False):
    del person["city"]
del person['salary'] # stergem mai multe key:value deodata
# print(person)

# v2
# stergerea unui perechi cheie:valoare dupa cheie
person.pop("name")
# print(person)
