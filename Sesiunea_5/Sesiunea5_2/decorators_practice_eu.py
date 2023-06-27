# Decoratori

# @property
# @abstractmethod

def new_decorator(original_func):
    def wrapper_func():
        print("Niste cod inaintea apelului original_func")
        original_func()
        print("Niste cod dupa apelul original_func")

    return wrapper_func


@new_decorator
def func_needs_decoration():
    print("Vreau sa fiu decorata")


@new_decorator
def hello():
    print("Hello Pythonistas!")


@new_decorator
def greet():
    print("Greetings to you")


func_needs_decoration()
hello()
greet()


# Daca aplicam decoratorul pe functia de mai jos, va functiona?

# @new_decorator # => eroare
# def salut(name):
#     print(f"Salut, {name}")

# salut("Ana")

# ex 2 cu parametri

def decorator_salut(original_func):
    def wrapper_func(*args, **kwargs):
        print(f"Am intrat in functia {original_func.__name__}")

        original_func(*args, **kwargs)

        print(f"Am iesit din functia {original_func.__name__}")

    return wrapper_func


@decorator_salut
def salut(name):
    print(f"Salut, {name}")


salut("Ana")


