import requests, re, threading
from os import system

# ---------------
# Bu Dosya Canpolat Gökkaya kodlanmıştır
# Sizden proxy dosya adını isteyecek, örneğin: proxy.txt
# Ardından gönderi bağlantısı isteyecektir, örneğin: https://t.me/androedit/1450
# Kaç tane Pencere istiyorsun [default:350]
# Not: Yalnızca [ HTTP / HTTPS ] Proxy'ler İle Çalışır !

# Kanalım : t.me/androedit
# İnstagram : canpolatgkky
# ---------------

system("title " + f"TeleView Coded by @canpolatgkky")
print('''
████████╗███████╗██╗     ███████╗██╗   ██╗██╗███████╗██╗    ██╗
╚══██╔══╝██╔════╝██║     ██╔════╝██║   ██║██║██╔════╝██║    ██║
   ██║   █████╗  ██║     █████╗  ██║   ██║██║█████╗  ██║ █╗ ██║
   ██║   ██╔══╝  ██║     ██╔══╝  ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║
   ██║   ███████╗███████╗███████╗ ╚████╔╝ ██║███████╗╚███╔███╔╝
   ╚═╝   ╚══════╝╚══════╝╚══════╝  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ 
   
                               # Coded by @canpolatgkky                          

''')
_proxy_file = input(' [canpolatgkky] Proxy Dosyanızın İsmini Giriniz Default:[ proxy.txt ]: ')
link = input(' [canpolatgkky] Telegram Post Bağlantısını Giriniz: ').strip().replace('https://', '').replace('http://', '')
_threads = int(input(' [canpolatgkky] Kaç tane Pencere istiyorsun [ Default:200 ] :'))

print(' [?] Cihazınızı etkileyebilecek birçok Pencere kullanıyorsunuz [400 Altında Değer Girin]  ' if _threads > 400 else '')
if _threads > 400: '' if input(' - Atlamak İstediğinden Emin Misin ?[y/N]: ').strip().lower() == 'y' else exit()

main_url = f'https://{link}?embed=1'
views_url = 'https://t.me/v/?views='

proxies_file = open(str(_proxy_file), 'r').read()
proxies = proxies_file.splitlines()
count_proxies = len(proxies)
sent, bad_proxy, done, next_proxy = 0, 0, 0, 0

_headers = {
  'accept-language': 'en-US,en;q=0.9',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}


def tit(): system("title " + f"TeleView Coded by @canpolatgkky -- İstatistik: ({done}/{count_proxies}) -- Gönderilen: {sent} -- Kötü Proxy: {bad_proxy}")


def send_views():
    global sent, bad_proxy, done, next_proxy
    while True:
        try:
            proxy = proxies[next_proxy]
            next_proxy += 1
        except IndexError:
            break
        try:
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update(_headers)
            main_res = session.get(main_url).text
            _token = re.search('data-view="([^"]+)', main_res).group(1)
            views_req = session.get(views_url + _token)
            print(' [✅✅] GÖNDERİLDİ [✅✅]  ' + ' '+str(views_req.status_code))
            sent += 1
            done += 1
            tit()

        except requests.exceptions.ConnectionError:
            print(' [♦️] Proxy Hatalı: ' + proxy)
            bad_proxy += 1
            done += 1
            tit()


Threads = []
for t in range(_threads):
    x = threading.Thread(target=send_views)
    x.start()
    Threads.append(x)

for Th in Threads:
    Th.join()
