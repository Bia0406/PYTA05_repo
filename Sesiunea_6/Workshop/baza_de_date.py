import sqlite3
"""

1. Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link: https://datahub.io/core/continent-codes
"""

# connection = sqlite3.connect("continents_practice1.db")
# cursor = connection.cursor()


# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS continents (
#     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     continent_name TEXT NOT NULL,
#     continent_code CHAR(2) NOT NULL
#     );
#     """
# )


# connection.commit()


"""
2. Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
"""

# connection = sqlite3.connect("continents_practice1.db")

# cursor = connection.cursor()

# continent_query = """
# INSERT INTO continents (continent_name, continent_code)
# VALUES (?, ?);
# """
# continents = [
#     ('Africa', 'AF'),
#     ('North America', 'NA'),
#     ('Oceania', 'OC'),
#     ('Antarctica', 'AN'),
#     ('Asia', 'AS'),
#     ('Europe', 'EU'),
#     ('South America', 'SA')

# ]

# cursor.executemany(continent_query, continents)
# connection.commit()


"""
3. Write a SQL statement to create a table called countries, with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number
"""

# connection = sqlite3.connect("continents_practice1.db")

# cursor = connection.cursor()

# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS countries (
#     country_code CHAR(2) NOT NULL,
#     country_name TEXT NOT NULL,
#     continent_id INTEGER NOT NULL,
#     population INTEGER NOT NULL,
#     FOREIGN KEY (continent_id) REFERENCES continents(continent_id)
#     );
#     """
# )


# connection.commit()


"""
4. Write a few SQL statements to add some countries. Here is a list of countries with their codes.
Feel free to invent or approximate their populations,
 and use your geography knowledge for their continent.
Add at least 10 countries, as diverse as possible (INSERT). Examples:
– Romania, EU, 19mil
– USA, NA, 330mil
– France, EU, 70mil
– Hungary, EU,  9mil
– Canada, NA, 40mil
– China, AS, 1450mil
– Belgium, EU, 12mil
–  Egypt, AF, 110mil
– Australia, OC, 25mil
"""


# connection = sqlite3.connect("continents_practice1.db")

# cursor = connection.cursor()

# country_query = """
# INSERT INTO countries (country_code, country_name, continent_id, population)
# VALUES (?, ?, ?, ?);
# """
# countries = [
#     ('RO', 'Romania', 6, 19000000),
#     ('US', 'USA', 2, '330000000'),
#     ('FR', 'France', 6, '70000000'),
#     ('HU', 'Hungary', 6, '9000000'),
#     ('CA', 'Canada', 2, 40000000),
#     ('CN', 'China', 5, 1450000000),
#     ('BE', 'Belgium', 6, 12000000),
#     ('EG', 'Egypt', 5, 110000000),
#     ('AU', 'Australia', 1, 25000000),
#     ('PT', 'Portugal', 6, 10000000)
# ]
#
# cursor.executemany(country_query, countries)
# connection.commit()


"""
5. Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
"""

# connection = sqlite3.connect("continents_practice1.db")

# cursor = connection.cursor()

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


"""
6. Write a SQL statement to select only countries with a population greater than 20 millions.
"""

# cursor.execute("""
# SELECT country_name FROM countries
# WHERE population > 20000000;
# """)
#
# population_countries = cursor.fetchall()
# print(population_countries)

"""
7. Write a SQL statement to select only countries that start with a certain letter (choose one that exists for you, e.g. 
C in the example above).
"""

# cursor.execute("""
# SELECT country_name FROM countries
# WHERE country_name LIKE 'C%' ;
# """)
#
# country_letter = cursor.fetchall()
# print(country_letter)


"""
8. Write a SQL statement that groups all countries by continents, and counts them.
"""
#
# cursor.execute("""
# SELECT COUNT(country_name), continent_id
# FROM countries
# GROUP BY continent_id
# ORDER BY COUNT(country_name);
# """)
#
# country_code = cursor.fetchall()
# print(country_code)


"""
9. Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
"""

# cursor.execute("""
# SELECT SUM(population), continent_id
# FROM countries
# GROUP BY continent_id
# ORDER BY SUM(population);
# """)
#
# population_continents = cursor.fetchall()
# print(population_continents)
#
# connection.close()


"""
Extra exercises can be found online:
W3Schools: https://www.w3schools.com/mysql/exercise.asp?filename=exercise_select1
OneCompiler: https://onecompiler.com/mysql
"""
