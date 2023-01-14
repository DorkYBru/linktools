from art import *
import os
tprint("HtmlTools")
print("1.Redirect your link via popular websites.")
print("2. Make your youtube channel link subscribe")
uinput=input("Whatchu wanna do? ")
def sub():
    suburl=input("Paste your channel link ")
    print(suburl + "?sub_confirmation=1")
def redir():
    os.system("cls")
    tprint("HtmlTools Redirect")
    redirurl=input("What link you want to redirect? ")
    print("1.url@your url")
    print("2.google url")
    method=input("What method you want to use? ")
    if method == "1":
        scndurl = input("Gimmie second url ")
        fullurl= scndurl + "@" + redirurl
        print(fullurl)
    if method == "2":
        fullurl= "https://www.google.com/url?sa=t&url=" + redirurl + "&usg=AOvVaw1YigBkNF7L7D2x2Fl532mA"
        print(fullurl)
if uinput == "1":
    redir()
if uinput == "2":
    sub()


