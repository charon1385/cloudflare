import socket
import time
try:
    from colorama import Fore
except:
    print("Pleas install colorama")
import sys
import subprocess
import os
def usage():
    os.system("cls")
    print(Fore.GREEN + """

    ****************************************************************
    *************       Information Gathering          *************
    *************                                      *************
    *************                                      *************
    *************       -s,--site    WebSite           *************
    *************                                      ************* 
    *************                                      *************            
    ****************************************************************
    """)

    input(Fore.GREEN+" [*] prees Enter Key (Press Enter...) ")
def cloudflare(site):
    print(""" [!] Welcome To The Cloudflare Bypasser Part \n\n [!] Please Enter The Target Website Address\n""")
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

    #site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Tetoolkit"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Bypass-CloudFlare"+Fore.RED+"""]
 #└──╼ """+Fore.WHITE+"卐 ")

    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
        except Exception:
            pass
    try:
        os.system("cls")
        print("[1] Please Check Internet\n[2] Try , Againe\n")
        input(Fore.GREEN+" [*] prees Enter Key (Press Enter...) ")
    except:
        print("")
        sys.exit()

if len(sys.argv) == 3:
    cloudflare(sys.argv[2])

else:
    usage()