#CYB135 Week3 Lab 3.14
'''
3.14 LAB: Detecting Network Change (files and lists)
Securing a network from attacks means a network administrator is watching traffic and user activity. Change detection (CD) is a method used to track changes in your network. CD can detect files accessed during off hours to more complex algorithmic detections added to software applications that manage this process.

This program is going to manage user login times and attempt to detect any change in a users typical login attempts. It will use an input file to store data and read the file using the csv.reader( ) method. The file will contain a list of login_names, followed by login_time separated by commas.

Write a program that first reads in the name of an input file, reads the information stored in that file and determines if the user login has occurred at off hour times. The company employees work from 9 am to 5 pm so any other time would be an off hour login attempt. If the login attempt is made after hours, store the user name and login time in a dictionary with the user name as the key. Display all anomaly attempts at the end of the program. If there are no questionable login attempts display No anomaly login attempts

Ex: If the input is:

input1.csv
and the contents of input1.csv are: (store time as integers and use military time to simulate am and pm attempts)

bob,2,paula,1,nancy,8,thomas,23,zach,22,charlotte,4
the output is:

Anomaly login attempts:
nancy:8
thomas:23
zach:22
charlotte:4
Ex: If the input is:

input2.csv
and the contents of input2.csv are: (store time as integers and use military time to simulate am and pm attempts)


the output is:

No anomaly login attempts
Note: There is a newline at the end of the output, and input1.csv is available to download.
'''

import csv

#Declare a dict
anomolyAttempts = {}
filename = input()
with open(filename, mode='r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        #Take length of the row
        rowLength=len(row)
        i=0
        #Loop until rowLength
        while(i<rowLength):
            #Take name
            name= row[i]
            #Take time
            loginTime= int(row[i+1])
            #Increment i value
            i+=2
            #Check if time is between 9 am to 5pm(17)
            if not (loginTime>=9 and loginTime<=17):
                #If it belongs to off hours add to anomalies
                anomolyAttempts[name] = loginTime

if len(anomolyAttempts)==0:
    #No anomoly attempts
    print('No anomaly login attempts')
else:
    print('Anomaly Login Attempts:')
    #Print dictionary
    for key, value in anomolyAttempts.items():
        print(key, value)
