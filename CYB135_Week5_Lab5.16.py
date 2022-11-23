#CYB135 Week5 Lab 5.16
'''
5.16 LAB: Cryptographic Hashing Algorithms
Encryption methods, such as the Caesar Cipher encryption, allow us to encrypt and decrypt text using a special key. Another method of encrypting text / passwords is called hashing. Hashing uses special algorithms to 'scramble' the text, which is tougher to be hacked. The hash function can take numbers, letters, and symbols as input, then the function applies one of the special algorithms to output the scrambled text. The longer the output string is, the harder to hack the hashed data. The difference between hashing and the Caesar Cipher encryption is that one cannot 'decrypt' a hashed data to its original text.

Since a hashed data cannot be decrypted, a user must enter the original text, which will be hashed by the program. Then the program compares the hashed value with the hashed data stored previously for the original text. A salt is used, at times, to create a random sequence that is added to the original text before using the hashing algorithm. This can help prevent the Brute Force attacks from using common words to gain access.

Python's hashlib module provides programmers with an API for accessing the different hashing algorithms. Some common hashing algorithms are: md5, sha1, sha224, sha256, and blake2b. To apply an hashing algorithm, import the hashlib module and specify the hashing algorithm and an encoding format to be used. A common encoding format is 'utf-8'.

Given hash_function( ) defined in the default template, complete the main function that does the following tasks:

Create a list called hash_list that contains the five hashing algorithm names described above.
Read from the user a password to hash.
Declare a salt variable and initialize the variable to the hex representation of 4458585599393. Hint: Use function hex().
Use a for loop to iterate over the hash_list and call the hash_function() with the hashing algorithm names in the list. Store the returned value of hash_function() in a variable and output the algorithm name used and the hashed password. Note: Output a new line after each hashed password is printed.
hash_function( ) takes three parameters: the password to be hashed, a salt containing the hex representation of a 13-digit number, and a hashing algorithm name. hash_function( ) applies a specific hashing algorithm to the combination of the password and the salt value. hash_function( ) then returns a text containing the hashed data in hex representation and the salt value.

Ex: If the input is:

secretPass
the output is:

Testing hash algorithm:  md5
Hashed Password =  bd19f99253c948637d64a4acbd524047:0x40e18692da1

Testing hash algorithm:  sha1
Hashed Password =  e5fbad38af8ba59c2648e98b9ae4196dfcb9f719:0x40e18692da1

Testing hash algorithm:  sha224
Hashed Password =  ef0ed799dee72469e5d12ab096473fe6347ae64d5541e95f42478abc:0x40e18692da1

Testing hash algorithm:  sha256
Hashed Password =  e73b86702464baa976c947a2a8c06adedc1e45ff5a35a07db41385120ce1e10a:0x40e18692da1

Testing hash algorithm:  blake2b
Hashed Password =  386eef2364609396229c7b58f3606354c12224cecfbc97f7b435c83218eee0b93d453a8ffa1ca2fcfcf5452013bc671fb538f35e426b33e4f07cee1f04a16bc7:0x40e18692da1
'''

import hashlib

def hash_function(password, salt, al):
  if al == 'md5':
    #md5
    hash = hashlib.md5(salt.encode() + password.encode())
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()
  elif (al == 'sha1'):
    #sha1
    hash = hashlib.sha1()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()
  elif al == 'sha224':
    #sha224
    hash = hashlib.sha224()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()
  elif al == 'sha256':
    #sha256
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()
  elif al == 'blake2b':
    #blake2b512
    hash = hashlib.blake2b()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()
  else:
    print("Error: No Algorithm!")

if __name__ == "__main__":
    hash_list = ['md5', 'sha1', 'sha224', 'sha256', 'blake2b']
    password = str(input())
    salt = hex(4458585599393)
    for h in hash_list:
        new_password = hash_function(password,salt,h)
        print('Testing hash algorithm: ',h)
        print('Hashed Password =  {new_password}:{salt}')
        print()
