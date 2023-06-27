# # base class / parent class
# class Chef:
#
#     def __init__(self, experience):
#         self.experience = experience
#
#     def make_salad(self):
#         print("salad")
#
#     def make_fries(self):
#         print("fries")
#
#
# # child class - mosteneste din clasa Chef
# # se trece intre paranteze numele clasei parinte
# class JapaneseChef(Chef):
#
#     def make_sushi(self):
#         print("sushi")
#
#
# # child class - mosteneeste din clasa Chef
# # se trece intre paranteze numele clasei parinte
# class ItalianChef(Chef):
#
#     def make_pizza(self):
#         print("pizza")
#
#
# chef1 = Chef(2)
# chef1.make_salad()
# chef1.make_fries()
# print(chef1.experience)
#
# chef2 = JapaneseChef(15)
# chef2.make_sushi()
#
# chef2.make_salad()
# chef2.make_fries()
# print(chef2.experience)
#
# chef3 = ItalianChef(23)
# chef3.make_pizza()
#
# chef3.make_salad()
# print(chef3.experience)
#
# chef3.make_fries()
#
#
"""
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
 Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""

# class Person:

# def __init__(self, name, age):
#     self.name = name
#     self.age = age

# def describe(self):
#     print(f'Persoana {self.name} are {self.age} ani.')


# class Empoyee(Person):
#     def __init__(self, name, age, salary, post):
#         super().__init__(name, age)
#         self.salary = salary
#         self.post = post

# def afiseaza_salariu(self):
#     return self.salary

# def describe(self):
#     (super).describe()
#     print(f'Salariu este {self.salary} pentru postul de {self.post}.')

# pers1 =Person('Vasile', '20')
# print(pers1.name)
# print(pers1.age)
# pers1.describe()


# emp1 =Empoyee('Ion', '38', 'sarac', 'tehnician')
# print(emp1.name)
# print(emp1.age)
# print(emp1.salary)
# print(emp1.post)

# emp1.describe()
# print(f'{emp1.name} has the salary {emp1.salary}.')


"""
EX2: POLIMORFISM

a. Defineste o clasa Pasare care implementeaza metoda 
zboara.
In metoda zboara, afiseaza mesajul 'Majoritatea pasarilor
pot zbura.'

b. Defineste o clasa Strut, care mosteneste din clasa 
Pasare.
Defineste metoda zboara, si afiseaza mesajul 
'Strutii nu pot zbura."
(Nu extindem metoda din clasa de baza, 
ci o suprascriem -> OVERRIDING)

c. Defineste clasa Rata, care mosteneste din clasa Pasare.
Defineste metoda zboara, si afiseaza mesajul 
"Ratele pot zbura."

d. Instantiaza cele 3 clase si apeleaza metoda zboara
pe fiecare obiect.
POLIMORFISM => aceeasi metoda (acelasi nume) -> 
comportament diferit.
"""


class Pasare:

    def fly(self):
        print("Majoritatea pasarilor pot zbura!")


class Strut(Pasare):

    def fly(self):
        print("Strutii nu pot zbura!")


class Rata(Pasare):

    def fly(self):
        print("Ratele pot zbura!")


pasare1 = Pasare
pasare1.fly(Pasare)

strut1 = Strut
strut1.fly(Strut)

rata1 = Rata
rata1.fly(Rata)

"""
EX3: ABSTRACTIZARE
a. Defineste interfata Car. Aceasta va avea o metoda
abstracta numita car_model.

b. Defineste clasele Tesla si BMW, care implementeaza
interfata Car.
Metoda car_model trebuie sa afiseze un mesaj legat
de modelul masinii.

Instantiaza clasele Tesla si BMW si invoca metoda 
car_model pe fiecare din acestea.
"""
# from abc import ABC, abstractmethod


# class Car(ABC):

    # @abstractmethod
    # def car_model(self):
    #     pass


# class Tesla(Car):

    # def car_model(self):
    #     print('This car is comfortable.')


# class Bmw(Car):

    # def car_model(self):
    #     print('This car is super!')


# tesla = Tesla()
# tesla.car_model()

# bmw = Bmw()
# bmw.car_model()
