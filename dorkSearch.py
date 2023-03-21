import requests 
import proxybroker 
from googlesearch import search
import sys
from colorama import Fore,init
from colorama import Fore, Style
import warnings
import random
from http import cookiejar
import os
from time import sleep

lverde= Fore.LIGHTGREEN_EX
v = Fore.GREEN
cyan = Fore.CYAN
rojo = Fore.RED
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
blanco = Fore.WHITE
reset = Fore.RESET
yellow = Fore.YELLOW
blue = Fore.BLUE

os.system("clear")  
class BlockAll(cookiejar.CookiePolicy):
    ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
    
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

        

Banner = """
·▄▄▄▄        ▄▄▄  ▄ •▄ .▄▄ · ▄▄▄ . ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄
██▪ ██ ▪     ▀▄ █·█▌▄▌▪▐█ ▀. ▀▄.▀·▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█
▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ ▐▀▀▄·▄▀▀▀█▄▐▀▀▪▄▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▐█
██. ██ ▐█▌.▐▌▐█•█▌▐█.█▌▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌▐█•█▌▐███▌██▌▐▀
▀▀▀▀▀•  ▀█▄▀▪.▀  ▀·▀  ▀ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ ·
"""
print(rojo+Banner)
D = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
s = requests.Session()
s.cookies.set_policy(BlockAll())
att = input(f"{blue}[{rojo}+{blue}] {magenta}DORK A BUSCAR: {reset}")
print ("")
query = att
a =  random.choice(D)
try:  
    for b in search(query, a , num=10 , stop=95 , pause=2):
            print(f'{blue}[{rojo}+{blue}] {yellow}URL FOUND ==>'  + v+(b) )
            sleep(1)
except KeyboardInterrupt:
    print (rojo+"Parando Busqueda...")
    sleep(1)
    cyan
print(f'{blue}[{rojo}+{blue}] {cyan}Busqueda Realizada.'+reset)
