#CYB135 Week4 Lab 4.9
'''
4.9 LAB: Sorting TV Shows (dictionaries and lists)
Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, separating multiple TV shows associated with the same key with a semicolon (;). Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.

Ex: If the input is:

file1.txt
and the contents of file1.txt are:

20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote
the file output_keys.txt should contain:

10: Will & Grace
12: Murder, She Wrote
14: Dallas
20: Gunsmoke; Law & Order
30: The Simpsons
and the file output_titles.txt should contain:

Dallas
Gunsmoke
Law & Order
Murder, She Wrote
The Simpsons
Will & Grace
Note: There is a newline at the end of each output file, and file1.txt is available to download.
'''

filename = input()

f = open(filename, 'r')
data = f.readlines()
f.close()

dictionary = {}
list_of_values =[]

for i in range(len(data)):
    data[i] = data[i].strip()

for i in range(0, len(data), 2):
    list_of_values.append(data[i+1])
    if data[i] in dictionary:
        dictionary[data[i]] = dictionary[data[i]]+'; '+data[i+1]
    else:
        dictionary[data[i]] = data[i+1]


f = open('output_keys.txt', 'w')

for item in sorted(dictionary.items()):
    f.write(str(int(item[0]))+': '+item[1]+'\n')

f.close()

f = open('output_titles.txt', 'w')

list_of_values.sort()

for each in list_of_values:
    f.write(each+'\n')

f.close()
