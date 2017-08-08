'''
For KIT103/KMA115 Practical 7: Euclidean Algorithms and Applications
Revised: 2016-09-09
Author: James Montgomery (james.montgomery@utas.edu.au)

Multiplicative encryption and decryption functions to illustrate
how they work. Can you see a way of having greater code reuse and
a shorter implementation of decrypt?

Has strings for lowercase and uppercase roman alphabet characters
defined for convenience.
'''

from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_lowercase[:26]
ALPHABET = ascii_uppercase[:26]

def mult(s, key, size):
    return (s * key) % size

def encrypt(message, key, symbols):
    '''Encrypts the given message using the given key;
    only characters in symbols are kept and encrypted.'''
    ciphertext = ''
    for c in message:
        if c in symbols:
            cIndex = symbols.find(c)
            ciphertext += symbols[ mult(cIndex, key, len(symbols)) ]
    return ciphertext

def decrypt(cipher, key, symbols):
    '''Decrypts the given encrypted message using
    the given original encryption key.'''
    kinv = mod_inverse(key, len(symbols))
    if kinv is None:
        print('Unable to decrypt message as key', key,\
            'and number of symbols', len(symbols), 'are not coprime')
    else:
        messagetext = ''
        for c in cipher:
            cIndex = symbols.find(c)
            messagetext += symbols[ mult(cIndex, kinv, len(symbols)) ]
        return messagetext
        

def mod_inverse(a, b):
    '''Calculates and returns the multiplicative inverse of a mod b.
    Returns None if gcd(a, b) is not 1.'''
    u,v, x,y = 1,0, 0,1
    while a != 0:
        q, r = divmod(b, a)
        b, a = a, r
        m,n = x - u*q, y - v*q
        x,y, u,v= u,v, m,n
    if b == 1: #at this point b = gcd(a, b)
        return x
    return None