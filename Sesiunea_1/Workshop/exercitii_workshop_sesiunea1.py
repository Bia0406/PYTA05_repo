"""
Partea 1 - Setup,variabile,tipuri de date
Exercitii - studiu in workshopul de weekend
"""

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

# Variabila - este o zona de memorie care tine date, o cutiuta in care punem valori.

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# string, int, float, bool.

# string
# masina = 'Mercedes'
# int
# pret = 5000
# float
# discount = 500.60
# bool
# nota = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

# print(type(masina))
# print(type(pret))
# print(type(discount))
# print(type(nota))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere).
# Verifică tipul acesteia.

# print(round(discount))
# discount = 501.00
# print(type(discount))

# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile. Rezolvă nepotrivirile de tip
# prin ce modalitate dorești.

# print(f'Culoarea gri este pentru {masina}.')
# print(f'Produsul acesta costa {pret} euro.')
# print(f'Automobilul aceasta are o reducere de {discount} euro.')
# print(f'{nota} confirma admiterea la facultate.')

# 6. Citește de la tastatură: - numele;
#                            - prenumele.
# Afișează: 'Numele complet are x caractere'.

# numele = str(input("Introduceti numele dvs: "))
# prenumele = str(input("Introduceti prenumele dvs: "))
# nume_complet = prenumele + ' ' + numele
# caractere_nume = len(nume_complet)
# print(f'{nume_complet} are {caractere_nume} caractere.')

# 7. Citește de la tastatură: - lungimea;
#                            - lățimea.
# Afișează: 'Aria dreptunghiului este x'.

# lungimea = int(input('Lungimea dreptunghiului: '))
# latimea = int(input('Latimea dreptunghiului: '))
# x = (lungimea * latimea)
# print(f'Aria dreptunghiului este {x}.')

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock': - afișează de câte ori apare cuvântul
# 'the';

prop = 'Coral is either the stupidest animal or the smartest rock.'
# print(prop.count(' the '))

# 9. Același string: ● Afișează de câte ori apare cuvântul 'the';
#                   ● Printează rezultatul.

# print(prop.count(' the '))
# print(prop.replace(' the ', ' '))

# 10. Același string: ● Folosește un assert ca să verifici dacă acest string conține doar numere.

# print(prop.isnumeric())

# 11. Exercițiu: - citește de la tastatură un string de dimensiune impară;
#               - afișează caracterul din mijloc.

# string_impar = 'orhidee'
# print(string_impar[3])

# 12. Folosind o singură linie de cod : - citește un string de la tastatură (ex: 'alabala portocala');
#                           - salvează fiecare cuvânt într-o variabilă; - printează ambele variabile pentru verificare.

# nume, prenume = input('Numele si prenumele meu este :').split()
# print(nume, prenume)

# 13. Exercițiu:- citește un string de la tastatură (ex: alabala portocala);
#               - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
#            - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

# x = input('Tasteaza un string format din minim 2 cuvinte: ')
# y = x[0]
# z = x.replace(y, y.upper())
# w = x[0]+z[1:-1:] + x[-1]
# print(w)

# 14. Exercițiu: - citește un user de la tastatură;
#               - citește o parolă; - afișează: 'Parola pt user x este ***** și are x caractere';
#               - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#               eg: parola abc => *** parola abcd => ****

# user = input("Numele meu este : ")
# parola = input("Parola este : ")
# parola_caractere = len(parola)
# print(f'Parola pentru user {user} este {parola} si are {parola_caractere} caractere.')

# 15. Exercitiu: Folosind o singura linie de cod , defineste 2 variabile , de tip int,cu valoarea 10.
# # math_grade, english_grade = 10, 10
# # print(math_grade)
# # print(english_grade)
# # print('Nota la matematica:', math_grade)
# # print('Nota la engleza:', english_grade)
"""
Partea 2 - Operatori, conditionale
Exercitii - studiu in workshopul de weekend

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe. 
X este un int.

"""

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

# If else functioneaza in felul urmator: daca variabila indeplineste prima conditie, se afiseaza in consola mesajul dorit,
# dar daca nu indeplineste prima conditie prin else putem sa-i dam alta varianta si afisam un alt mesaj.

# 2. Verifică și afișează dacă x este număr natural sau nu.

# x = int(input("Introduceti un numar: "))
# if x >= 0:
#     print('X este un numar natural.')
# else:
#     print('X nu este un numar natural.')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

# if x < 0:
#     print('X este un numar negativ.')
# elif x == 0:
#     print('X este un numar neutru.')
# else:
#     print('X este un numar pozitiv.')

# 4. Verifică și afișează dacă x este între -2 și 13.


# if x >= -2 and x <= 13:
#     print('X este cuprins intre -2 si 13.')
# else:
#     print('X nu este cuprins intre -2 si 13.')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

# y = 10
# if x-y < 5:
#     print('Diferenta dintre x si y este mai mica decat 5!')
# else:
#     print('Diferenta dintre x si y este mai mare decat 5!')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

