import re
import requests
import threading


print('''
   ____   ____ ___ _   _ _   _     ____ _____ ____  _____  ____ _____ _| |_ ___   ____ 
  |  _ \ / ___) _ ( \ / ) | | |   / _  | ___ |  _ \| ___ |/ ___|____ (_   _) _ \ / ___)
  | |_| | |  | |_| ) X (| |_| |  ( (_| | ____| | | | ____| |   / ___ | | || |_| | |    
  |  __/|_|   \___(_/ \_)\__  |   \___ |_____)_| |_|_____)_|   \_____|  \__)___/|_|    
  |_|                   (____/   (_____|                                               

                                                                [ HTTP-HTTPS ]
       
        - Coded By Canpolatgkky
        
        - Kanalım : t.me/androdit
        - İnstagram : canpolatgkky
            
''')


urls = '''
https://openproxy.space/list/http
https://free-proxy-list.com/
https://hidemy.name/tr/proxy-list/?type=hs#list
http://free-proxy.cz/en/proxylist/country/all/http/ping/all
http://free-proxy.cz/en/proxylist/country/all/https/ping/all
https://api.proxyscrape.com/?request=getproxies&proxytype=http4&timeout=10000&country=all
https://api.proxyscrape.com/?request=getproxies&proxytype=https4&timeout=10000&country=all
https://spys.one/
https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
'''


file = open('proxy.txt', 'w')
file.write(' Telegram : @canpolatgkky Proxyleriniz:\n')
file.close()
file = open('proxy.txt', 'a')
good_proxies = list()


def pattern_one(url):
    ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)
    if not ip_port: pattern_two(url)
    else:
        for i in ip_port:
            file.write(str(i) + '\n')
            good_proxies.append(i)


def pattern_two(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('td>(\d{2,5})<', url)
    if not ip or not port: pattern_three(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_three(url):
    ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('>\n[\s]+(\d{2,5})\n', url)
    if not ip or not port: pattern_four(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_four(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('>(\d{2,5})<', url)
    if not ip or not port: pattern_five(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_five(url):
    ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('(\d{2,5})', url)
    for i in range(len(ip)):
        file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
        good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def start(url):
    try:
        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text
        pattern_one(req)
        print(f' [+] Proxy Çekilecek Site: {url}')
    except requests.exceptions.SSLError: print(str(url) + ' [x] SSL Hatası')
    except: print(str(url) + ' [x] Bilinmeyen hata')


threads = list()
for url in urls.splitlines():
    if url:
        x = threading.Thread(target=start, args=(url, ))
        x.start()
        threads.append(x)


for th in threads:
    th.join()


input(f' \n\n[canpolatgkky] Toplam Bulunan Proxyler : ({len(good_proxies)}) Adet proxy.txt Dosyasına Kayıt Edilldi. ')
