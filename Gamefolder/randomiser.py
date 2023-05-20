import time

def lcgkumpul(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x = (a*x + c) %m
        r = (x % 6)  #menghasilkan nilai dari 0 sampai 5
        return r
    
def lcgbangun(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x = (a*x + c) %m
        r = (x % 5) + 1 #menghasilkan nilai dari 1 sampai 5
        return r

def randomnumbergenerator(lcg,i):
    seedvalue = int(time.time() * i) #i berfungsi untuk memvariasikan time dalam satu rangkain prosedur
    randomnumber = lcg(seedvalue)
    return randomnumber