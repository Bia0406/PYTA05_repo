import requests

"""
Practice exercise
"""

'''
Folosim https://jsonplaceholder.typicode.com/guide/ 
Toate requesturile se vor face prima data in Postman (pentru verificare), iar apoi folosind libraria requests din Python.
Structura datelor este următoarea: 
- fiecare post este deținut de un user, și poate avea mai multe comments 
- fiecare album este deținut de un user, și poate avea mai multe photos 
- fiecare todo este detinut de un user.

* Alege un user din lista de useri predefiniti. Pentru acesta, fa requesturile necesare pentru a afișa următoarele informații: 
-> lista de posts 
-> lista de albume 
-> lista de todos
Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste doar informații despre 
primele 3 obiecte, iar apoi afiseaza "+x more posts/albums/todos", unde x este numărul de obiecte rămase.
* Alege un post, și afișează lista de comentarii. Alege un album, si afiseaza lista de photos.

* Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul pentru a vedea cum ar arata în viitor 
dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?

* Alege un post existent și realizează operațiunile de PUT si PATCH (atentie, modificările NU vor fi salvate, 
analizăm doar răspunsul). Ce observi ca este diferit între cele 2 metode?

* Folosind query parameters, filtrează lista de todos pentru userul ales astfel incat sa afisezi doar todos care 
nu sunt completed.

* Alege un album, și ia pozele din acesta în 2 moduri diferite (o data cu nested resource, o data folosind query params).
 Verifica dacă exista vreo diferenta intre cele 2 rezultate.
'''

# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response)
# print(response.json())
# for items in response.json():
#     print(items)


# *
# response = requests.get('https://jsonplaceholder.typicode.com/users/1/posts')
#
# for item in response.json():
#     if item['userId'] - - 1 and item['id'] - - 9:
#         print(item)

# response = requests.get('https://jsonplaceholder.typicode.com/users/1/albums')
#
# for item in response.json():
#     if item['userId'] - - 1 and item['id'] - - 9:
#         print(item)

# response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

# for item in response.json():
#     if item['userId'] - - 1 and item['id'] - - 9:
#         print(item)

# *
# payload = {'userId': '1', 'id': '102'}
# r = requests.post('https://jsonplaceholder.typicode.com/posts')

# print(payload)

# payload = {'userId': '1', 'id': '1'}
# r = requests.get('https://jsonplaceholder.typicode.com/albums')
#
# print(payload)

