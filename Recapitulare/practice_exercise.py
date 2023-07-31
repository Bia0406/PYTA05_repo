"""
Exercitii recapitulative
"""

"""
1. Creeaza o functie Python care inversează și returnează un număr întreg pozitiv. În cazul unui număr negativ, afișează o eroare.
Exemple: 
reverse(1234567) => 7654321
reverse(10) => 1 
reverse(101) => 101 
reverse(10000000) => 1 
reverse(-65) => eroare
"""


# def reverse(n):
#     if n >= 0:
#         a = str(n)
#         b = a[::-1]
#         c = int(b)
#         return c
#     else:
#         raise ValueError("Numarul nu este pozitiv!")


# print(reverse(1234567))
# print(reverse(-65))

"""
2. Creaza o functie Python care primește o lista și un număr întreg pozitiv k, si roteste lista cu k pozitii. 
Exemple: 
rotate([1, 2, 3, 4, 5], 1) => [2, 3, 4, 5, 1]
rotate([1, 2, 3, 4, 5], 2) => [3, 4, 5, 1, 2]
rotate([1, 2, 3, 4, 5], 4) => [5, 1, 2, 3, 4]
rotate([1, 2, 3, 4, 5], 3) => [4, 5, 1, 2, 3]
rotate([1, 2, 3, 4, 5], 8) => [4, 5, 1, 2, 3]
rotate([1, 2, 3, 4, 5], 5) => [1, 2, 3, 4, 5]
rotate([1, 2, 3, 4, 5], 6) => [2, 3, 4, 5, 1]
rotate([1, 2, 3, 4, 5], 7) => [3, 4, 5, 1, 2]
"""

# v1
# def rotate(lista, k):
#     k = k % len(lista)
#     lista2 = lista[k:] + lista[0:k]
#     print(lista2)
#
#
# rotate([1, 2, 3, 4, 5], 8)

# v2
# from collections import deque
#
#
# def rot(lista,k):
#     deque_list = deque(lista)
#     deque_list.rotate(-k)
#     return list(deque_list)
#
#
# print(rot([1, 2, 3, 4, 5], 8))

"""
3. Creaza o functie Python care primește 2 stringuri, și verifica dacă acestea sunt anagrame (case-insensitive). 
Exemple: 
is_anagram(‘Adela’, ‘ealad’) => True 
is_anagram(‘ITFactory’, ‘acfiorty’) => True 
is_anagram(‘Stringy’, ‘gringsty’) => False 
is_anagram(‘ana’, ‘ioana’) => False
"""

# def is_anagram(str1, str2):
#     if sorted(str1.upper()) == sorted(str2.upper()):
#         print("Sunt anagrams.")
#     else:
#         print("The strings aren't anagrams.")
#
#
# str1 = input("string1 =  ")
# str2 = input("string2 = ")
# is_anagram(str1, str2)

"""
4. Creaza o functie Python care primeste o lista de numere, si il returneaza pe al doilea cel mai mare numar distinct. 
Exemple: 
get_second_biggest([1,2,3,4,5]) => 4 
get_second_biggest([1,2,3,4,4]) => 3 
get_second_biggest([1,2,4,4,4]) => 2 
get_second_biggest([-1,-2,-3,-4,-5]) => -2
"""

#
# def get_second_biggest(number):
#
#     x = 0
#     y = min(number)
#
#     for i in range(len(number)):
#         if number[i] > y:
#             x = y
#             y = number[i]
#         else:
#             x = max(x, number[i])
#
#     return x
#
#
# print(get_second_biggest([1, 2, 3, 4, 5]))
# print(get_second_biggest([-1, -2, -3, -4, -5]))


"""
5. Creaza o functie Python care primeste doua stringuri ce reprezinta niste numere foarte mari, si returneaza rezultatul 
adunarii “numerelor”, tot sub format string:
Exemple: 
add_two(‘12345’, ‘12345’) => ‘24690’ 
add_two(‘1234’, ‘4321’) => ‘5555’ 
add_two(‘563895634’, ‘548967348053’) => ‘549531243687’
"""

#
# def add_two(str1, str2):
#
#     result = ""
#     for i in str1, str2:
#         result += i
#     return result
#
#
# print(add_two('12345', '12345'))

"""
6. Creaza o functie Python care primeste un numar n, si o lista de numere de dimensiune n-1. In lista se afla toate numerele 
de la 1 la n, in afara de 1. Functia trebuie sa gaseasca acel numar in cel mai eficient mod posibil si sa-l returneze. 
Exemple: 
find_missing(5, [1,2,3,5]) => 4 
find_missing(2, [1]) => 2 
find_missing(7, [6,5,1,3,2,7]) => 4
"""


# def find_missing(n, *karg):
#     n = [n-1]
#     for i in range(1, 8):
#         print([i])
#
#
# print(find_missing(5, [1, 2, 3, 5]))


"""
7. Creaza o clasa Calendar, care primeste ca unic parametru un an, si genereaza “calendarul” acelui an. Se va tine cont de 
faptul daca anul este bisect sau nu. Metode: -> init(an) -> print_calendar(luna) - va printa calendarul pentru luna menționată
intr-un format user-friendly, 
ex October 2022
Mo Tu We Th Fr Sa Su 
               1  2 
3  4  5  6  7  8  9
10 11 12 13 14 15 16 
17 18 19 20 21 22 23 
24 25 26 27 28 29 30 
31
-> get_day_of_week(zi, luna) - va returna ce zi din saptamna este, exemplu ‘Marti’ 
-> get_days_in_month(luna) - va returna numarul de zile din luna respectivă;
"""
import calendar

year = 2023
month = 7


class Calendar:

    def __init__(self, year):
        self.firstweekday = None
        self.month = None
        self.day = None
        self.year = year

    def get_day_of_week(self, day, month, firstweekday):
        self.day = day
        self.month = month
        self.firstweekday = firstweekday

    obj = calendar.Calendar(firstweekday=0)

    for day in obj.iterweekdays():
        print(day)

    def get_days_in_month(self,month):
        pass


print(calendar.month(year, month))
print(calendar.calendar(year))
