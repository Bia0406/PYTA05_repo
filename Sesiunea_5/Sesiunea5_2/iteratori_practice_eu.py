# lst = ['a', 'b', 'c']
# for x in lst:
#     print(x)
    # avem 3 iteratii: x = 'a', x = 'b', x = 'c'

# ITERABIL

# Cum ne dam seama daca un obiect este iterabil sau nu/ Cum ne dam seama daca putem folosi cicluri repetitive pe un obiect?
# Trebuie ca obiectul respectiv sa aiba disponibila metoda __iter__()

# nums = [1, 2, 3]
# print(nums.__iter__()) # <list_iterator object at 0x0000020E13F6AC20>
# SAU
# nums = [1, 2, 3]
# i_nums = iter(nums)

# ITERATORII

# Tehnic vorbind, un obiect iterator Python trebuie sa implementeze doua metode speciale,
# __iter__() și __next__(), numite colectiv protocol iterator.

# nums = [1, 2, 3]

# i_nums = iter(nums)
# print(i_nums)
# print(iter(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums)) # StopIteration error

# Implementarea for loop-ului este de fapt:

# create an iterator object from that iterable
# iter_obj = iter(iterable)

# infinite loop
# while True:
#     try:
        # get the next item
        # element = next(iter_obj)
    # except StopIteration:
    #     if StopIteration is raised, break from loop
    #     break

"""
EX1: Implementeaza o clasa care sa fie atat iterabila cat si un iterator
si sa aiba acelasi comportament ca si functia range din Python.
"""

# range(1, 5)
# range(3, 6)

# for x in range(1, 5):
#     print(x)

# print("--------------------")

# for x in range(3, 6):
#     print(x)


# for x in MyRangeClass(1, 5):
#     print(x)

# for x in MyRangeClass(3, 6):
#     print(x)


# class MyRangeClass:

    # def __init__(self, start, end):
    #     self.value = start
    #     self.end = end

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if self.value >= self.end:
    #         raise StopIteration
    #     current_value = self.value
    #     self.value += 1
    #     return current_value


# nums = MyRangeClass(1, 10)
# for num in nums:
#     print(num)

# for number in MyRangeClass(1, 4):
#     print(number)


# Generatori

# def my_gen():
#     n = 1
#     print('This is printed first')

    # Generator function contains yield statements
    # yield n

    # n += 1
    # print("This is printed second")
    # yield n

    # n += 1
    # print('This is printed at last')
    # yield n

# v2
# for number in my_gen():
#     print(number)

# v1
# generator = my_gen()
# print(next(generator))
# print(next(generator))
# print(next(generator))


"""
EX2: Creeaza un generator care face acelasi lucru ca si clasa MyRange
implementata la exercitiul anterior.
"""


# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1


# for number in my_range(1, 4):
#     print(number)


"""
EX3: Implementeaza un generator de numere pare care ne va da acces la toate
numerele pare pana la un numar maxim luat ca si parametru.
"""


# def my_range_num(start, end):
#     par = start
#     while par < end:
#         yield par
#         par += 2


# for number in my_range_num(2, 100):
#     print(number)

"""
EX4: Implementeaza un generator de puteri ale unui numar.
Va lua doi parametri: numarul ce va fi ridicat la putere, si
un numar care va reprezenta puterea maxima pana la care primul
parametru va fi ridicat.
"""


# def gen_putere(start, end):
#     num = start
#     while num < end:
#         yield num
#         num *= 2


# for number in gen_putere(2, 257):
#     print(number)
