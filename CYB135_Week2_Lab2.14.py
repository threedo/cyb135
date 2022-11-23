#CYB135 Week2 Lab 2.14

'''
2.14 LAB: Exception handling to detect input string vs. integer
The given program reads a list of single-word first names and ages (ending with -1), and outputs that list with the age incremented. The program fails and throws an exception if the second input on a line is a string rather than an integer. At FIXME in the code, add try and except blocks to catch the ValueError exception and output 0 for the age.

Ex: If the input is:

Lee 18
Lua 21
Mary Beth 19
Stu 33
-1
then the output is:

Lee 19
Lua 22
Mary 0
Stu 34
'''

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
age = parts [1]

while name != '-1':
    # Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1

        # printing name and age
        print('{} {}'.format(name, age))

    except ValueError:

        # printing name and age as 0
        print('{} {}'.format(name, 0))

    # Get next line
    parts = input().split()
    name = parts[0]
