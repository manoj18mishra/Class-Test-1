#import random library
import random
#Create a class named Cipher
class Cipher:
    #Creating the cipher key for encryption decryption
    cipher_key = random.randint(1,50)
    #Defining the constructor for the class
    def __init__(self):
        #Get the input from the user
        print("Please enter the text to be encrypted:",end="")
        self.text = input()
        print("The key is: {}".format(str(self.cipher_key)))
        #Call encrypt fucntion
        self.e_text = self.encrypt()
        #Call decrypt fucntion
        self.d_text = self.decrypt()
    #Defining encrypt module
    def encrypt(self):
        #Using generator expression for encrypting and filtering for alphanumeric values
        g_en = (chr(ord(x)+self.cipher_key) for x in self.text if x.isalnum())
        encrypted_text = ''.join(g_en)
        print("The encrypted text is: {}".format(encrypted_text))
        return encrypted_text
    #Defining decrypt module
    def decrypt(self):
        #Using generator expression for decrypting
        g_de = (chr(ord(x)-self.cipher_key) for x in self.e_text)
        decrypted_text = ''.join(g_de)
        print("The decrypted text is: {}".format(decrypted_text))
        return decrypted_text

c1=Cipher()