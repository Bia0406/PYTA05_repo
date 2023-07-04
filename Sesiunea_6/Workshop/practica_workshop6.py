"""
Exercitii workshop 6
"""

'''
Pachete python. Interacțiune cu fișiere.
'''


'''
1. Create a text file called “hello.txt” and add the following text inside of it: 
Python 
Java
Javascript 
C/C++/C# 
PHP
Node.js 
Write a short program to read and display the text file
'''
#
# with open(file="hello.txt", mode="w") as file:
#     file.writelines([
#         "Python\n"
#          "Java\n"
#          "Javascript\n"
#          "C/C++/C#\n"
#          "PHP\n"
#          "Node.js\n"
#     ]
#     )

#
# def read_file(hello_txt):
#     with open("hello.txt", "r") as file:
#         return file.readlines()
#
#
# print(read_file("hello_txt", ))


'''
2. Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go 
Kotlin
Swift
Display the new contents of the file.
'''

#
# def write_read_file(hello_txt):
#     with open("hello.txt", "a") as file:
#         file.writelines([
#             "Go\n"
#             "Kotlin\n"
#             "Swift\n"
#         ]
#     )

#
# f = open("hello.txt", "r")
# for file in f:
#     print(f.read())
# f.close()

'''
3. Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
'''
#
# f = open("hello.txt", "r")
# for line in f:
#     print(f.read())



'''
4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below: 
My name is letter X. I am the 24th letter of the alphabet. Make sure you use the correct ending for the letter’s number 
(e.g. 1st, 2nd, 3rd, etc.)
'''





'''
5. Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade 1,Maria,Popescu,31,7.5 2,Andrei,Ionescu,26,8.0 3,Adriana,Marinescu,21,7.5 4,Matei,Gheorghescu,
42,8.5 5,Eusebiu,Pop,33,9.5 6,Ioana,Popa,29,9.0 Read the file using Python’s `csv` standard library, and display it in 
the terminal as a table, using the options for string formatting from Python:id fname
lname
age grade
---------------------------------------------------
1
Maria
2
3
4
5
6
Andrei
Adriana
Matei
Eusebiu
Ioana
Popescu
Ionescu
Marinescu
Gheorghescu
Pop
Popa
31 7.5
26 8.0
21 7.5
42 8.5
33 9.5
29 9.0
'''







'''
6. Read again the information from the csv file above, store it all in a list of
data, and then write a new file, called “students.json”, which will contain a
valid JSON object. Use the following format for each student (and use
Python’s standard JSON module):
[
{
"id": 1,
"fname": "Maria",
"lname": "Popescu",
"age": 31,
"grade": 7.5
},
...
]
'''








'''
7. Create a new PyCharm project. Make sure it has a virtualenv. Install all the
following packages from PYPI:
behave
behave-html-formatter
requests
selenium
webdriver-manager
Use pip to create a `requirements.txt` file. Send your project to a colleague
and ask them to install all dependencies using pip.
'''




'''
SQL
'''

'''
1. Write a SQL statement to create a table called continents, 
with the following columns: a. continent_id b. continent_name c. continent_code – 2 letters code, use this link
'''




'''
2. Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
'''



'''
3. Write a SQL statement to create a table called countries, with the following columns: a. country_code – 2 letters code 
(e.g. RO, US, IT, etc) b. country_name c. continent_id – foreign key d. population – number
'''



'''
4. Write a few SQL statements to add some countries. Here is a list of countries with their codes. Feel free to invent or 
approximate their populations, and use your geography knowledge for their continent. Add at least 10 countries, as diverse 
as possible (INSERT). Examples: – Romania, EU, 19mil – USA, NA, 330mil – France, EU, 70mil – Hungary, EU, 9mil – Canada, 
NA, 40mil – China, AS, 1450mil – Belgium, EU, 12mil – Egypt, AF, 110mil – Australia, OC, 25mil
'''




'''
5. Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
'''


'''
6. Write a SQL statement to select only countries with a population greater than 20 millions.
'''



'''
7. Write a SQL statement to select only countries that start with a certain letter (choose one that exists for you, e.g.
 C in the example above).
'''


'''
8. Write a SQL statement that groups all countries by continents, and counts them.
'''


'''
9. Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
'''
