"""
Interactiunea cu tabelul users
"""

# CRUD operations/methods
# CREATE
# READ
# UPDATE
# DELETE
import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CREATE USER

# user 1
# are completate doar campurile obligatorii
#
# cursor.execute(
#     """
#     INSERT INTO users (username, email, password, first_name, last_name)
#     VALUES ('biancabad01', 'biancabia@gmail.com', 'bia1234', 'Bianca', 'Bad');
#     """
# )
# connection.commit()

# user 2
# are completate toate campurile (inclusiv cele optionale)
# adaugam valori intr-un mod dinamic
#
# user_query = """
# INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# """
#
# cursor.execute(
#     user_query,
#     ('alinapopa', 'alina@gmail.com', 'alina111', 'Alina', 'Popa'
#      'str. Trandafirilor', 'Nr.34', 'Brasov', '356745', 'Romania')
# )
# connection.commit()

# adaugarea mai multor inregistrari in tabelul users deodata
#
# user_query = """
# INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# """
# users_to_create = [
#     ('paulamarc', 'paulamarc@gmail.com', 'paula222', 'Paula', 'Marc',
#      'Str. 1 mai, Bl. 23, Ap. 21', 'Deva', '330125', 'Romania'),
#     ('bobdavid', 'david_bob@yahoo.com', '123456', 'David', 'Bob',
#      'Str. Florilor, Nr.45', 'Iasi', '254433', 'Romania')
# ]
#
# cursor.executemany(user_query, users_to_create)
# connection.commit()

# READ/ GET USER BY ID
#
# get_by_id_query = """
# SELECT * FROM users
# WHERE id = ?;
# """
#
# cursor.execute(get_by_id_query, (11,))

# cand executam un query de select, pentru a vedea rezultatul primit
# putem sa apelam/invocam metoda fetchone() disponibila
# pe obiectul cursor

# user = cursor.fetchone() # ne returneaza intrarea din db sub forma de tuplu
# print(user)
# print(user[2])

# GET USER BY username
# query = """
# SELECT * FROM users
# WHERE username = ?;
# """
# cursor.execute(query, ('alinapopa',))
# user2 = cursor.fetchone()
# print(user2)

# # READ / GET ALL USERS
# cursor.execute("""
# SELECT * FROM users;
# """)
#
# # v1  cursor => iterator

# for row in cursor.execute("SELECT * FROM users;"):
#     print(row)

# v2

# users = cursor.fetchall()
# print(users)
#
# for user in users:
#     print(user)

# READ/ GET ALL USERS (only username and email columns)
# #
# cursor.execute("""
# SELECT username, email FROM users;
# """)
#
# users = cursor.fetchall()
# print(users)
#
# for user in users:
#     print(user)

# UPDATE USER
# schimbam username-ul, email, password,first_name and last_name pentru user-ul cu id-ul 1
# cursor.execute(
#     """
#     UPDATE users SET email='biancabia@gmail.com', username='biancabad01', password='bia1234', first_name='Bianca',
#     last_name='Bad'
#     WHERE id = 1;
#     """
# )
# connection.commit()

# update last name and address
# cursor.execute(
#     """
#     UPDATE users SET  last_name='Popa', address='Str. Trandafirilor, nr. 34'
#     WHERE id = 5;
#     """
# )
# connection.commit()


# DELETE USER
# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 4;
#     """
# )
# connection.commit()
#
# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 2;
#     """
# )
# connection.commit()

# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 11;
#     """
# )
# connection.commit()

# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 10;
#     """
# )
# connection.commit()
#
# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 9;
#     """
# )
# connection.commit()
#
# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 8;
#     """
# )
# connection.commit()
#
# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 7;
#     """
# )
# connection.commit()
#
# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 6;
#     """
# )
# connection.commit()
#
# cursor.execute(
#     """
#     DELETE FROM users
#     WHERE id = 12;
#     """
# )
# connection.commit()


# user_query = """
# INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# """
#
# cursor.execute(
#     user_query,
#     ('alinapopa', 'alina@gmail.com', 'alina111', 'Alina', 'Popa'
#      'str. trandafirilor', 'nr.34', 'Brasov', '356745', 'Romania')
# )
# connection.commit()
