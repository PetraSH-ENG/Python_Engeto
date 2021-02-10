# texty
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# formatovani
oddelovac = ("=" * 35)

# uvitani
print(oddelovac)
print("Vitej uzivateli do Text Analyzer!")
print(oddelovac)

print("Na vyber mame nasledujici prihlasovaci udaje:")
print("1 - bob   | 123", "2 - ann   | pass123", "3 - mike  | password123", "4 - liz   | pass123", sep='\n')
print(oddelovac)

# prihlaseni
jmeno = input("Zadej sve prihlasovaci jmeno:")
male_jmeno = jmeno.lower()  # jen mala pismena
print("Prihlasovaci jmeno:", male_jmeno)  # jen mala pismena
heslo = input("Zadej sve heslo:")
print("Prihlasovaci heslo:", heslo)

# overeni
udaje = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
if udaje.get(jmeno) != heslo:
    print("Ukonceno, nespravne jmeno nebo heslo!")
    print(oddelovac)
    quit()
else: print("Jste prihlasen/a, pokracujeme dale!")

print(oddelovac)

# vyber textu
print("Vyber jeden ze tri textu.")
vyber = int(input("Vyber cislo 1 az 3:"))
   if vyber == 1 or vyber == 2 or vyber == 3:
        print("Vybrany text c.:", vyber)
    else:
        print ("Ukonceno, chybne cislo!")
        quit()

vybrany = TEXTS[vyber -1]
print("Vybrany text c.:", vyber)
print(oddelovac)

# cisteni textu
slova = vybrany.split()
jen_slova = []

while slova:
    slovo = slova.pop()
    slovo = slovo.strip('.,')
    if slovo: jen_slova.append(slovo)
pocet_slov = len(jen_slova)


# pocitadlo
velke_prvni = 0
velka_pismena = 0
mala_pismena = 0
cisla = 0
pocet = {}
soucet = 0

a = 0
while a < len(jen_slova):
    if jen_slova[a].istitle():
        velke_prvni = velke_prvni + 1

    elif jen_slova[a].isupper():
        velka_pismena = velka_pismena + 1

    elif jen_slova[a].islower():
        mala_pismena = mala_pismena + 1

    elif jen_slova[a].isnumeric():
        cisla = cisla + 1
        soucet = soucet + int(jen_slova[a])

    p = len(jen_slova[a])
    pocet[p] = pocet.get(p, 0) + 1

    a = a + 1

pocet_slov = len(jen_slova)
print("V textu c.", vyber, "je", pocet_slov, "slov celkem.")
print("V textu c.", vyber, "je", velke_prvni, "slov zacinajici velkym pismenem.")
print("V textu c.", vyber, "je", velka_pismena, "slov psanych velkymi pismeny.")
print("V textu c.", vyber, "je", mala_pismena, "slov psanych malymi pismeny.")
print("V textu c.", vyber, "je", cisla, "cisel.")
print("Soucet vsech cisel v textu c.", vyber,  "je:", str(soucet))
print(oddelovac)

# graf
print("pocet slov dle jejich delky:")

pismena = sorted(pocet)
a = 0
while a < len(pismena):
    delka = pismena[a]
    frequency = pocet[delka]
    if len(str(delka)) == 1:
        str_len = ' ' + str(delka)
    else:
        str_len = str(delka)
    print(str_len, '~' * frequency, frequency)
    a = a + 1

# konec
print(oddelovac)
print("KONEC ANALYZATORU, DEKUJEME ZA SPOLUPRACI!")
print(oddelovac)
