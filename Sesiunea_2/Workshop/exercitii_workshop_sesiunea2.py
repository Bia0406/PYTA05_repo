"""
Partea 1 - Structuri de date
Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe. X este un int.
"""

"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do ● Afișeaz-o. 
● Inversează ordinea folosind slicing și suprascrie această listă. ● Printează varianta actuală (inversată). 
● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. 
Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi 
într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. 
Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.
"""
# note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# print(note_muzicale)
# print(note_muzicale[::-1])
# note_muzicale_1 = note_muzicale[::-1]
# print(note_muzicale_1)

# def reverse_list(note_muzicale_1):
#     left = 0
#     right = len(note_muzicale_1) - 1

#     while left < right:
#         tamp = note_muzicale_1[left]
#         note_muzicale_1[left] = note_muzicale_1[right]
#         note_muzicale_1[right] = tamp
#         left += 1
#         right -= 1

    # return note_muzicale_1

# print(reverse_list(note_muzicale_1))


"""
 2. De câte ori apare ‘do’?
"""
# print(note_muzicale.count('do'))

"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4] Găsește 2 variante să le unești într-o singură listă.
"""

# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]

#v1
# list3 = list1 + list2
# print(list3)

#v2
# list1.extend(list2)
# print(list1)


"""
4.● Sortează și afișează lista generată la exercițiul anterior. ● Șterge numărul 0 folosind o funcție.
  ● Afișaza iar lista.
"""
# print(list3.sort())
# list3.remove(0)
# print(list3)

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează: ● Lista este goală. ● Lista nu este goală.
"""

# if len(list3) != 0:
#     print("Lista nu este goala!")
# else:
#     print("Lista este goala!")

"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3
"""

# list3.clear()
# print(list3)

'''
7. Copy paste la exercițiul 5. Verifică încă o dată. Acum ar trebui să se afișeze că lista e goală.
'''

# if len(list3) != 0:
#     print("Lista nu este goala!")
# else:
#     print("Lista este goala!")

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5} Folosește o funcție că să afișezi Elevii (cheile)
'''
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# cheie = dict1.keys()
# print(cheie)

'''
9. Printează cei 3 elevi și notele lor Ex: ‘Ana a luat nota {x}’ Doar nota o vei lua folosindu-te de cheie
'''

# for key, value in dict1.items():
#     print(key, ' a luat nota ', value)

'''
10. Dorel a făcut contestație și a primit 6 ● Modifică nota lui Dorel în 6 ● Printează nota după modificare
'''

# dict1.update({'Dorel ': '6'})

# for key, value in dict1.items():
#     print(key, ' a luat nota ', value)

'''
11. Gigel se transferă din clasă ● Căuta o funcție care să îl șteargă ● Vine un coleg nou. Adaugă Ionică, cu nota 9 
● Printează noii elevi
'''
# del dict1['Dorel']
# print(dict1)

# dict1['Ionica'] = 9
# print(dict1)


'''
12. Ne imaginăm o echipă de fotbal pt teren sintetic. 3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători ● Schimbari_efectuate = te joci tu cu valori diferite ● Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție - Efectuează schimbarea - Șterge jucătorul scos din listă 
- Adaugă jucătorul intrat - Afișază a intrat x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren: - Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
- Afișază ‘mai ai z schimbări’ Testează codul cu diferite valori
Google search hint “how to check if item is în list python”
'''

# jucatori = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5']
# schimbari_efectuate = 2
# schimbari_max = 3
# x = input('Jucator intrat: ')
# y = input('Jucator iesit: ')
# z = 3 - schimbari_efectuate

# if x in jucatori and schimbari_efectuate <= 3:
#         print(f'A intrat {x}, a iesit {y} , mai ai {z} schimbari.')
# else:
#         print(f'Nu se poate efectua schimbarea deoarece {x} nu e în teren!')
#         print(f'Mai ai {z} schimbari!')

'''
13. Set zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'} weekend = {'sâmbăta', 'duminică'} 
● Adaugă în zilele_sapt ‘luni’ ● Afișează zile_sapt
'''
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}

# zile_sapt.add('luni') # nu se pot adauga elemente duplicate
# print(zile_sapt)
# zile_sapt.remove('sâmbăta')
# zile_sapt.remove('duminică')
# print(zile_sapt)

'''
14.Folosește un if și verifică dacă: ● Weekend este un subset al zilelor din săptămânii.
 ● Weekend nu este un subset al zilelor din săptămânii.
'''

# if weekend.issubset(zile_sapt):
#         print('Weekend este un subset al zilelor săptămânii.')
# else:
#         print('Weekend nu este un subset al zilelor săptămânii.')

'''
15. Afișează diferențele dintre aceste 2 seturi.
'''

# print(len(weekend))
# print(len(zile_sapt))

# dif_set = zile_sapt.difference(weekend)
# print(dif_set)


'''
16. Afișează intersecția elementelor din aceste 2 seturi.
'''
# elemente_set = zile_sapt.intersection(weekend)
# print(elemente_set)

"""
Partea 2 - Cicluri repetitive 
Exerciții - studiu în workshopul de weekend
"""

'''
1.Având lista: mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi; ● ‘Mașina mea preferată este x’.
 ● Fă același lucru cu un for each. ● Fă același lucru cu un while.
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# for

# for x in masini:
#     if x == 'Mercedes':
#         print(f'Masina mea preferata este {x}.')
#         break
#     else:
#         print('Nu-mi place aceasta masina!')

# for each

# for masina in masini:
#     print(f"Masina mea preferata este {masina}.")

