"""
Interactiunea cu tabelul products
"""
import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CRUD

# CREATE PRODUCT
# product_query = """
# INSERT INTO products (name, category, price, stock_count, description)
# VALUES (?, ?, ?, ?, ?);
# """
#
# products = [
#     ("birou negru", "mobilier", 120, 2, "birou negru descriere"),
#     ("pitic de gradina", "gradina", 56.99, 5, "pitic gradina descriere"),
#     ("ghiveci flori alb", "gradina", 25.45, 10, "ghiveci flori descriere")
# ]
#
# cursor.executemany(product_query, products)
# connection.commit()


# READ PRODUCT (BY ID)

# get_by_id_query = """
# SELECT * FROM products
# WHERE id = ?;
# """
#
# cursor.execute(get_by_id_query, (2,))
#
#
# product = cursor.fetchone()
# print(product)
# print(product[2])

# READ/GET ALL PRODUCTS

# cursor.execute("""
# SELECT * FROM products;
# """)
#
# # v1
# # for row in cursor.execute("SELECT * FROM products;"):
# #     print(row)
#
# # v2
# products = cursor.fetchall()
# print(products)
#
# for product in products:
#     print(product)


# UPDATE PRODUCT
#
# cursor.execute(
#     """
#     UPDATE products SET description='ghiveci flori colorat', stock_count=12
#     WHERE id = 3;
#     """
# )
# connection.commit()

# DELETE PRODUCT

# cursor.execute(
#     """
#     DELETE FROM products
#     WHERE id = 2;
#     """
# )
# connection.commit()



# Mai adaugam un produs
#
# product_query = """
# INSERT INTO products (name, category, price, stock_count, description)
# VALUES (?, ?, ?, ?, ?);
# """
#
# products = [
#     ("roaba ornamentala gradina", "gradina", 56.99, 10, "roaba ornamentala gradina maro"),
# ]
#
# cursor.executemany(product_query, products)
# connection.commit()

