from Crypto.Cipher import AES
from Crypto import Random
import random
import time
import datetime
p=2
random_gen = Random.new()
key = random_gen.read(16)
print("Kacper Lukasiewicz gr2A PADDING ATTACK")
tekstJawny = b"Kryptologia semestr letni 2020/2021, po raz trzeci zdalnie, czy ostatni???"
print("tekst jawny --> ",tekstJawny)

###########################################################################################źródło:https://github.com/jjcomline/padding-oracle-attack/blob/master/oracle.py
def dodaniePaddingu(tekstJawny):
    pad_len = AES.block_size - (len(tekstJawny) % AES.block_size)
    padding = bytes([pad_len]) * pad_len
    return tekstJawny + padding


def szyfrowanie(tekstJawny):
    iv = random_gen.read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(dodaniePaddingu(tekstJawny))


def zdekryptowanie(data):
    iv = data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return usuwaniePaddingu(cipher.decrypt(data[AES.block_size:]))


def usuwaniePaddingu(data):
    pad_len = data[-1]

    if pad_len < 1 or pad_len > AES.block_size:
        return None
    for i in range(1, pad_len):
        if data[-i - 1] != pad_len:
            return None
    return data[:-pad_len]


def wyrocznia(data):
    return zdekryptowanie(data) is not None


###########################################################################################

wynikSzyfrowania = szyfrowanie(tekstJawny)  # zaszyfrowanie tekstu jawnego
print(wynikSzyfrowania)
blocks = [wynikSzyfrowania[i:i + AES.block_size] for i in


          range(0, len(wynikSzyfrowania), AES.block_size)]  # podzielenie szyfru na bloki o długośći 16 bajtów
tablicaBajtów = []

for i in range(len(blocks)):  # pętla przetwarzająca bloki dziwnych znaków na tablice bajtów
    for j in blocks[i]:
        tablicaBajtów.append(j)

print("tablica bajtów -->  ", tablicaBajtów)


blocks = [tablicaBajtów[i:i + AES.block_size] for i in
          range(0, len(tablicaBajtów), AES.block_size)]  # podział tablicy bajtów na bloki z bajtami


def przygotowanieC1prim(index, i2):  #
    c1prim = []
    for i in range(0, 16):  # pętla wypełniająca
        c1prim.append(random.randint(0, 255))

    for i in range(0, index - 1):  # wypełnia za zerami liczbami
        miejsce = 16 - i - 1
        c1prim[miejsce] = index ^ i2[miejsce]
    return c1prim


wynikXor = [0] * 16
odczytaneBloki = [0] * len(blocks)


def intToString(data):#internet stack
    slowo = ""

    for i in range(len(data)):
        if (data[i] > 31):
            slowo = slowo + chr(data[i])
    return slowo


def atak():
    c = []
    tymczas = [0] * 16

    for z in (range(p,len(blocks))):  # pętla idzie po blokach
        for k in range(1, 17):  # pętla idzie po bajtach w bloku
            c1prim = przygotowanieC1prim(k, tymczas)
            for i in range(0, 256):  # pętla zmnienająca ostatni bajt tablicy na wartosc z przedziału 0-255
                c1prim[16 - k] = i
                c = c1prim + blocks[z]  # konkatenacja tablicy przedostatniej z losowymi znakami i ostatniej
                if wyrocznia(bytearray(c)):
                    tymczas[16 - k] = k ^ i
                    wynikXor.append(tymczas[16 - k] ^ blocks[z - 1][16 - k])

start = datetime.datetime.now()
atak()
end = datetime.datetime.now()
elapsed = end - start
wynikXor.reverse()

odszyfrowaneBloki = [wynikXor[i:i + AES.block_size] for i in range(0, len(wynikXor), AES.block_size)]#podział na bloki

print("")
# wyswietlenie odszyfrowanych blokow (odworenie bloków)
print("Odszyfrowane bloki:")
for i in reversed(range(len(odszyfrowaneBloki))):  # usuniecie bloku z vektorem inicjalizującemy
    a = intToString(odszyfrowaneBloki[i])

    print(a)

print(elapsed.microseconds/10000,"ms")