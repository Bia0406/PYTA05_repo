"""
OOP - advance
Exerciții - studiu în workshopul de weekend
"""


# def calculeaza_suma(a, b):
#     return a + b


# print(calculeaza_suma(1, 2))


# def calculeaza_suma2(a, b):
#     suma = a + b
#     return suma
#     print(suma)


# print(calculeaza_suma2(1, 2))

# suma_calculata = calculeaza_suma2(1, 2)
# print(suma_calculata)


'''
1. ABSTRACTION Clasa abstractă FormaGeometrica
Conține un field PI=3.14 Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
'''
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')

'''
2.INHERITANCE Clasa Pătrat - moștenește FormaGeometrica constructor pentru latură
'''


class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura = latura

    def aria(self):
        pass

    @property
    def latura(self):
        print('Getter')
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        print('Setter')
        self.__latura = latura_noua

    @latura.deleter
    def latura(self):
        print('Am sters latura')
        self.__latura = 0

# patrat1 = Patrat(5)
# print(patrat1.latura)
# patrat1.latura = 8
# print(patrat1.latura)
# del patrat1.latura
# print(patrat1.latura)

'''
3. ENCAPSULATION latura este proprietate privată Implementează getter, setter, deleter pentru latură 
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica constructor pentru rază, raza este proprietate privată 
Implementează getter,setter, deleter pentru rază Implementează metoda cerută de interfață - 
în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.__raza * self.PI

    def descrie(self):
        print('Eu nu am colturi')

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, new_raza):
        self.__raza = new_raza

    @raza.deleter
    def raza(self):
        self.__raza = 0


# cerc1 = Cerc(5)
# print(cerc1.aria())
# print(cerc1.raza)

# cerc1.raza = 7

# print(cerc1.raza)
# print(cerc1.aria())
# cerc1.descrie()

# del cerc1.raza
# print(cerc1.raza)

'''
4. POLYMORPHISM Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Pătrat și joacă-te cu metodele lui Creează un obiect de tip Cerc și joacă-te cu metodele lui3.
'''
# patrat2 = Patrat(4)
# print(patrat2.aria())
# patrat2.descrie()
# print(patrat2.PI)

# cerc2 = Cerc(3)
# cerc2.descrie()
# print(cerc2.aria())

