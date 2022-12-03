import random 

class A:
    def __init__(self, key, n):
        self.key = key
        #self.key = 0
        self.n = n

    def gen_random_r(self):
        self.r = random.choice(range(1, self.n-1))
        print(f'random r - {self.r}')
        self.z = self.r*self.r % self.n

    def send_z(self):
       
        return self.z

    def check_bit(self, bit):
        if bit == 0:
            print(f'return r - {self.r}')
            return self.r
        if bit == 1:
            self.y = self.r * self.key % self.n
            print(f'return y - {self.y}')
            return self.y

class B:
    def __init__(self, key, n):
        self.n = n
        self.key = key
         
    def send_random_bit(self):
        numbers = [0,1]
        self.choice = random.choice(numbers)
        return self.choice

    def get_z(self, z):
        print(f'z - {z}')
        self.z = z

    def check_answer(self, r, y):
        if self.choice == 0:
            z = r*r % self.n
            print(f'z in func with 0 - {z}')
            if z == self.z: 
                return True
            else:
                return False
        if self.choice == 1:
            z = (y*y*self.key) % self.n
            print(f'z in func with 1 - {z}')
            if z == self.z: 
                return True
            else:
                return False


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

def generate_pq():
    minPrime = 4
    maxPrime = 8
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
    x = 1
    v_list = list()
    while x <= n:
        v = x*x % n
        v_list.append(v)
        x+=1
    v_list = list(set(v_list))
    dictionary = {}
    for i in v_list:
        for j in range(1, n):
            if i*j % n == 1:
                dictionary.update({i:j})
    
    v = random.choice(list(dictionary.values()))
    rv = dictionary[v]
    value = 0
    while True:
        if value * value % n == rv:
            s = value
            break
        value += 1
    print(f'N - {n}')
    print(f'Public key - {v}')
    print(f'Private key: {s}')
    print('---------------------')

    return n, v, s

def get_keys():
    p, q = generate_pq()
    n,v, s = generate_keys(p, q)
    return n, v, s        

def main():
    n, v, s = get_keys()
    a1 = A(s, n)
    b1 = B(v, n)
    t = 0
    while t != 10:
        a1.gen_random_r()
        b1.get_z(a1.send_z())
        bit = b1.send_random_bit()
        print(f'bit: {bit}')
        answer = b1.check_answer(a1.r, a1.check_bit(bit))
        print(f'answers:{answer}')
        print('---------------------')
        t += 1
  

if __name__ == '__main__':
    main()