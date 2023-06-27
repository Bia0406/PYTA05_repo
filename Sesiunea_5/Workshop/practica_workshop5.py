'''
Design Patterns. Iterators, Generators, Decorators
'''
from functools import wraps

'''
1. Singleton
Se da următoarea clasa:


class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent
'''

"""
class PresidentOfRomania:
    instance = None

    def new(cls, args):
        if not hasattr(cls, "instance"):
            cls.instance = super().new(cls, args)
        return cls.instance

    def str(self):
        return "I am Romania's president"

    def say_hello(self):
        return f'Salut! {self}'


a = PresidentOfRomania()
b = PresidentOfRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Same object? {a is b}')
"""

'''
Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea 
de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).

Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba 
(exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language)
 – in functie de parametrul language, returnează un translator object.


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
'''

"""
class FrenchLocalizer:

    def __init__(self):
        self.translations = {
           "car": "voiture",
           "bike": "bicyclette",
           "cycle": "cyclette"
        }

    def localize(self, msg):

        return self.translations.get(msg, msg)


class SpanishLocalizer:

    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }

    def localize(self, msg):

        return self.translations.get(msg, msg)


class EnglishLocalizer:

    def localize(self, msgy):
        return msgy


def factory(language="English"):

    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()


if __name__ == "__main__":

    f = factory("French")
    e = factory("English")
    s = factory("Spanish")

message = ["car", "bike", "cycle"]

for msg in message:
    if f and e and s:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))


# factory = TranslatorFactory()

# english_trans = factory.get_translator('en')
# spanish_trans = factory.get_translator('es')

# print(f'In engleza zicem {english_trans.localize("masina")}')
# print(f'In spaniola zicem {spanish_trans.localize("masina")}')
"""

'''
3. Generators
Implementați un generator pentru loteria 6/49 și noroc:
-Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
-Ultima apelare va da un singur număr de “noroc” format din 7 cifre.
'''
"""
import random


def generator():
    total = 0
    while total < 6:
        yield random.randint(1, 49)
        total += 1


def noroc_generator():
    yield random.randint(10, 60)

    
lottery_num = tuple(generator())
noroc_num = tuple(noroc_generator())
print("loteria 6/49")
print(lottery_num)

print("noroc num")
print(noroc_num)

"""

'''
4. Context Managers
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind 
urmatoarele 2 metode:
-try - finally 
Fișierul se deschide înainte de try, folosind functia open
În interiorul try citim conținutul folosind functia read
În finally se închide fișierul
-with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context managerul face asta 
pentru noi.
'''

"""
class File(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


try:
    with File('hello.txt', 'r') as file_name:
        print(file_name.read())
finally:
    print(file_name.close())

"""
'''
5. Decorators
Implementați următorii decoratori:
-timeit – decorator care măsoară timpul de execuție al unei funcții 
-logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
'''

"""
import time


def new_decorator(original_func):

    def wrapper():
        t1 = time.time()
        result = time.time()
        t2 = time.time() - t1
        print(f"{original_func.__name__} a fost executata in {t2} secunde.")
        return result

    return wrapper()


@new_decorator
def timeit(original_func):
    return result


@new_decorator
def logger(name, model):
    print(f" a rulat cu parametrii {name}, {model}")

"""

'''
6. Decorators extra
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nașterii 
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind 
un decorator `@require_login` 
– o metoda logout, fara params, care delogheaza userul.
Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
'''

'''
class User:

    def __init__(self, name, email, password, birthdate):
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate


def require_login(User):

    def login(self, email, password):
        self.email = email
        self.password = password
        self.email = input("Introduceti emailul dvs: ")
        self.password = input("Introduceti parola dvs: ")
        if self.password == len('******'):
            print("Logare reusita!")
        else:
            print('Parola sau user gresit! Incercati din nou: ')
            self.email = input("Introduceti emailul dvs: ")
            self.password = input("Introduceti parola dvs: ")


@require_login
def get_info(self, name, email, password, birthdate):
    if self.password == len("******"):
        print( f"Detalii user: {self.name}\n {self.email} \n {self.password} \n {self.birthdate} ")


def logout():
    pass


for details in get_info():
    if require_login is True:
        print(details)
    elif logout is True:
        print(details)
    else:
        print(details)


user1 = User("Maria", "maria@gmail.com", "mariamaria", "18 may 1990")
print(user1.email)
print(user1.password)
print(user1.name)
print(user1.birthdate)

'''
