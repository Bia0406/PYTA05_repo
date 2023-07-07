"""
Exercitii workshop 6 - Part 1 - Pachete python. Interacțiune cu fișiere.
"""

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
# f = open("hello.txt", "a")
# f.write("Go\n"
#         "Kotlin\n"
#         "Swift\n"
#         )
# f.close()
#
# f = open("hello.txt", "r")
# for x in f:
#     print(x)

'''
3. Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
'''
#
# with open("hello.txt", "r") as f:
#     for i in f:
#         x = f.readline()
#         print('only odd lines :' + i)

'''
4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below: 
My name is letter X. I am the 24th letter of the alphabet. Make sure you use the correct ending for the letter’s number 
(e.g. 1st, 2nd, 3rd, etc.)
# '''
#
# import string
#
# letters = string.ascii_uppercase
#
#
# for letter in letters:
#     file = letter + ".txt"
#
#     with open(file, "w") as f:
#         f.write(f"My name is letter {letter.upper()}. I am the {chr(ord(letter))}  letter of the alphabet ")


'''
5. Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade 
1,Maria,Popescu,31,7.5 
2,Andrei,Ionescu,26,8.0 
3,Adriana,Marinescu,21,7.5 
4,Matei,Gheorghescu,42,8.5 
5,Eusebiu,Pop,33,9.5 
6,Ioana,Popa,29,9.0 
Read the file using Python’s `csv` standard library, and display it in 
the terminal as a table, using the options for string formatting from Python:

id fname lname age grade
-------------------------------------
1 Maria Popescu 31 7.5
2 Andrei Ionescu 26 8.0
3 Adriana Marinescu 21 7.5
4 Matei Gheorghescu 42 8.5
5 Eusebiu Pop 33 9.5
6 Ioana Popa 29 9.0
'''
#
# import csv
#
#
# with open("students.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)


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
#
# import csv
# import json
#
#
# with open("students.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)
#
#
# def scriere_in_fisier_json(students_json, inf):
#     with open(students_json, 'w') as file:
#         json.dump(inf, file)
#
#
# students = [{
#         "id": 1,
#         "fname": "Maria",
#         "lname": "Popescu",
#         "age": 31,
#         "grade": 7.5
#         },
#     {
#         "id": 2,
#         "fname": "Andrei",
#         "lname": "Ionescu",
#         "age": 26,
#         "grade": 8.0
#     },
#     {
#         "id": 3,
#         "fname": "Adriana",
#         "lname": "Marinescu",
#         "age": 21,
#         "grade": 7.5
#     },
#     {
#         "id": 4,
#         "fname": "Matei",
#         "lname": "Gheorghescu",
#         "age": 42,
#         "grade": 8.5
#     },
#     {
#         "id": 5,
#         "fname": "Eusebiu",
#         "lname": "Pop",
#         "age": 33,
#         "grade": 9.5
#     },
#     {
#         "id": 6,
#         "fname": "Ioana",
#         "lname": "Popa",
#         "age": 29,
#         "grade": 9.0
#     }
# ]
#
# scriere_in_fisier_json("students.json", students)

