"""
Folosim Simple Books API, descris aici : https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Toata rezolvarea se va face într-o clasa numita Books API Client.
Pentru testare se va crea un obiect din aceasta clasa și se vor apela metodele implementate.

1. Folosind endpoint-ul de authentication, genereaza un access token
(fa asta in constructor, client name si email ar trebui sa fie atribute).

2. Adaugă o metoda prin care poți vedea toate comenzile.

3. Adaugă o metoda prin care poți vedea toate cărțile.

4. Adaugă o metoda prin care poți posta/crea o comanda.

5. Adaugă o metoda prin care poți șterge o comanda.

"""
import requests

url = 'https://simple-books-api.glitch.me'

# 1 Get all books
#
# response = requests.get(f'{url}/books')
#
# print(response.status_code)
# print(response.json())

# 2 Get all books filtred by type and limit(query_params)
#
# response = requests.get(f'{url}/books?type=fiction&limit=2')
# print(response.status_code)
# print(response.json())

# v2
#
# data = {
#     'type': 'fiction',
#     'limit': 2
# }
# response2 = requests.get(f'{url}/books', params=data)
#
# print(response2.status_code)
# print(response2.json())

# # 3 Post create token
# data2 = {
#     "clientName": "Bianca",
#     "clientEmail": "bianca1@example.com"
# }
# response3 = requests.post(f'{url}/api-clients', json=data2)
# print(response3.status_code)
# print(response3.json())

# 4 Post place an order
token = '666b0a2a989a4c070edd04bbd8ff046d2749655996367194c5e7d3784e30fe49'
comanda = {
    "bookId": 1,
    "customerName": "Bianca"
}

headers_params = {
    'Authorization': token
}

response4 = requests.post(f'{url}/orders', json=comanda, headers=headers_params)
print(response4.status_code)
print(response4.json())


# class BooksAPIClient:
#
#     token = "666b0a2a989a4c070edd04bbd8ff046d2749655996367194c5e7d3784e30fe49"
#     __BASE_URL = 'https://simple-books-api.glitch.me'
#
#     def __init__(self, client_name, client_email):
#         self.client_name = client_name
#         self.client_email = client_email
#
#     def get_orders(self, order_id):
#         url = f'{self.__BASE_URL}/{order_id}'
#         status = requests.get(url)
#         return status
#
#     def get_books(self):
#         status = requests.get(self.__BASE_URL)
#         return status
#
#     def add_order(self, **kwargs):
#         url = f'{self.__BASE_URL}/add'
#
#         kwargs = {
#             "Client_name": "Popa Andrei",
#             "Client_email": "popaandrei@gmail.com"
#         }
#         status = requests.post(url, data=kwargs)
#         return status
#
#     def delete_order(self, order_id):
#         url = f'{self.__BASE_URL}/{order_id}'
#         status = requests.delete(url)
#         return status
#
#
# user = BooksAPIClient('Popa Alina', 'popaalina@gmail.com')
# print(user.token)
# print(user.client_name)


# def get_status(url):
#     res = requests.get(url)
#     return res
#
#
# response1 = get_status("https://simple-books-api.glitch.me/status%22)
# print(response1.status_code)
# print(response1.json())
#
# token = "666b0a2a989a4c070edd04bbd8ff046d2749655996367194c5e7d3784e30fe49"
#
# get all books
# avem posibilitatea (este OPTIONAL) sa furnizam query params: limit si type
# https://simple-books-api.glitch.me/books
# https://simple-books-api.glitch.me/books?limit=1
# https://simple-books-api.glitch.me/books?type=1
# https://simple-books-api.glitch.me/books?type=1&limit=2
# def get_all_books(url, limit=0, type=''):
#     link = url
#     # if limit is not None:
#     #     link = f"{url}?limit={limit}"
#     # if type is not None:
#     #     link = f"{url}?type={type}"
#     # if limit is not None and type is not None:
#     #     link = f"{url}?type={type}&limit={limit}"
#     data = {
#         "limit": limit,
#         "type": type
#     }
#     res = requests.get(link, params=data)
#     return res
#
#
# response2 = get_all_books("https://simple-books-api.glitch.me/books%22)
# response2 = get_all_books("https://simple-books-api.glitch.me/books", 1)
# response2 = get_all_books("https://simple-books-api.glitch.me/books", 2, "fiction")
# response2 = get_all_books("https://simple-books-api.glitch.me/books", type="fiction")
# print(response2.status_code)
# print(response2.json())
#
#
# and operator
# x = 5
# y = 2
#
# print(x and y == 2)
# FALS/GRESIT ! => se verifica daca x este 2 SI daca y este 2: False AND True -> FALSE
# CORECT => se evalueaza bool(x) si daca y este egal cu 2: True AND True -> TRUE
# print(bool(x))
# print(x == 2 and y == 2)

