from pyrogram import Client as yumiko, filters as filt
import pyrogram 
import os

API_ID = 9276915
API_HASH = "e8145ec48504292485900892fffaf890"
BOT_TOKEN = "6262747338:AAH6vsOF0FfuTVxV2tWLfoyEy1gtWNzy8kk"

app = yumiko("Yumkio", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

black = '\033[40m'
red = '\033[41m'
green = '\033[42m'
orange = '\033[43m'
blue = '\033[44m'
purple = '\033[45m'
cyan = '\033[46m'
lightgrey = '\033[47m'
clear = '\033[0m'
lgreen = '\033[92m'

banner = blue+'''

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
'''+clear
print(" ")
print(banner)
