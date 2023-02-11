from urllib.request import hashlib

import turtle

import pyfiglet

import pyautogui
from colorama import Fore,Style

print(Fore.RED + Style.BRIGHT)

import pyfiglet
  
result = pyfiglet.figlet_format("VENOM CRACKER", font = "isometric1" )

print(result)

#-------------------------------------Turtle Animation 10 sec--------------------------------------------

t = turtle.Turtle()
s  = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle()

    #---------------------------------END Turtle Animation-----------------------------

pyautogui.password = pyautogui.password("Enter Cracker Password" "\U0001F47D")

if pyautogui.password ==  "password":
   print("Acess Denied.")
else:
    print("Acess Granted \u2714 ")
    emoji = "\u2714"
print(emoji)

if True:
   answer = input('Do you want to continue?:')
   if answer.lower().startswith("y"):
      print("Ok, Carry On Then""\U0001F47D")
   elif answer.lower().startswith("n"):
      print("Ok Bye --- | --- люблю тебя ")
      exit()

#SHA256 PORTION:
        #SHA-256 (Secure Hash Algorithm 2), of which SHA-256 is a part, is one of 
        #the most popular hash algorithms around. A cryptographic hash.
        #also often referred to as a “digest”, “fingerprint” or “signature”.
        #It is an almost perfectly unique string of characters that is generated from a separate.
        #piece of input text. SHA-256 generates a 256-bit (32-byte) signature.

while True:
    
    print()
    print ("Enter Type Of Hash You WanT To CracK (Select 3 to quit the script)!\n 1. SHA256-Hash \n 2. MD5-Hash \n 3. Quit Script")
    print() 
    k = input("Enter Type Of Yor Hash : ")

    if (k=="1"):
        passFound = False

        sha256hash = input("Please Enter The SHA256 Hash To Crack.\n >>>>>  ")

        with open ("Venom_Passwords.txt","r") as file:

            for guess in file:

                hashedGuess = hashlib.sha256(bytes(guess.strip(), 'utf-8')).hexdigest()

                if hashedGuess.upper() == sha256hash.upper():

                    print("The Password Is |------->>>>>>>> ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != sha256hash:
                    print("Password guess ",str(guess)," Does Not MaTcH >-----TRYING NEXT \u2714-------<")

        if (passFound==False):
            print("-------------| PASSWORD Is Not In The DataBase |-----------------")

#md5 Portion:
            #MD5 is a widely-used cryptographic hash function that takes an input 
            # (or "message") and returns a 128-bit fixed-size output called the "hash". 
            # The output is typically represented as a 32-character hexadecimal number. 
            # The function is designed to be a one-way function, meaning it is computationally 
            # infeasible to reverse the process and obtain the original message from the hash.
            # The MD5 algorithm is used in a variety of applications, including digital signature 
            # algorithms and file integrity verification.

    elif (k=="2"):
        passFound = False

        md5hash = input("Please Enter The MD5 HasH to CracK.\n >>>>>>>>  ")

        with open ("Venom_Passwords.txt","r") as file:    

            for guess in file:

            
                hashedGuess = hashlib.md5(bytes(guess.strip(), 'utf-8')).hexdigest()

            

                if hashedGuess.upper() == md5hash.upper():

                    print("The Password Is --------------->>>>>>>>>>>> ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != md5hash:
                    print("Password guess ",str(guess)," Does Not MaTcH >-----TRYING NEXT \u2714-------<")

        
        if (passFound==False):
            print("----------------| Password Is Not In The DataBase |--------")

    elif (k=="3"):
        quit()
