"""
1. Scrie un program care afiseaza primii 7 multiplii
a lui 7.
HINT: for loop + if + break
Expected Output: 0 7 14 21 28 35 42 49
"""
# v1
# result = ''
# for numar in range(0, 8):
#     x = 7 * numar
#     result += str(x)
#     result += ' '
#     print(result)

# v2
# res1 = ""
# y = 0
# for i in range(1, 1000):
#     if y == 7:
#         break
#     if i % 7 == 0:
#         res1 += str(i) + ' '
#         y += 1
#         print(res1)

"""
2. Scrie o functie care adauga patratul fiecarui numar
intr-o noua lista si afiseaz-o.

Aceasta functie va primi ca parametru o lista.

Example input: [2, 3, 4]
Expected output: [4, 9, 16]
"""


# def my_function(a, b, c):
#     for i in range(2, 5):
#         if i ** 2 != 0:
#             result = i ** 2
#             print([result])
#         else:
#             print("Nu se poate afisa!")


# my_function(a=2, b=3, c=4)

"""
3. Scrie o functie care primeste ca paremtru o lista
de numere intregi.

Separa numerele pozitive de cele negative si returneaza-le.

Apeleaza functia cu diferite argumente si afiseaza rezultatul
conform exemplului de mai jos:

Example input: [1, 2, 5, -2, 3, -5]
Expected output:
Positive: [1, 2, 5, 3]
Negative: [-2, -5]
"""


# def numbers(numere_intregi = []):
#     if numere_intregi > 0:
#         print(f"Numerele pozitive sunt: {numere_pozitive}")
#     else:
#         print(f"Numerele negative sunt: {numere_negative}")


# numere_pozitive = []
# numere_negative = []

# numbers([2, 3, 4, 5, -6, -7, -8, -9])
# numbers(numere_pozitive)
# numbers(numere_negative)


"""
4. Scrie o functie care calculeaza factorialul unui numar natural
pozitiv luat ca si parametru si returneaza rezultatul.

Example input: 6
Expected output: 720
"""
