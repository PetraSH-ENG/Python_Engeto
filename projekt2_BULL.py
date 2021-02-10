# formatovani
import random
oddelovac = '=' * 40

# uvod
print("Vitejte v nasi hre BYCI & KRAVY!".center(30, ' '))
print(' ')
print("""Mame pro Vas nahodne vygenerovane
 4-mistne cislo a Vasim ukolem je 
 ho uhodnout v co nejkratsim case.""".center(40, ' '))
print(oddelovac)
print("PRAVIDLA:".center(40, ' '))
print("""
~ Napiste 4-mistne cislo, ale
    * cislice se nemuzou opakovat
    * cislo nemuze zacinat 0
~ Pokud jste uhodli cislo, tak
    * na spravne pozici je to BYK
    * na spatne pozici je to KRAVA""")
print(oddelovac)


# hlavni
def main():
    cislo = gen_cislo(4)
    pokus = 0
    while True:
        odhad = input("Napiste cislo, ktere hadate:")
        pokus += 1
        if spatne(odhad):
            continue
        byk, krava = soucet(odhad, cislo)
        if konec_hry(byk, krava, pokus):
            break


# generovani cisla
def gen_cislo(length):
    number = ''
    while len(set(number)) != length or number[0] == 0:
        number = str(random.randint(1000, 9999))
    return number


# overeni cisla
def spatne(input):
    hadam = False
    if not input.isdecimal() or len(input) != 4:
        print("Musite hadat 4 cislice, znovu, prosim!")
        hadam = True

    elif input[0] == '0':
        print("Cislo nesmi zacinat 0, znovu, prosim!")
        hadam = True

    elif len(set(input)) != 4:
        print("Cislice se nesmi opakovat, znovu prosim!")
        hadam = True
    return hadam


# hodnoceni
def soucet(inpt, generovano):

    byk = krava = 0
    for index, num in enumerate(inpt):
        if num == generovano[index]:
            byk += 1
        elif num in generovano:
            krava += 1
    return byk, krava


# konec hry
def konec_hry(byk, krava, pokus):
    stav = '| {} x BYK | {} x KRAVA | {} x POKUS |'
    konec_hry = False
    if byk == 4:
        suffix = '' if pokus > 1 else ''
        print(oddelovac, '\n', "KONEC!", '\n', "Uhodnuto po %d pokusech.%s"
              % (pokus, suffix))
        print(" To %s" % (evaluation(pokus)), end='\n\n')
        konec_hry = True

    else:
        print(stav.format(byk, krava, pokus))
    return konec_hry


def evaluation(pokusy):
    if pokusy <= 5: return "bylo skvele!"
    if pokusy <= 10: return "bylo dobre!"
    else: return "by slo i lepe."

main()