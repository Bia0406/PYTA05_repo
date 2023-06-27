

# my_list = [5, 10, 15, 25]
# print(my_list[-2::-2])

"""
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""
# from Sesiunea_3.Sesiunea3_1.func import multiply

# for number in range(1, 11):
#     print(number)

# def get_number():
#     for number in range(1, 11):
#         print(number)
# get_number()

"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""

# def par_impar(lista):
#     for num in lista:
#         if isinstance(num, int):
#             if num % 2 == 0:
#                 print(num, 'Este par')
#             else:
#                 print(num, 'Este impar')
#         else:
#             print('Elementul', num ,'nu este un numar intreg.')

# par_impar([1,2,3,4,5, 'string'])


"""
EX3: Scrie o functie care calculeaza patratul unui numar.
Afiseaza rezultatul.
"""


# def number(x):
#     result = x * x
#     print(f'Patratul nr: {number}')


# number(5)


"""
EX4: Scrie o functie care calculeaza inmultirea dintre doua numere.
Afiseaza rezultatul.
"""


# def add_numbers(x, y):
#     result = x * y
#     print(f'Inmultirea : {result}')


# add_numbers(x=5, y=10)


"""
EX5: Scrie o functie care calculeaza inmultirea dintre doua numere.
Afiseaza rezultatul.
"""


# def inmultire_num(x, y):
#     result = x*y
#     print(f'Inmultire : {result}')


# inmultire_num(x=5, y=10)

"""
EX6: Rescrie functia de la exercitiul 3, 
astfel incat sa returneze rezultatul.
"""

#
# def square(number):
#     return number * number


# print(square(5))

"""
EX7: Rescrie functia de la exercitiul 4, 
astfel incat sa returneze rezultatul.
"""


# def add_numbers(x, y):
#     return x*y


# print(add_numbers(3, 5))


"""
EX8: Scrie o functie care ia ca parametru un numar intreg
si returneaza True daca numarul e par
si False daca numarul e impar.
"""


# def nr_par(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False


# b = nr_par(4)
# print(b)


# print(multiply(2, 4))






