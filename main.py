import random
import os
import time
import os
import pyfiglet as pf

def RegisterData():
    os.system('cmd /c "pip install pyfiglet"')

def generatePassword(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Password will be generated In "+ timer, end="\r")
        time.sleep(1)
        t -= 1
    os.system('cls')

def PasswordGenerator():
    lower = 0
    upper = 0
    number = 0
    count = 0
    password = []

    length = input("Enter Password Length: ")
    length = int(length)
    
    if type(length) == int:
        while count < length:
            rand = random.randint (0,3)
            if rand == 0:
                lower += 1
                b = int(random.randint (97,123))
                password.append(b)
            elif rand == 1:
                upper += 1
                b = random.randint (65,91)
                password.append(b)
            elif rand == 2:
                number += 1
                b = random.randint (48,58)
                password.append(b)
            count += 1
        password = "".join([chr(c) for c in password])
        # function call
        generatePassword(int(5))
        print("Password: " + password + "\n")
        enter = input("Press ENTER to continue ...")
        if enter:
            os.system('cls')
            MenuUI()
        else:
            os.system('cls')
            MenuUI()
    
    elif length:
        print("must be a number")
        
def IPCheck():
    a = 1
    
def MenuUI():
    print(pf.figlet_format("Power Tools", font="bulbhead"))
    print("    Github : github.com/MuhammadDaffaTFA\n    Instagram : @mdafftfa\n\nChoose, what do you want to do in below: \n1) Random Password Generator \n2) Coming soon\n")
    option = int(input("Select Options: "))
    
    if type(option) == int:
        if option == 1:
            PasswordGenerator()
        elif option == 2:
            IPCheck()
        elif option == 0:
            Update()
        else:
            return MenuUI()
    else:
        return MenuUI()
        
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("You will back to Menu in "+ timer, end="\r")
        time.sleep(1)
        t -= 1
    
    os.system('cls')
    MenuUI()
    
MenuUI()
