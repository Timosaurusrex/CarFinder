from bs4 import BeautifulSoup
import requests
import time
import willhaben_lib as wh
from math import sqrt
import json

url_requ = input("JSON einfügen:\n")
if(url_requ == ""):
    url = {"brand":"BMW","type":"3er-Reihe","keyword":"","mileage":"100000","price":"20000","year":"2015","extras":{"heatedSeats": False,"navigation": False,"diesel": True,"benzin": True,"elektro": False,"hybrid": False}}
else:
    print(url_requ)
    try:
        url = json.loads(url_requ)
        print(url)
    except Exception as e:
        print(e)
        print("JSON konnte nicht geladen werden, bitte erneut versuchen!")

time1 = time.time()

autos = []
i = 1

#https://www.willhaben.at/iad/gebrauchtwagen/auto/gebrauchtwagenboerse?sfId=93da4042-34d7-49a9-bc14-131974d73f0a&CAR_MODEL/MODEL=1775&rows=30&CAR_MODEL/MAKE=1043&isNavigation=true&ENGINE/FUEL=100001&EQUIPMENT=42&EQUIPMENT=15&EQUIPMENT=102&EQUIPMENT=100&EQUIPMENT=86&page=1
url_changed = f"https://www.willhaben.at/iad/gebrauchtwagen/auto/gebrauchtwagenboerse?sfId=b82af512-8a99-419e-a408-df37680ae11d&isNavigation=true&CAR_MODEL/MAKE={wh.brand[url['brand']]}&rows=30&keyword={url['type'] + '%20' + url['keyword'].replace(' ','%20')}&page=1&MILEAGE_TO={str(url['mileage'])}&YEAR_MODEL_FROM={str(url['year'])}&PRICE_TO={str(url['price'])}&ENGINEEFFECT_FROM=74&MOTOR_CONDITION=20&MOTOR_CONDITION=50&MOTOR_CONDITION=10&MOTOR_CONDITION=91&MOTOR_CONDITION=40"

if (url['extras']['heatedSeats'] == True):
    url_changed = url_changed + "&EQUIPMENT=15"
if (url['extras']['navigation'] == True):
    url_changed = url_changed + "&EQUIPMENT=16"
if (url['extras']['diesel'] == True):
    url_changed = url_changed + "&ENGINE/FUEL=100003"
if (url['extras']['benzin'] == True):
    url_changed = url_changed + "&ENGINE/FUEL=100001"
if (url['extras']['elektro'] == True):
    url_changed = url_changed + "&ENGINE/FUEL=100004"
if (url['extras']['hybrid'] == True):
    url_changed = url_changed + "&ENGINE/FUEL=100013&ENGINE/FUEL=100022"

print(url_changed)

while (i <= 99):
    #print(i)
    #time.sleep(0.5)
    url_final = url_changed.replace("&page=1", f"&page={i}").replace("&rows=30", f"&rows=5")
    page = requests.get(url_final)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('div', attrs={'id': 'skip-to-resultlist'})
    rows = table.findAll('div', attrs={'class': 'Box-sc-wfmb7k-0 iENLOS'})
    if (len(rows) == 0 or rows == None):
        break

    for row in rows:
        try:
            url_auto = row.find('a')
            img = row.find('img')

            auto = row.find('h3', attrs={'class': 'Text-sc-10o2fdq-0 fFalrS'})
            print(auto.text)

            preis = row.find('span', attrs={'class': 'Text-sc-10o2fdq-0 duCArz'})
            print(preis.text)
            auto = auto.text.replace(",", ".")
            preis= preis.text.replace("€ ", "€").replace(".", "").replace("€", "")

            pz = row.findAll('span', attrs={'class': 'Text-sc-10o2fdq-0 bspjoM'})
            pz = pz[1].text.replace("Ö", "Oe").replace("ö", "oe").replace(",","-")

            all_car = row.find('div', attrs={'class': 'Box-sc-wfmb7k-0 iqzkXU'})
            all_car2 = all_car.findAll('span', attrs={'class': 'Text-sc-10o2fdq-0 jZYJua'})

            ez = all_car2[0].text.replace(".", "")
            km = all_car2[1].text.replace(".", "")
            ps = all_car2[1].text.replace(".", "")

            url_auto = "https://www.willhaben.at/" + url_auto['href']
            autos.append({'car': auto, 'price': preis, 'pz': pz, 'ez': ez, 'km': km, 'ps': ps, 'url': url_auto, 'image': img['src']})
        except:
            pass
    i = i + 1

"""
for erstzulassung in range(2018, 2022):
    autos_filtered = [auto for auto in autos if auto['ez'] == erstzulassung]
    if len(autos_filtered) == 0:
        break
    print(autos_filtered)

    # Schreiben der Daten in eine Datei nach x*y sortiert
    autos_sorted = sorted(autos_filtered, key=lambda auto: sqrt((int(auto['price'])/1000)**2+(int(auto['km'])/10000)**2))
    with open(f"sorted_java.txt", 'a') as f:
        f.write("Autos von " + str(erstzulassung) + ": \n")
        for auto in autos_sorted:
            f.write(f"Marke: {auto['marke']}, Preis: {auto['price']}, km: {auto['km']}, PS: {auto['ps']}, PZ: {auto['pz']}, Url: {auto['url']}\n")
        f.write("\n")
    f.close()
"""

# Alle Autos sortiert
autos_sorted2 = sorted(autos, key=lambda auto: sqrt((int(auto['price'])/1000)**2+(int(auto['km'])/10000)**2))
"""
with open(f"sorted_java.txt", "a") as f:
    f.write("Alle Autos sortiert: \n")
    for auto in autos_sorted2:
        f.write(f"EZ: {auto['ez']}, Preis: {auto['price']}, Km: {auto['km']}, Marke: {auto['car']}, PS: {auto['ps']}, PZ: {auto['pz']}, Url: {auto['url']}\n")
f.close()
"""
#print(autos_sorted2)
#print("Time: ", time.time() - time1, "\n")
#print("Füge das in die Datenbank ein: \n")

time.sleep(2)

print("{'Autos':" + str(autos) + "} \n")
time.sleep(50)

