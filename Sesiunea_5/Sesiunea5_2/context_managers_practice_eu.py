# Context Manager

# interactiunea cu fisierele
# f = open("my_first_file.txt", "r")
# print(f.read())
# f.close()

# daca apar erori inainte sa inchidem fisierul
# f = open("my_first_file.txt", "r")
# if aaa:
#     print("doing something")
# f.close()
# apare o eroare in codul nostru inainte sa se ajunga la inchiderea fisierului
# fisierul nu va fi inchis niciodata si astfel face datele raman vulnerabile

# Cum putem imbunatati blocul de mai sus?
# v1 - try except + finally
# f = open("my_first_file.txt", "r")
# try:
#     print(f.read())
#     if aaaa:
#         print("doing something")
# except Exception:
#     print('avem o exceptie')
# finally:
#     print('la final inchidem fisierul orice ar fi')
#     f.close()


# v2 - the way to do - folosirea de context managers : with statment

# with open("my_first_file.txt", "r") as f:
# variabila f reprezinta rezultatul expresiei apelata in blocul with
# print('suntem in blocul with')
# print(f.read())
# print('suntem in afara blocului with')
# print(f.read()) #=> rezulta eroare, fisierul este inchis automat

# exemplu
# class File:
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)

# def __enter__(self):
#     return self.file_obj

# def __exit__(self, type ,value, traceback):
#     self.file_obj.close()


# with File('my_first_file.txt', 'r') as file:
#     print(file.read())


"""
EX5: Implementeaza un context manager care va masura si va afisa
durata de executie a codului executat.
"""


class Timer(object):

    def __init__(self, timer_name, method):
        self.timer_obj = open(timer_name, method)

    def __enter__(self):
        return self.timer_obj

    def __exit__(self, type ,value, traceback):
        self.timer_obj.close()


with Timer('my_first_file.txt', 'w') as file:
    print(file.write("Time executed: "))


