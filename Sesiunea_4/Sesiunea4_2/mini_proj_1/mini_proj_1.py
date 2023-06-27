from abc import ABC, abstractmethod


class IMasina(ABC):
    @abstractmethod
    def descrie(self):
        pass

    @abstractmethod
    def inmatriculare(self, nr_inmatriculare):
        pass

    @abstractmethod
    def vopseste(self, culoare):
        pass

    @abstractmethod
    def accelereaza(self, viteza):
        pass

    @abstractmethod
    def franeaza(self):
        pass


class Masina(IMasina):

    MARCA = "Dacia"
    CULORI_DISPONIBILE = {"negru", "rosu", "galben", "albastru"}

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.__culoare = "GRI"
        self.__inmatriculata = False
        self.__nr_inmatriculare = None

    def descrie(self):
        print(f"Marca: {self.MARCA}", f"Modelul : {self.model}", f"Viteza maxima : {self.viteza_maxima}")
        print(f"Viteza actuala : {self.viteza_actuala}", f"Culoare : {self.__culoare}")
        print(f"Inmatriculata : {self.__inmatriculata}", f"Nr inmatriculata : {self.__nr_inmatriculare}")

    def inmatriculare(self, nr_inmatriculare):
        self.__nr_inmatriculare = nr_inmatriculare
        self.__inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.CULORI_DISPONIBILE:
            self.__culoare = culoare
        else:
            print("Culoarea nu este disponibila")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("Viteza nu poate fi o valoare negativa")
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0


    @property
    def culoare(self):
        print(f"Getter culoare")
        return self.__culoare

    @property
    def inmatriculata(self):
        print("Getter inmatriculata")
        return self.__inmatriculata

    @property
    def nr_inmatriculata(self):
        print("Getter nr_inmatriculare")
        return self.__nr_inmatriculare


masina1 =Masina("1300", 100)
masina1.descrie()
masina1.inmatriculare("B80SGS")
masina1.descrie()
masina1.vopseste("roz")
masina1.descrie()
print(masina1.culoare)
print(masina1.viteza_actuala)
masina1.accelereaza(-1)
print(masina1.viteza_actuala)
masina1.accelereaza(200)
print(masina1.viteza_actuala)
masina1.accelereaza(60)
print(masina1.viteza_actuala)
masina1.franeaza()
print(masina1.viteza_actuala)

