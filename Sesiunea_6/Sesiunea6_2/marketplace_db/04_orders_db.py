"""
Interactiunea cu tabelul orders + tabelul order_items
"""
import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CREATE ORDER

# pentru a crea o comanda completa, avem nevoie de
# un order, iar apoi avem nevoie de order items,
# care includ produsele/caracteristicile produselor

# 1. cream o comanda
# order_query = """
# INSERT INTO orders (customer_id, order_date)
# VALUES (1, '03.07.2023');
# """
#
# cursor.execute(order_query)
# connection.commit()

# 2. adaugam linii de comanda
# order_items_query = """
# INSERT INTO order_items (order_id, product_id, quantity, total_price)
# VALUES (?, ?, ?, ?);
# """

# order_items = [
#     (1, 1, 2, 240),
#     (1, 2, 1, 56.99)
# ]
#
# cursor.executemany(order_items_query, order_items)
# connection.commit()
#
# query = """
# INSERT INTO order_items (order_id, product_id, total_price)
# VALUES (1, 3, 25.45);
# """
# cursor.execute(query)
# connection.commit()

# READ/GET ORDER BY ID
#
# get_by_id_query = """
# SELECT * FROM orders
# WHERE id = ?;
# """
#
# cursor.execute(get_by_id_query, (1,))
#
# order = cursor.fetchone()
# print(order)
# print(order[1])

# READ/GET ALL ORDERS
#
# cursor.execute("""
# SELECT * FROM orders;
# """)
#
# for row in cursor.execute("SELECT * FROM orders;"):
#     print(row)

# UPDATE ORDER
#
# cursor.execute(
#     """
#     UPDATE orders SET order_date='04.07.2023'
#     WHERE id = 1;
#     """
# )
# connection.commit()

# DELETE ORDER
# TEMA:
# - Ce se intampla daca stergem un order? Sunt sterse automat
# si order items asociate?
#
# cursor.execute(
#     """
#     DELETE FROM orders
#     WHERE id = 1;
#     """
# )
# connection.commit()

# => A sters doar comanda fara a sterge order items.
# => Nu pot sterge order items dupa ce am sters order...


# adaugam o alta comanda
#
# order_query = """
# INSERT INTO orders (customer_id, order_date)
# VALUES (2, '04.07.2023');
# """
#
# cursor.execute(order_query)
# connection.commit()