# while

# masina_preferata = "Mercedes"

# while masina_preferata == "Mercedes":
#     print(f'Masina mea preferata este {masina_preferata}.')
#     break
# else:
#     print('Nu-mi place aceasta masina!')

'''
2. Aceeași listă: Folosește un for else În for - Modifică elementele din listă astfel încât să fie scrise cu majuscule,
 exceptând primul și ultimul.
În else: - Printează lista.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# for x in range(len(masini)):
#     if 0 < x < len(masini)-1:
#         masini[x] = masini[x].upper()
# print(masini)

'''
3.Aceeași listă: Vine un cumpărător care dorește să cumpere un Mercedes. Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’ Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel: Printează ‘Am găsit mașina X. Mai căutam‘
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dvs!')
#         break
#     else:
#         print(f'Am gasit masina {masina}.Mai cautam.')


'''
4. Aceeași listă;Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun: Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else). - Printează S-ar putea să vă placă mașina x.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lăstun':
#             continue
#     print(f'S-ar putea sa va placa masina {masina}.')

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi. ● Iterează prin mașini. ● Când găsesti Lăstun sau Trabant: 
- Salvează aceste mașini în masini_vechi. - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x. ● Modele noi: x.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []

# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lăstun':
#         masini_vechi.append('Trabant')
#         masini_vechi.append('Lăstun')
#         masini[5] = 'Tesla'
#         masini[7] = 'Tesla'
#         print(f'Modele vechi : {masini_vechi}  ')
#         print(f'Modele noi : {masini} ')

'''
6. Având dict:
pret_masini = {'Dacia': 6800, 
               'Lăstun': 500, 
                'Opel': 1100, 
                'Audi': 19000, 
                'BMW': 23000
                }
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget. 
● Iterează prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
● Iterează prin listă.
'''
# pret_masini = {'Dacia': 6800,
#                'Lăstun': 500,
#                 'Opel': 1100,
#                 'Audi': 19000,
#                 'BMW': 23000
#                 }

# for cheie, valoare in pret_masini.items():
#     if valoare <= 15000:
#         print(f'Pentru un buget de sub 15000 euro puteți alege mașină : {cheie}.')


'''
7. Având lista: numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3] 
● Iterează prin ea. ● Afișează de câte ori apare 3 .
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
# y = []

# for x in range(len(numere)):
#     if numere[x] == 3:
#         y.append(numere[x])
#         x += 1
# print(len(y))

'''
8. Aceeași listă: ● Iterează prin ea ● Calculează și afișează suma numerelor .
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]


# for index in range(len(numere)):
#     print(numere[index])
#     print(sum(numere))


'''
9. Aceeași listă: ● Iterează prin ea. ● Afișază cel mai mare număr .
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# for index in range(len(numere)):
#     print(max(numere))


'''
10. Aceeași listă: ● Iterează prin ea. ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3 ● Afișază noua listă.
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0

# for x in range(len(numere)):
#     if numere[x] >= 0 or numere[x] == -4:
#         numere.insert(x, -numere[x])
#         numere.remove(numere[x+1])
# print(numere)


'''
11. alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3] numere_pare = [] numere_impare = [] 
numere_pozitive = [] numere_negative = [] Itereaza prin listă alte_numere Populează corect celelalte liste 
Afișează cele 4 liste la final
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []

# for x in range(len(alte_numere)):
#     if alte_numere[x] % 2 == 0:
#         numere_pare.append/(alte_numere[x])
#     else:
#         numere_impare.append(alte_numere[x])
#     if alte_numere[x] > 0:
#         numere_pozitive.append(alte_numere[x])
#     else:
#         numere_negative.append(alte_numere[x])

# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

'''
12. Aceeași listă: Ordonează crescător lista fară să folosești sort. Te poți inspira vizual de aici.
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# for x in range(len(alte_numere)):
#     for y in range(len(alte_numere) - x - 1):
#         if alte_numere[y] > alte_numere[y + 1]:
#             alte_numere[y], alte_numere[y + 1] = alte_numere[y + 1], alte_numere[y]

# print(f'Numerele ordonate crescator sunt: {alte_numere}')

'''
13. Ghicitoare de număr: numar_secret = Generați un număr random între 1 și 30 Numar_ghicit = None 
Folosind un while User alege un număr Programul îi spune: ● Nr secret e mai mare ● Nr secret e mai mic 
● Felicitări! Ai ghicit!
'''
# import random

# numar_secret = random.randint(1, 30)
# gasit = False
# while not gasit:
#     numar_ghicit = int(input('Alege un numar de la 1 la 30 : '))
#     if numar_ghicit == numar_secret:
#         print('Felicitari!Ai ghicit!')
#         gasit = True
#     elif numar_ghicit > numar_secret:
#         print('Numarul secret e mai mic!')
#     else:
#         print('Numarul secret e mai mare!')

'''
14. Alege un număr de la tastatură Ex: 7 Scrie un program care să genereze în consolă următoarea piramidă 
1 22 333 4444 55555 666666 7777777
Ex:3 1 22 333
'''
# numar = int(input("Introduceti un numar: "))
# x = 1

# while x <= numar:
#     print(str(x) * x)
#     x += 1
# else:
#      print("Nu se poate genera o piramida cu numarul introdus!")

'''
15. tastatura_telefon = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [0] ]
    Iterează prin listă 2d Printează ‘Cifra curentă este x’ ( hint: nested for - adică for în for)
'''
# tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

# for x in tastatura_telefon:
#     for item in x:
#         print(f"Cifra curenta este {item}.")










