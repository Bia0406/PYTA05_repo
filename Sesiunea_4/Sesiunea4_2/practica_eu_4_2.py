# class CarPy:
#
#     def __init__(self, color):
#         self.__color = color
#
##     @property
#     def color(self):
#         return self.__color
#
#     @color.getter
#     def color(self):
#         print(f"Getter: Culoarea este {self.__color}")
#         if self.__color is not None:
#             return  self.__color.upper()
#         return ("nu avem culoare")
#     @color.setter
#     def color(self, culoare_noua):
#         print(f"Setter: Noua culoare este {culoare_noua}")
#         self.__color = culoare_noua

#     @color.deleter
#     def color(self):
#         print(f"Deleter: Am sters culoarea")
#         self.__color = None
#
#
# car2 = CarPy('gray')
# print(car2.color)
#
# car2.color = 'red'
# print(car2.color)
#
# del car2.color
# print(car2.color)

"""
EX4: ENCAPSULARE
a. Defineste o clasa Produs.
Aceasta va avea in constructor urmatoarele atribute:
- nume
- pret
- discount - atribut privat

b. Defineste proprietatea discount:
- getter
- setter -> inainte de a seta o valoare pentru discount,
asigura-te ca acesta e cuprins intre 0-100.
- deleter
"""

# class Produs:

# def __init__(self, nume, pret, discount):
#     self.nume = nume
#     self.pret = pret
#     self.__discount = discount

# @property
# def discount(self):
#     return self.__discount

# @discount.getter
# def discount(self):
#     print(f"Getter: The discount is {self.__discount}")
#     if self.__discount is not None:
#         print("Getter : We dont't have discount!")

# @discount.setter
# def discount(self, discount_new):
#     print(f"Setter: The new discount is {discount_new}")
#     self.__discount = discount_new

# @discount.deleter
# def discount(self):
#     print(f"Deleter: The discount is delete!")
#     self.__discount = None
#     print()


# disc1 = Produs("mere", 50, 20)
# print(disc1.nume)
# print(disc1.pret)
# print(disc1.discount)

# disc1.discount = 30
# print(disc1.discount)

# del disc1.discount
# print(disc1.discount)

"""
EX5: Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""

from abc import ABC, abstractmethod


class AbstractVideo(ABC):

    @abstractmethod
    def show_detail(self):
        pass

    def show_detail(self):
        return "It is working!"

    def play(self):
        play = True
        if play is True:
            return "Video is playing!"


# game = AbstractVideo()
# print(game.play())
# print(game.show_detail())


"""
EX6: Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""


class Videoclip(AbstractVideo):

    def __init__(self, title, duration):
        super().__init__()
        self.title = title
        self.duration = duration

    def show_detail(self, title, duration):
        super().show_detail()
        print(f"{title} has a duration of {duration} minutes.")


# videoclip1 = Videoclip("The game", 15)
# print(videoclip1.show_detail("The game", 15))


"""
EX7:
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""


class Movie(Videoclip):

    def __init__(self, title, duration, genre="", director="", actors=[]):
        super().__init__(title, duration)
        self.genre = genre
        self.__director = director
        self.actors = actors

    def show_detail(self, title, duration, director, actors):
        super().show_detail(title, duration)
        return f'Is directed by {director} and the actors are {actors}.'

    @property
    def director(self):
        return self.__director

    @director.getter
    def director(self):
        print(f"Getter: Director is {self.__director}")

    @director.setter
    def director(self):
        print(f"Getter: Director is {self.__director}")
        if self.__director is not True:
            return self.__director.upper()
            return "We dont't have director"

    @director.deleter
    def director(self):
        print(f"Deleter: The director is delete!")
        self.__director = None
        print()


# movie1 = Movie("Harry Potter", "180")
# print(movie1.show_detail("Harry Potter", "180", "Harry", "Harry, Margaret and Jon"))

mov2 = Movie("Harry Potter", "180", "Harry", "Harry, Margaret and Jon")
print(mov2.show_detail("Harry Potter", "180", "Harry", "Harry, Margaret and Jon"))
print(mov2.director)



