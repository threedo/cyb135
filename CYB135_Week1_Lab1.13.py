#CYB135 Week1 Lab 1.13

'''
1.13 LAB: Introduction to Cyptography (classes/constructors)
Cryptography is the practice of encryption. Information Security uses cryptography techniques to encrypt and decrypt data. A simple encryption method might take plaintext and mix up the letters using some predetermined pattern and then use that pattern to decrypt the data for reading.

Ciphers are the algorithms used to put the data into its secret pattern and then systematically decrypt it for reading. This script is going to use a famous simple cipher called the Caesar Cipher. It is a substitution cipher where each letter in the text is 'shifted' in a certain number of places. It uses the alphabet as the primary pattern and then based on the shift number, it would shift all the letters and replace the alphabet with our pattern.

For example, if our shift number was 3, then A would be replaced with D, if we performed a right shift. As an example:

Text = "THE CAT IS VISIBLE AT MIDNIGHT" Ciphertext = "WKH FDW LV YLVLEOH DW PLGQLIJKW"

The keys to decrypt this message are the shift number and the direction. The shift value can be any integer from 0 - 25. The above example uses shift = 3 and the shift direction is right or direction = 'r'.

Complete the CipherTest class by adding a constructor to initialize a cipher item. The constructor should initialize the shift to 0, and the direction to 'r' for right shift. If the constructor is called with a shift value, and direction, the constructor should assign each instance attribute with the appropriate parameter value.

Complete the following TODO's: (1) create input for text, shift value, and direction (use lower( )) to keep l and r lower case (2) create a cipher item and use the constructor with the above input values (3) use control structures to call shifttoright() if direction is right and call shifttoleft if direction is left. Make sure you print out the return encrypted message inside the control structures.

We can create the encrypted text by using the ord ( ) function. This function will return an integer that represents the Unicode code point of the character. Character are represented by different values for upp/er and lower case so an 'a' returns the integer 97. By using the unicode value we can add and subtract our shift value represented by an integer.

The given program accepts as input a text string as our message to be encrypted, a shift value, and a direction of 'l' for left and 'r' for right. The program creates a cipher item using the input values. The program outputs the encrypted message based on the shift value and the direction provided.

Ex: If the input is text = "Cryptography is fun!", shift = 4, and direction = l.
The output is:

Ynulpkcnwldu eo bqjk
'''

class CipherTest:

  def __init__(self, shift=0, direction='r', text="Testing"):
      self.text = text
      self.shift = shift
      self.direction = direction

  def shift_to_right(self):
      encrypted_Text = ""
      for i in range(len(self.text)):
          c = self.text[i]
          if(c == ' '):
              encrypted_Text += (' ')
          elif (c.isupper()):
              encrypted_Text += chr((ord(c) + self.shift-65) % 26 + 65)
          else:
              encrypted_Text += chr((ord(c) + self.shift-97) % 26 + 97)

      return encrypted_Text

  def shift_to_left(self):
      encrypted_Text = ""
      for i in range(len(self.text)):
          c = self.text[i]
          if(c == ' '):
              encrypted_Text += (' ')
          elif (c.isupper()):
              encrypted_Text += chr((ord(c) - self.shift-65) % 26 + 65)
          else:
              encrypted_Text += chr((ord(c) - self.shift-97) % 26 + 97)

      return encrypted_Text

if __name__ == "__main__":
    text=input()
    shift=int(input())
    direction=input().lower()

    cipher_item = CipherTest(shift, direction, text)

    if direction =='l':
        encrypted_Text=cipher_item.shift_to_left()
        print(encrypted_Text, end="")
    elif direction =='r':
        encrypted_Text=cipher_item.shift_to_right()
        print(encrypted_Text)
