import requests
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


class BooksAPIClient:

    __BASE_URL = 'https://simple-books-api.glitch.me'

    def __init__(self, client_name, client_email):
        self.client_name = client_name
        self.client_email = client_email

    def get_orders(self, order_id):
        url = f'{self.__BASE_URL}/{order_id}'
        status = requests.get(url)
        return status

    def get_books(self):
        status = requests.get(self.__BASE_URL)
        return status

    def add_order(self, **kwargs):
        url = f'{self.__BASE_URL}/add'

        kwargs = {
            "ClientName": "Popa Andrei",
            "ClientEmail": "popaandrei@gmail.com"
        }
        status = requests.post(url, data=kwargs)
        return status

    def delete_order(self, order_id):
        url = f'{self.__BASE_URL}/{order_id}'
        status = requests.delete(url)
        return status


user = BooksAPIClient('Popa Alina', 'popaalina@gmail.com')
status = Workshop.get_orders()
print(status.get_orders)
print(status.json())
