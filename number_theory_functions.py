from random import randrange
import time
from math import sqrt,floor
def __extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    # Base Case
    if a == 0:
        return b, 0, 1

    d, x1, y1 = __extended_gcd(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return d, x, y
def extended_gcd(a,b):
    if (a==0 and b==0):
        raise Exception("gcd(0,0) is undefined")
    (d,x,y) = __extended_gcd(a,b)
    sign_d = abs(d)/d

    return sign_d*d,sign_d*x, sign_d*y



def modular_inverse(a,n):
    """
       Returns the inverse of a modulo n if one exists

       Parameters
       ----------
       a : Input data.
       n : Input data.

       Returns
       -------
       x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
       """
    gcd_res = extended_gcd(a,n)
    if  gcd_res[0] != 1:
        return None
    if gcd_res[1]>0:
        return gcd_res[1]%n
    return (n+gcd_res[1])%n



def __modular_exponent(a, d, n):
    """
       Returns a to the power of d modulo n

       Parameters
       ----------
       a : The exponential's base.
       d : The exponential's exponent.
       n : The exponential's modulus.

       Returns
       -------
       b: such that b == (a**d) % n
       """

    d_bin = bin(d)[2:]
    d_bin = d_bin[::-1]
    res=1
    a = a%n
    for i,x in enumerate(d_bin):
        if x == "0":
            continue
        b = int(x,2)
        modi = 2**(i)
        tmp = a**(b*modi)
        tmp = tmp%n
        res *= tmp
    res = res%n
    return res
def modular_exponent(a,d,n):
    divnum = floor(sqrt(d))
    res =1
    for i in range(divnum):
        res *= __modular_exponent(a,d//divnum,n)
        res = res % n
    res *= __modular_exponent(a,d%divnum,n)
    return res %n

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None

if __name__ == '__main__':
    # unittest.main()
    a = 5279
    b = -797
    r = lambda x: 1e6 * x
    d, x, y = list(map(r,extended_gcd(a, b)))
    print(d == 1e6)
    print(d == a*x+b*y)
    m = 23539673
    n = 3434462
    base = 1000
    st = time.time()
    print(modular_exponent(m,n,base))
    print(time.time()-st)

