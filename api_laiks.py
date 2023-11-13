#Laika noteikšana

import requests

#Latvijas laika pieprasīšana
URL = "https://worldtimeapi.org/api/timezone/Europe/Riga"

dati = requests.get(URL)
# print(dati)
laiksLatvija = dati.json()
# print(laiksLatvija)
print(laiksLatvija["datetime"])

#ASV laiks, Ņujorka
URL2 = "https://worldtimeapi.org/api/timezone/America/New_York"
dati2 = requests.get(URL2)
#print(dati2)
laiksNewYork = dati2.json()
print(laiksNewYork)
print(laiksNewYork["datetime"])