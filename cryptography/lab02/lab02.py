import random
from sympy import *
import time

M = 12321342145213421512521352345435342534435354672345673573462347345623623747786923476583412678543267834267923467892346794327623467983246789678293468723486754238675234# sekret
p=''
W = []  # wartości cienia po obliczeniu

print('Podaj ilosc cieni: ')
n = int(input())

print('Podaj wartosc progowa: ')
m = int(input())

def modInverse(a, n):#stack i przyjaciele
    b, c = 1, 0
    while n:
        q, r = divmod(a, n)
        a, b, c, n = n, c, b - q * c, r
    # at this point a is the gcd of the original inputs
    if a == 1:
        return b
    raise ValueError("Not invertible")

def tworzenieCieni():
    taba = []# tablica z losowymi współczynnikami
    for i in range(0, m-1):
        taba.append(random.randint(0, 1232134214521342151252135234543534253443535467234567357346234734562362374))
    sum = 0
    for x in range(1, n + 1):
        for i in range(1, m):
            sum = sum + (taba[m - 1 - i] * pow(x, m - i))

        W.append((sum + M) % int(p))
        sum = 0

    for i in range(len(W)):
        print("Wartość cienia", i + 1, " = ", W[i])
    return

def sekret(W):
    mnozenie = 1
    dodawanie = 0
    for k in range(0, m):
        for i in range(0, m):
            if ((k != i)):
                mnozenie = mnozenie * ((-(i+1) * mod_inverse((k+1) - (i+1), int(p))))
        dodawanie = dodawanie + (W[k] * mnozenie)
        mnozenie = 1
    return dodawanie % p

def createModule(n):
    return nextprime(n)

print("Sekret",M)
tic = time.perf_counter()
p=createModule(M)#moduł przekształcenia czyli kolejna liczba pierwsza

tworzenieCieni()
print("Policzony sekret",sekret(W))
toc = time.perf_counter()
print(f"POLICZONO W {toc - tic:0.4f} seconds")
