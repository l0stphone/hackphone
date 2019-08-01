import time
import os
import sys

# VARIBLES
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

nonJBStateStart = True
JBStateStart = False
defaultBrowser = "anternetexplore"
allowedWebsites = ("")
DoURLThing = False

# MAIN
os.system("title PhoneHack" if os.name == "nt" else "")
print("PETABYTE Ultra-BIOS v1.0")
time.sleep(0.5)
print("Booting into BootDevice1")
time.sleep(5)
clear()
time.sleep(1)
sys.stdout.write("-")
time.sleep(0.2)
sys.stdout.write("\r--")
time.sleep(0.2)
sys.stdout.write("\r---")
time.sleep(0.2)
sys.stdout.write("\r---e")
time.sleep(0.2)
sys.stdout.write("\r---eO")
time.sleep(0.2)
sys.stdout.write("\r---eOS")
time.sleep(0.2)
sys.stdout.write("\r---eOS L")
time.sleep(0.2)
sys.stdout.write("\r---eOS Lo")
time.sleep(0.2)
sys.stdout.write("\r---eOS Log")
time.sleep(0.2)
sys.stdout.write("\r---eOS Logi")
time.sleep(0.2)
sys.stdout.write("\r---eOS Login")
time.sleep(0.2)
sys.stdout.write("\r---eOS Login-")
time.sleep(0.2)
sys.stdout.write("\r---eOS Login--")
time.sleep(0.2)
sys.stdout.write("\r---eOS Login---")
time.sleep(0.2)
print("")
print("No Login Found.")
print("")
print("Please Sign Up Below.")
print("")
username = input("Username: ")
if(username == ""):
    print("Enter a username next time.")
    time.sleep(3)
    raise SystemExit

password = input("Password: ")
if(len(password) <=  3):
    print("The Password must be bigger than 3")
    time.sleep(3)
    raise SystemExit

print("Welcome to eOS! Your best choice of non-gui operating systems!")
input("<Press enter to continue whenever brackets pop up>")
print("Don't worry about any security holes, as they aren't there...")
input("<>")
print("The start menu is pretty self-explanitory. Explore what you can do on this operating system. Its pretty medium.")
input("<>")
print("[PROT EAR 0]")
time.sleep(2)
print("Launching into area.StartMenu")
time.sleep(3)
clear()

while True:
    if(DoURLThing == True):
        if(url == "antersoft.com"):
            print("Contacting antersoft.com...")
            time.sleep(3)
            DoURLThing = False
    clear()
    print("eOS Start Menu")
    print("")
    print("1) About")
    print("")
    if(defaultBrowser == "anternetexplore"): print("2) Anternet Explorer")
    command = input("1 - 2> ")
    if(command == ""):
        print("Please enter a number")
        print("")
        time.sleep(4)
    elif(command != ""):
        commandInt = int(command)
        if(commandInt == 1):
            print("eOS Tabby v1.0.0")
            print("By l0stphone")
            print("Open-Source!")
            print("")
            input("<>")
        elif(commandInt == 2):
            if(defaultBrowser == "anternetexplore"):
                print("Starting Anternet Explorer...")
                time.sleep(3)
                clear()
                print("Welcome, %s, to Anternet Explorer!" % username)
                print("")
                print("For a list of websites to visit, go to antersoft.com")
                time.sleep(1)
                url = input("Where would you like to go? URL: ")
                DoURLThing = True
