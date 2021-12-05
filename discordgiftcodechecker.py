import requests
import random
from colorama import Fore

codes = open("codes.txt", "r")
proxyfile = open("proxies.txt", "r")

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def random_line(afile):
    afile.seek(0)
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num):
          continue
      line = aline
    return line

print(Fore.BLUE + """
 ██████╗  ██████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ███╗██║         ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║   ██║██║         ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝╚██████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝  ╚═════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                    By raptor root#1337""")

for code in codes:
    proxies = { "http": random_line(proxyfile) }
    r = requests.get("https://discordapp.com/api/v6/entitlements/gift-codes/" + code, proxies = proxies)
    if '{"message": "404: Not Found", "code": 0}' in r.text:
        print(Fore.RED + "[-] Empty Code")
    elif '{"message": "Unknown Gift Code", "code": 10038}' in r.text:
        print(Fore.RED + "[-] Not Working Code: " + code)
    elif 'You are being rate limited.' in r.text:
        print(Fore.RED + "[-] Rate Limit")
    elif '"redeemed": false' in r.text:
        print(Fore.GREEN + "[+] Working Code: " + code + " Name: " + find_between(r.text, '"name": "', '",'))
    else:
        print(Fore.RED + "[-] An Error Occured")
