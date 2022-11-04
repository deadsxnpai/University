import math
import random 

alphabet = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И",'Й',"К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"," "]


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

def generate_pq():
    minPrime = 10
    maxPrime = 100
    primes = [i for i in range(minPrime,maxPrime) if is_prime(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    if p != q:
        return (p, q)
    else:
        while q==p:
            q = random.choice(primes)
        return (p, q)

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randrange(1, n)
        g = gcd(e, phi)
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break

    return ((e,n),(d, n))

def decrypt(codes, private):
    res = ''
    d, n = private
    for i in range(len(codes)):
        ci = int(codes[i])
        mi = pow(ci, d, n)  
        res += alphabet[mi]
    return res

if __name__ == '__main__': 
    p, q = generate_pq()
    print('P and Q:',p,q)
    public, private = generate_keys(p, q)
    print('Public key is', public)
    print('Private key is', private)
    message = input("Enter a message: ").split(' ')
    print(message)
    #msg = [2775, 3291, 3188, 0, 2246, 918, 2246, 2880]
    #private = (1873,3763)
    print(decrypt(message,private))
