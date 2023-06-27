# class Car:
#     fields (attributes)
    # make = 'Dacia'
    # year = 2022
# from Sesiunea_3.Sesiunea3_2.calculator import Calculator

# def __init__(self, model, color):
    #     self.model = model
    #     self.color = color


# car1 = Car('Duster', 'white')
# car2 = Car('Logan', 'blue')

# print(car1.make)
# print(car1.model)
# print(car1.color)


# class Complex:

    # def __init__(self, real, imag):
    #     self.r = real
    #     self.i = imag

# z = Complex(3.0, -4.5)

# calcl = Calculator(a=5, b=2)
# print(calcl.a)
# print(calcl.b)
# print(calcl.adunare())
# print(calcl.scadere())
# print(calcl.inmultire())
# print(calcl.impartire())

# calcl2= Calculator(a=20, b=0)
# print(calcl2.impartire())


"""
EX:
a. Defineste o clasa noua Dog.
b. Obiectele de tip Dog vor avea obligatoriu 2 atribute:
name si age.
c. Creeaza doua obiecte de tip clasa Dog, acceseaza atributele
si afiseaza-le.
d. Schimba atributul nume pentru unul din obiecte
si afiseaza-l din nou.
e. Creaza o metoda description, care returneaza
mesajul '{nume} is {age} years old'.
f. Folosind unul din obiectele instantiate la exercitiul
apeleaza metoda description, salveaza rezultatul
intr-o variabila si afiseaza variabila.
g. Clasa Dog este caracterizata si de atributul rasa.
Adauga acest atribut ca si un atribut al clasei (nu al obiectului)
h. Adauga o noua metoda in clasa Dog, numita speak,
care ia un parametru numit sound.
Metoda trebuie sa returneze mesajul "<name> says <sound>."
i. Apeleaza metoda speak pe unul din obiecte si afiseaza
rezultatul.
"""
from turtle import color


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.color = color
        self.height = height

    def description(self):
        return f'{self.name} is {self.age} years old'


dog1 = Dog('labrador', '3')
dog2 = Dog('chihuahua', '1')


print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

dog2 = Dog('chihuahua', '1')

print(dog2.name, dog2.age)

print(dog1.description())
print(dog2.description())


