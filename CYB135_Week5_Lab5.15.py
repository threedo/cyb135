#CYB135 Week5 Lab 5.15
'''
5.15 LAB: Hacking Ciphers
The Caesar Cipher Algorithm was introduced in Week #1. Encryption is the act of encoding a message with the intent of allowing only authorized people the knowledge of how to read that message. An encrypted message can be decoded, allowing the secured content to be read after decryption.

Recall that the Caesar Cipher uses alphabets as the primary source of information but shifted a certain number of letters to the left or right as a key to create the encrypted data. The Caesar Cipher is easily hacked because of the simple technique used to build the key that encrypts and decrypts the data.

In this lab, the key is the number of alphabets shifted, and the direction is always toward the increasing alphabetical order. This provides 26 ways of encrypting a message and therefore makes it easier to be hacked by guessing the key within the range of 0 - 25.

Write the function caesar_hack( ) that takes three parameters: a Caesar Cipher encrypted message, an alphabet list, and the original message. Function caesar_hack( ) uses a Brute Force Attack to find the key that decrypts the encrypted message correctly. This would typically be a technique used by an unauthorized user.

Use a nested for loop in the function caesar_hack( ) to try all the possible keys. For each key, check the encrypted letter position based on the alphabet letter and attempt to decrypt the message. If the decrypted message is the same as the original message, return the key value and the decrypted message. If a key is not found, return 99 as the key and "Error: Key not found!" as the message. Note: The decrypted message is always in upper case due to the uppercase letters in the alphabet list. Convert the original message to upper case before being compared.

In main: Add a call to the caesar_hack() function. Make sure you capture both of your returned variables. Then add control structures that output the returned error message if the returned key is 99, or output "Successful attempt found! Key = the returned key" followed by "Secret message: the returned message" in a new line.

Ex: If the input is:

4
then the output is:

Brute Force Hack Attempt:
Encrypted Message:  XLMW MW E WIGVIX QIWWEKI
Successful Attempt found! Key = 4
Secret message: THIS IS A SECRET MESSAGE
Ex: If the input is:

22
then the output is:

Brute Force Hack Attempt:
Encrypted Message:  PDEO EO W OAYNAP IAOOWCA
Successful Attempt found! Key = 22
Secret message: THIS IS A SECRET MESSAGE
'''

def caesar_cipher_encrypt(text, key, a):
    text = text.upper()
    encrypted_Text = ""
    for i in text:
        if i in a:
            index = (a.find(i) + key) % len(a)
            encrypted_Text = encrypted_Text + a[index]
        else:
            encrypted_Text = encrypted_Text + i
    return encrypted_Text

#Caesar Cipher Decrypt function
def caesar_cipher_decrypt(text, key, a):
    text = text.upper()
    decrypted_Text = ""
    for i in text:
        if i in a:
            index = (a.find(i) - key) % len(a)
            decrypted_Text = decrypted_Text + a[index]
        else:
            decrypted_Text = decrypted_Text + i
    return decrypted_Text

def caesar_hack(text, a, check):
  for key in range(len(a)):
    hack = ""
    for c in text:
        if c in a:
          num = a.find(c)
          num = num - key
          if num < 0:
            num = num + len(a)
          hack = hack + a[num]
        else:
          hack = hack + c
    if (hack == check.upper()):
      return key, hack
  return 99, "Error: Key not found!"


if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = "This is a secret message"
    shift = int(input()) #Number between 1 & 25
    encrypted_data =  caesar_cipher_encrypt(text, shift, alphabet)
    print('Brute Force Hack Attempt: ')
    print ('Encrypted Message: ', encrypted_data)
    key,msg = caesar_hack(encrypted_data,alphabet,text)
    if key==99:
        print(msg)
    else:
        print('Successful Attempt found! Key =',key)
        print('Secret message:',msg)
