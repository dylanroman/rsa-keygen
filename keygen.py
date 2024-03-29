#Imports
import random
from math import sqrt

#Used for Key Generator Function
#Extended Euclidean Algorithm
def euclidean(x, y):
    #Checks to see if formula can be used
    if x == 0:
        return (y, 0, 1)
    #Runs values through extended euclidean algorithm
    #Note // uses floor division, it find the nearest integer, gets rid of decimal
    gcd, b, a = euclidean(y % x, x)
    return (gcd, a - (y // x) * b, b)

#Inverse Mod
def invMod(x, mod):
    gcd, a, b = euclidean(x, mod)
    #Mod DNE
    return a % mod

#Prime Number Checker
def prime (n):
    #Checks if "n" number is larger than 2, or is divisible by 2
    if n <= 1:
        return False
    if n == 2:
        return True
    if (n % 2) == 0:
        return False
    #Checks to see if "n" number is divisible by any number besides 1 and "n" number
    i = 2
    while i <= (sqrt(n)):
        if n % i == 0:
            return False
        i = i + 1
    return True

#Prime Number Generator
def primeGen (min, max):
    #Generates random baseline number
    primeNum = random.randrange(min, max)
    #Adds 1 to baseline number until number is prime
    while True:
        if prime(primeNum) == True:
            return primeNum
        primeNum = primeNum + 1




#Key Generator
#generator limits
lim1 = 10000
lim2 = 15000
def keyGen():
    #Generate two random primes
    p1 = primeGen(lim1, lim2)
    p2 = primeGen(lim1, lim2)
    #Phi
    phi = (p1 - 1) * (p2 - 1)
    #Public Keys
    pubKey2 = p1 * p2
    pubKey1 = random.randrange(3, 15)
    if pubKey1 % 2 == 0:
        pubKey1 = pubKey1 + 1
    #Loop pubKey 1 generator until a useable key is generated
    goodKey = False
    while goodKey == False:
        if phi % pubKey1 != 0:
            goodKey = True
            break
        pubKey1 += 2
    #Public Key
    privKey = invMod(pubKey1, phi)
    #Output keys
    keys = [pubKey1, pubKey2, privKey]
    return keys

##Using a key generator is important because in order for RSA to work only specific key combinations work when reversing the ecrypted code
##Keys are outputted in this function via list, however it can be adapted into a class easily by making each index in the list an output to an @route, this is just a quick fix to the lack of a key generator on my original class function
##In order to use RSA, public Key 1 and Public Key 2 are used to encrypt, Public Key 1 and Private Key are used to decrypt