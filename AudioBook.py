"""
Author: new92
Github: @new92
AudioBook: In this script the user enters the name of the file which contains the book and the script will 
convert into sound and play it.
"""

try:
    import platform
    from os import system
    from time import sleep
    import pyttsx3
    import sys
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring Warning...")
    sleep(1)
    if sys.platform.startswith('linux') == True:
        system("sudo pip install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
        pass

book=str(input("[::] Please enter the name of the file (which contains the book): "))
while book == None or book.endswith(".txt") == False:
    print("[!] Sorry can't convert this type of book :(")
    sleep(2)
    print("[+] Try another one :)")
    sleep(1)
    book=str(input("[::] Please enter again the name of the file: "))

file=open(book,'r')
content=file.readlines()
engine = pyttsx3.init()

for i in content:
    engine.say(i)
    engine.runAndWait()