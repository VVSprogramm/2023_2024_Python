#Datu kriptēšana

from cryptography.fernet import Fernet

atslega = Fernet.generate_key()

print(atslega)

a = Fernet(atslega) #Objekta izveide

teksts = b'slepeni dati'

kriptDati = a.encrypt(teksts) #Metodes encrypt izmantošana

print(kriptDati)

print(a.decrypt(kriptDati)) #Metodes decrypt izmantošana

