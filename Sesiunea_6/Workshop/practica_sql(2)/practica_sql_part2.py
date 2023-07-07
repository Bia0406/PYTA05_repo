import sqlite3
"""
Exercitii workshop 6 - Part 2 - SQL
"""

'''
1. Write a SQL statement to create a table called continents,
with the following columns:
a. continent_id
b. continent_name
c. continent_code – 2 letters code, use this link
'''

connection = sqlite3.connect("continents.db")

cursor = connection.cursor()

#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS continents (
#     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     continent_name VARCHAR,
#     continent_code VARCHAR(2) DEFAULT 'https://datahub.io/core/continent-codes'
#     );
#     """
# )
#
#
# connection.commit()

'''
2. Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
'''
# #
# connection = sqlite3.connect("continents.db")
#
# cursor = connection.cursor()
# continent_query = """
# INSERT INTO continents (continent_name, continent_code)
# VALUES (?, ?);
# """
# continents = [
#     ('AF', 'Africa'),
#     ('NA', 'North America'),
#     ('OC', 'Oceania'),
#     ('AN', 'Antarctica'),
#     ('EU', 'Europe'),
#     ('SA', 'South America')
#
# ]
#
# cursor.executemany(continent_query, continents)
# connection.commit()
#

'''
3. Write a SQL statement to create a table called countries, with the following columns: 
a. country_code – 2 letters code (e.g. RO, US, IT, etc) 
b. country_name 
c. continent_id – foreign key d. population – number
'''
# connection = sqlite3.connect("continents.db")
#
# cursor = connection.cursor()
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS countries (
#     country_code VARCHAR(2),
#     country_name VARCHAR,
#     country_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     population TEXT NOT NULL,
#     FOREIGN KEY (country_id) REFERENCES continents(id)
#     );
#     """
# )
#
#
# connection.commit()


'''
4. Write a few SQL statements to add some countries. Here is a list of countries with their codes. Feel free to invent or
approximate their populations, and use your geography knowledge for their continent. Add at least 10 countries, as diverse
as possible (INSERT). 
Examples: 
– Romania, EU, 19mil 
– USA, NA, 330mil 
– France, EU, 70mil 
– Hungary, EU, 9mil 
– Canada, NA, 40mil 
– China, AS, 1450mil 
– Belgium, EU, 12mil 
– Egypt, AF, 110mil 
– Australia, OC, 25mil
'''
# #
# connection = sqlite3.connect("continents.db")
#
# cursor = connection.cursor()
# #
# country_query = """
# INSERT INTO countries (country_code, country_name, population)
# VALUES (?, ?, ?);
# """
# countries = [
#     ('EU', 'Romania', '19mil'),
#     ('NA', 'USA', '330mil'),
#     ('EU', 'France', '70mil'),
#     ('EU', 'Hungary', '9mil'),
#     ('NA', 'Canada', '40mil'),
#     ('AS', 'China', '1450mil'),
#     ('EU', 'Belgium', '12mil'),
#     ('AF', 'Egypt', '110mil'),
#     ('OC', 'Australia', '25mil'),
#     ('EU', 'Portugal', '10mil')
# ]
#
# cursor.executemany(country_query, countries)
# connection.commit()
#

'''
5. Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
'''
#
# cursor.execute("""
# SELECT country_name FROM countries
# ORDER By country_name;
# """)
#
# countries = cursor.fetchall()
# print(countries)
#
#
# cursor.execute("""
# SELECT COUNT(country_name)
# FROM countries;
# """)
#
# country_name = cursor.fetchall()
# print(country_name)

'''
6. Write a SQL statement to select only countries with a population greater than 20 millions.
'''
#
# cursor.execute("""
# SELECT country_name FROM countries
# WHERE population > '20mil';
# """)
#
# population_countries = cursor.fetchall()
# print(population_countries)

'''
7. Write a SQL statement to select only countries that start with a certain letter (choose one that exists for you, e.g.
 C in the example above).
'''

# cursor.execute("""
# SELECT country_name FROM countries
# WHERE country_name LIKE 'C%' ;
# """)
#
# country_letter = cursor.fetchall()
# print(country_letter)


'''
8. Write a SQL statement that groups all countries by continents, and counts them.
'''
#
# cursor.execute("""
# SELECT COUNT(country_name), country_code
# FROM countries
# GROUP BY country_code
# ORDER BY COUNT(country_name);
# """)
#
# country_code = cursor.fetchall()
# print(country_code)


'''
9. Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
'''
#
# cursor.execute("""
# SELECT SUM(population), country_code
# FROM countries
# GROUP BY country_code
# ORDER BY SUM(population);
# """)
#
# population_continents = cursor.fetchall()
# print(population_continents)
#
# connection.close()
