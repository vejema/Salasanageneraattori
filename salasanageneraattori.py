# Tuodaan 'random' -moduuli satunnaisuuden toteuttamista varten
import random

# Tuodaan 'string' -moduuli salasanan merkkejä varten
import string


# Esitellään muuttujat
spec_chars = string.punctuation
alphabets = string.ascii_lowercase
numbers = string.digits
numbers_spec_chars = numbers + spec_chars
alphabets_numbers = alphabets + numbers
alphabets_spec_chars = alphabets + spec_chars
alphabets_numbers_spec_chars = alphabets + numbers + spec_chars

# Kerrotaan mitä ohjelma tekee ja pysäytetään sen suoritus kunnes painetaan 'Enter' -painiketta
print("### Tervetuloa salasanageneraattoriin ###")
print("\n")
print("Salasanageneraattorilla voi luoda eri tyyppisiä ja pituisia salasanoja sekä numerosarjoja.")
print("\n")
print("Kirjaimet:", alphabets)
print("Numerot:", numbers)
print("Erikoismerkit:", spec_chars)
print(
    "Salasanatyypit:\n1 = Vain kirjaimia 'dszkgfwcvt'\n2 = Kirjaimia sekä numeroita 'h7zmwydmd0'\n3 = Kirjaimia sekä erikoismerkkejä '_f[c+ynywm'\n4 = Kirjaimia, numeroita sekä erikoismerkkejä '9=.[g1^vlb'\n5 = Vain numeroita '5787291993'\n6 = Numeroita sekä erikoismerkkejä '!{!^]8$4`{'")
print("\n")
dump = input("Paina 'Enter' jatkaaksesi")

# Kysytään kriteerit salasanaan
count = int(input("Kuinka monta salasanaa generoidaan? "))
length = int(input("Syötä salasanan pituus: "))
type = int(input("Salasanatyyppi: "))

# Tehdään for-loop joka käy läpi salasanan tyypin ja sijoittaa 'password' -muuttujaan satunnaiset merkit annettujen kriteerien perusteella
for c in range(count):
    password = ""
    for l in range(length):

        # 1. tyyppi = Vain kirjaimia
        if type == 1:
            password += random.choice(alphabets)

        # 2. tyyppi = Kirjaimia sekä numeroita
        elif type == 2:
            password += random.choice(alphabets_numbers)

        # 3. tyyppi = Kirjaimia sekä erikoismerkkejä
        elif type == 3:
            password += random.choice(alphabets_spec_chars)

        # 4. tyyppi = Kirjaimia, numeroita sekä erikoismerkkejä
        elif type == 4:
            password += random.choice(alphabets_numbers_spec_chars)

        # 5. tyyppi = Vain numeroita
        elif type == 5:
            password += random.choice(numbers)

        # 6. tyyppi = Numeroita sekä erikoismerkkejä
        elif type == 6:
            password += random.choice(numbers_spec_chars)


# Tulostetaan salasana(t)
    print(password)
