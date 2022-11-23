#CYB135 Week3 Lab 3.13
'''
3.13 LAB: Extracting Passwords (files and lists)
The Linux operating system is a very popular server OS. A network administrator has to protect the login/password files stored on the servers. In Linux there are two important files:

/etc/passwd

And it contains rows that look like this:

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
user1:x:15:51:User One:/home/user1:nologin
user2:x:15:51:User One:/home/user1:nologin
user3:x:15:51:User One:/home/user1:nologin
This file contains login information. It's a list of the server's accounts that has userID, groupID, home directory, shell and more info.

And the second file /etc/shadow, contains rows that look like this:

root:$1$TDQFedzX$.kv51AjM.FInu0lrH1dY30:15045:0:99999:7:::
bin:*:14195:0:99999:7:::
daemon:*:14195:0:99999:7:::
adm:*:14195:0:99999:7:::
ftp:*:14195:0:99999:7:::
user1:$1$ssTPXdzX$.kv51AjM.FInu0lrH1dY30:15045:0:99999:7:::
user1:44##$TDQFedzX$.Pxp39484.FInu0lrH1dY30:15045:0:99999:7:::
user1:%TXlsifhQMinXX@.YUlppxp0177:15045:0:99999:7:::
This file contains the actual password in encrypted format for each of the user's accounts stored in /etc/passwd. Notice the encrypted text after the login and : colon. That is the encrypted password.

Typically, if a hacker obtains access to these files, they could use some sort of cracking software to decrypt the passwords. Basically, they take a Brute Force approach and use common passwords to find a match.

Write a program that first reads in the name of two input files; input1pass.txt and input1shadow.txt. These files will contain encrypted and non-encrypted passwords to simulate a Brute Force approach. Next the program will accept input of two strings representing a potential user name, and password. The files should be read using the file.readlines( ) method.

Your program should output the attempted login and password with a message that it was a successful or unsuccessful brute force attempt.

Ex: If the input is:

input1pass.txt
input1shadow.txt
bobpickle
pa$$w0rd
and the contents of input1pass.txt are:

user1:x:15:51:User One:/home/user1:nologin
user2:x:16:52:User One:/home/user1:nologin
user3:x:17:53:User One:/home/user1:nologin
and the contents of the input1shadow.txt are:

user1:XXPP192920r:15045:0:99999:7:::
user1:LLmm928393x:15046:0:99999:7:::
user1:&^334294kksri.:15047:0:99999:7:::
the output is:

Brute Force Attempt:
Login:  user1
Password:  XXPP192920r
Unsuccessful brute force attempt

Brute Force Attempt:
Login:  user2
Password:  LLmm928393x
Unsuccessful brute force attempt

Brute Force Attempt:
Login:  user3
Password:  &^334294kksri.
Unsuccessful brute force attempt
Ex: If the input is:

input2pass.txt
input2shadow.txt
demo123
password
and the contents of input1pass.txt are:

user1:x:15:51:User One:/home/user1:nologin
user2:x:16:52:User One:/home/user1:nologin
user3:x:17:53:User One:/home/user1:nologin
demo123:x:18:54:Demo User:/home/demo123:nologin
and the contents of the input1shadow.txt are:

user1:XXPP192920r:15045:0:99999:7:::
user1:LLmm928393x:15046:0:99999:7:::
user1:&^334294kksri.:15047:0:99999:7:::
demo123:password:15048:0:99999:7:::
the output is:

Brute Force Attempt:
Login:  user1
Password:  XXPP192920r
Unsuccessful brute force attempt

Brute Force Attempt:
Login:  user2
Password:  LLmm928393x
Unsuccessful brute force attempt

Brute Force Attempt:
Login:  user3
Password:  &^334294kksri.
Unsuccessful brute force attempt

Brute Force Attempt:
Login: demo123
Password: password
Successful brute force attempt
Notes:

There is a newline at the end of the output.
input1pass.txt is available to download.
input1shadow.txt is available to download
'Hint' - check out the Python zip ( ) for mapping the login in one file to the other.
'''

passfile = input()
shadowfile = input()
usr = input()
pw = input()

userlst = []
with open (passfile) as f1:
    for line in f1:
        userlst.append (line.split(':')[0])

passlst = []
with open (shadowfile) as f2:
    for line in f2:
        passlst.append (line.split(':')[1])

for i in range (len(userlst)):
    print ("Brute Force Attempt:")
    print ("Login:", userlst[i])
    print ("Password:", passlst[i])
    if userlst[i] == usr and passlst[i] == pw:
        print ("Successful brute force attempt\n")
    else:
        print ("Unsuccessful brute force attempt\n")
