'''
1. Clasa Angajat Atribute: nume, prenume, salariu Constructor pentru toate atributele Metode: ● descrie() ● nume_complet()
 ● salariu_lunar() ● salariu_anual() ● marire_salariu(procent)
'''

"""
class Employee:

    def __init__(self, name, first_name, salary):
        self.name = name
        self.first_name = first_name
        self.salary = salary

    def describe(self):
        return f'{self.first_name} {self.name} has {self.salary} .'

    def complete_name(self):
        print(f'My complete name is {self.first_name} {self.name}.')

    def monthly_salary(self):
        pass

    def annual_salary(self, monthly_salary):
        if self.annual_salary == 12 * self.salary is True:
            return self.annual_salary

    def salary_increase(self):
        percent = int(input(f"The percent is : "))
        if percent > 0:
            print(f"The percent is : {percent}")
        else:
            print("The percent is a invalid number!")


employee1 = Employee('George', 'Pop', 3000)
print(employee1.complete_name())
print(employee1.describe())
print(employee1.monthly_salary())
print(employee1.annual_salary("3000"))
print(employee1.salary_increase())
"""

'''
2. Clasa Cont Atribute: iban, titular_cont,
 sold Constructor pentru toate atributele Metode: ● afisare_sold() - Titularul x are în contul y suma de n lei
 ● debitare_cont(suma) ● creditare_cont(suma)
'''

"""
class Cont:

    def __init__(self, iban, titular_cont):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = 500

    def afisare_sold(self, titular_cont, iban, suma):
        print(f"Titularul {titular_cont} are in contul {iban} suma de {suma} lei.")

    def debitare_cont(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma} lei.')
            print(f'Aveti in cont {self.sold} lei.')
        else:
            print('Fonduri insuficiente')

    def creditare_cont(self, suma):
        self.sold += suma
        print(f'Ati alimentat {suma} lei.')
        print(f'Aveti in cont {self.sold} lei.')


cont1 = Cont("Bia B", "RO001")
cont2 = Cont("Flavi B", "RO002")
cont1.afisare_sold("Bia B", "RO001", 500)
cont2.afisare_sold("Flavi B", "RO002", 500)

cont1.debitare_cont(200)
cont2.debitare_cont(100)

cont1.creditare_cont(500)
"""

'''
3. Clasa Factură Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc Constructor: toate atributele, fără serie Metode:
● schimbă_cantitatea(cantitate) ● schimbă_prețul(pret) ● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x număr y Data: generează automat data de azi Produs | cantitate | preț bucată |
Total Telefon | 7 | 700 | 49000
'''

'''
class Factura:

    seria = "FAR001"
    data = 21062023
    telefon = 770049000

    def __init__(self, seria, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
        self.seria = seria
        print(f"Factura cu numarul {numar} : {nume_produs}  {cantitate} - {pret_buc}")

    def schimba_cantitatea(self, cantitatea):
        return cantitatea

    def schimba_pretul(self, pret):
        return pret

    def schimba_nume_produs(self, nume):
        return nume

    def genereaza_factura(self, data="216223"):
        for row in table:
            print(f'| {self.seria} | {self.numar} | {data} | {self.nume_produs} | {self.cantitate} '
                  f'| {self.pret_buc} |'.format(*row))


table = [[]]


factura1 = Factura("FAR001", "001", "Loreal sampon", "24 buc", "15 lei")
print(factura1.seria)
print(factura1.pret_buc)
print(factura1.schimba_cantitatea(25))
factura1.genereaza_factura('21062023')
'''




