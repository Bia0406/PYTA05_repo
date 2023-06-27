'''
1.Funcție care să calculeze și să returneze suma a două numere
'''

# def add_number(a,b):
#     result = a + b
#     print(f'Suma : {result}')

# def sum(a,b):
#     return a+b
# add_number(a = 5, b= 35)

# print(f'Suma returnata este : {sum(15, 35)}')

'''
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
'''
# def numar(n):
#     if n % 2 == 0:
#         return True
#     return False

# print(f'Paritatea : {numar(1000)}')
# print(f'Imparitatea : {numar(1001)}')
'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
# def nume(nume, prenume, nume_mijociu = ' '):
#     if type(nume) == str and type(prenume) == str and type(nume_mijociu) == str:
#         return len(nume+prenume+nume_mijociu)
#     return  -1

# print(f'Lungimea numelui complet este {nume("Bia", "Bad")} caractere.')

# if nume(10, 20, 30) > 0:
#     print(f'Lungimea numelui complet este {nume(10, 20, 30)} caractere.')
# else:
#     print('Introduceti parametrii de tip string')

'''
4. Funcție care returnează aria dreptunghiului
'''


# def aria_dreptunghi(a, b):

    # result = (a*2)+(b*2)
    # print(f'Aria dreptunghiului este {result}.')


# aria_dreptunghi(a=5, b=3)


'''
5. Funcție care returnează aria cercului
'''


# def aria_cerc(pi, R):

    # return pi * R ** 2


# print(f'Aria cercului este {aria_cerc(pi=5, R=5)}.')

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
'''

# def char_finder(expectancy, x):
#     if expectancy.find(x) > 0:
#         return True
#     else:
#         return False


# print(f'Acest caracter se gaseste in {char_finder('Ana are mere.', 'r')}')


'''
7. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''


# def item_count(my_list):
#     dicti = {
#         "0": 0,
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0,
#         "6": 0,
#         "7": 0,
#         "8": 0,
#         "9": 0
#     }
#     for item in dicti.keys():
#         dicti[item] = my_list.count(int(item))

    # return dicti


# print(f'Dictionar {item_count([0, 1, 2, 5, 2 ,7, 8, 9,5])}')

'''
8. Clasa Dreptunghi Atribute: lungime, lățime, culoare Constructor pentru toate atributele Metode: ● descrie() ● aria()
 ● perimetrul() ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă 
 culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
'''


# class Right:
#
#     length = 5
#     width = 15
#     color = 'green'
#
#     def __init__(self, l, w, c):
#         self.length = l
#         self.width = w
#         self.color = c
#
#     def describle(self):
#         print(f'This right has a  length of {self.length} and one width of {self.width}. His color is {self.color}.')
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# right = Right(5, 15, 'pink')
# right.change_color('yellow')
# print(f'The area of right is {right.area()}.')
# right.describle()
# print(f'The perimeter is {right.perimeter()}.')
