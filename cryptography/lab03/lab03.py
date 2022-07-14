from random import getrandbits
from sympy import *
from termcolor import colored
import time
import codecs
import math
import hashlib
wiadomoscPoOdszyfrowaniu = []
wiadomosc = '1234'


def nwd(a, b): return nwd(b, a % b) if b else a


def generowanieKlucza(bity):
    p = nextprime(getrandbits(bity))
    q = nextprime(getrandbits(bity))
    e = nextprime(getrandbits(256))
    n = p * q
    while p == q:
        q = nextprime(bity)

    Euler = (p - 1) * (q - 1)

    while nwd(Euler, e) != 1 or e == p or e == q or e > Euler:
        e = e + 1
        e = nextprime(e)

    d = mod_inverse(e, Euler)

    return n, e, d


def szyfrowanie(n, e, wiadomosc):
    cipher = []
    for i in range(len(wiadomosc)):
        tymczas = pow(ord(wiadomosc[i]), e, n)
        cipher.append(tymczas)

    return cipher


def deszyfrowanie(n, e, cipher, d):
    for i in range(len(cipher)):
        wiadomoscPoOdszyfrowaniu.append(chr(pow(cipher[i], d, n)))
    return wiadomoscPoOdszyfrowaniu


def validacja(wiadomoscPoOdszyfrowaniu):
    str1 = ''.join(str(e) for e in wiadomoscPoOdszyfrowaniu)
    if str1 == wiadomosc:
        print(colored('validacja pomyślna', 'green'))
        print('wiadomosc po odszyfrowaniu -->', str1)
    else:
        print(colored('zle', 'red'))
    return str1

def fdhszyfrowanie(d,n):
        m = hashlib.sha256()
        m.update(b"message")
        h = int(m.hexdigest(), 16)
        return pow(h, d, n)



def fdhwalidacja(sign,e,n):

        m = hashlib.sha256()
        m.update(b"message")
        h = int(m.hexdigest(), 16)
        if h == pow(sign, e, n):
            print("jest ok")
        else:
            print("nie jest ok")

def eksperyment1(wiadomosc, e, n, d):
    s = pow(int(wiadomosc), e, n)

    m2 = pow(s, e, n)

    odszyfrowanaWiadomosc = pow(m2, d, n)
    if s == odszyfrowanaWiadomosc:
        print(colored('validacja pomyślna', 'green'))
    return


def eksperyment2( e, n):
    wiadomosc1 = 1234
    wiadomosc2 = 45321
    wiadomosc = wiadomosc1 * wiadomosc2 % n

    s1 = pow(wiadomosc1, e, n)
    s2 = pow(wiadomosc2, e, n)

    s = s1 * s2 % n
    x = pow(wiadomosc, e, n)
    if s == x:
        print(colored('S == S', 'green'))
    return


def eksperyment3():

    e = 3
    cipher = 2829246759667430901779973875

    message = math.ceil(pow(cipher, 1 / e))
    decrypted = hex(message)
    decode_hex = codecs.getdecoder("hex_codec")
    sliced = decrypted[2:]
    string = decode_hex(sliced)[0]
    print(string)
    return


print("wiadomosc -->", wiadomosc)
start = time.time()
(n, e, d) = generowanieKlucza(1024)
(cipher) = szyfrowanie(n, e, wiadomosc)
print("szyfrogram -->", cipher)
(wiadomoscPoOdszyfrowaniu) = deszyfrowanie(n, e, cipher, d)
validacja(wiadomoscPoOdszyfrowaniu)
end = time.time()
elapsed = end - start
print(end - start, "s")

print("#############################")
print("")
print("eksperyment1")
eksperyment1(wiadomosc, e, n, d)
print("eksperyment2")
eksperyment2( e, n)
print("eksperyment3")
eksperyment3()

print("FDH")
(n, e, d) = generowanieKlucza(1024)
sign=fdhszyfrowanie(d,n)
fdhwalidacja(sign,e,n)