# if not x <= 5 and x > 27 :
#     print('X nu este intre 5 si 27.')
# else:
#     print('X este cuprins intre 5 si 27.')

# 7. x și y (int)
#    Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

# if x > y and y < x:
#     print('x este mai mare decat y.')
# elif x < y and y > x:
#     print('y este mai mare dacat x.')
# else:
#     print('x este egal cu y.')

# 8. X, y, z - laturile unui triunghi.
#    Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

# x = 5
# y = 6
# z = 5
# if x == y == z:
#     print('Triunghiul este echilateral.')
# elif x == y or y == z or x == z:
#     print('Triunghiul este isoscel.')
# else:
#     print('Triunghiul este oarecare.')

# 9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu.

# vocale = "a", "e", "i", "o", "u", "ă", "â", "î"
# litera = input("Introdu o litera : ")
# for vocala in vocale:
#     if litera == vocala:
#         print('Este o vocala!')
#         break
# else:
#     print('Nu este o vocala, este o consoana!')

# 10. Transformă și printează notele din sistem românesc în :
#     Peste 9 => A; Peste 8 => B; Peste 7 => C; Peste 6 => D; Peste 4 => E; 4 sau sub => F.

# nota = int(input("Tasteaza nota : "))
# if nota >= 9:
#     print('Ai luat nota A!')
# elif nota >= 8:
#     print('Ai luat nota B!')
# elif nota >= 7:
#     print('Ai luat nota C!')
# elif nota >= 6:
#     print('Ai luat nota D!')
# elif nota >= 4:
#     print('Ai luat nota E!')
# else:
#     print('Ai luat nota F!')

# 11. Verifică dacă x are minim 4 cifre (x e int). (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

# x = int(input("Introduceti un numar: "))
# if x <= 9999 and x >= 1000:
#     print(f'{x} are 4 cifre!')
# else:
#     print(f'{x} nu are minim 4 cifre.')

# 12. Verifică dacă x are exact 6 cifre.

# x = input("Introduceti un numar : ")

# if len(x) == 6:
#     print(f'{x} are {len(x)} cifre')
# else:
#     print(f'{x} are {len(x)} cifre')

# 13. Verifică dacă x este număr par sau impar (x e int)

# x = int(input("Introduceti un numar: "))
# if x % 2 == 0:
#     print(f'{x} este un numar par.')
# else:
#     print(f'{x} este un numar impar.')

# 14. x, y, z (int) Afișează care este cel mai mare dintre ele?

# x = 8
# y = 7
# z = 9
# if x > y and x > z:
#     print(f'{x} este mai mare ca {y} si {z}!')
# elif y > x and y > z:
#     print(f'{y} este mai mare decat {x} si {z}!')
# else:
#     print(f'{z} este mai mare decat {x} si {y}!')

# 15. X, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.
# x = 65
# y = 75
# z = 40
# if x + y + z == 180:
#     print('Triunghiul este valid!')
# else:
#     print('Triunghiul este invalid!')

# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
#                      ● Citește de la tastatură un int x
#                      ● Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

string = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input("Introdu un nr: "))
# print(string[:-x:])

# 17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.

# string_nou = string[:5:]+string[-5::]
# print(string_nou)

# 18. Același string. ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock
#     (hint: este o funcție care te ajuta sa faci asta)
#     ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
#     ( output: 'Coral is either the stupidest animal or the smartest')

# string_v = 'Coral is either the stupidest animal or the smartest rock'
# print(string_v.index('rock'))
# print(string_v[0:-4])

# 19. Joc ghicit zarul Caută pe net și vezi cum se generează un număr random Ne imaginăm ca dai cu zarul și salvăm
# acest număr în dice_roll Ia numărul ghicit de la utilizator Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y. ● Ai pierdut.
# Ai ales un numar mai mare. Ai ales x dar a fost y. ● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

# import random
# dice_roll = random.randint(0, 20)
# number_guessed = None
# while number_guessed != dice_roll:
#     number_guessed = int(input('Ghiceste un numar intre 0 si 20 \n '))
#     if number_guessed < dice_roll:
#         print(f'Ai pierdut.Ai ales un numar mai mic.Ai ales {number_guessed}, dar a fost {dice_roll}!')
#     elif number_guessed > dice_roll:
#         print(f'Ai pierdut.Ai ales un numar mai mare.Ai ales {number_guessed}, dar a fost {dice_roll}!')
#     else:
#         print(f'Ai ghicit.Felicitari!Ai ales {number_guessed} si zarul a fost {dice_roll}!')

# 20. Citește de la tastatură un string Verifică dacă primul și ultimul caracter sunt la fel.
#     Se va folosi un assert Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

# a = input("Introdu un sir de caractere: ")
# b = a[0]
# c = a[-1]
# assert 'b == c'
# print(a)

# 21. Având stringul '0123456789' ● Afișează doar numerele pare ● Afișează doar numerele impare
#     (hint: folosește slicing, controlează din pas)

# cifre = '0123456789'
# print(cifre[::2])
# print(cifre[1::2])


