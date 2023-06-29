"""
Practica sesiunea 5_2  - Context managers
"""

# interactiunea cu fisierele
# f = open('my_first_file.txt', 'r')
# print(f.read())
# f.close()

# Ce se intampla daca apar erori inainte sa inchidem fisierul?
# f = open('my_first_file.txt', 'r')
# if aaaaaa:
#     print("doing something")
# f.close()
# apare o eroare in codul nostru inainte sa se ajunga
# la inchiderea fisierului -> fisierul NU va fi inchis
# niciodata
# -> consumam resurse + raman datele vulnerabile/expuse!

# Cum putem sa imbuntatim codul de mai sus?

# VARIANTA 1:
# - ne folosim de blocul try except + finally
# f = open('my_first_file.txt', 'r')
# try:
#     print(f.read())
#     if aaaaa:
#         print("doing something")
# except Exception:
#     print("avem o exceptie")
# finally:
#     print("la final inchidem fisierul orice ar fi")
#     f.close()

# VARIANTA 2 the way to do
# folosirea de CONTEXT MANAGERS -> with statement

with open('my_first_file.txt', 'r') as f:
    # variabila f reprezinta rezultatul expresiei apelate in blocul with
    # si este disponibila in interiorul blocului with
    print("suntem in blocul with")
    print(f.read())
print("suntem in afara blocului with")
# print(f.read()) # -> EROARE, in momentul cand am iesit din blocul
# with, fisierul nu mai e deschis!


class File:

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with File('my_first_file.txt', 'r') as file:
    print(file.read())

print("here")

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

