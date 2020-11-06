from random import randrange

def extended_gcd(a,b):
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
    if a == 0 and b == 0:
        raise Exception
    # if a == 0 or b == 0:
        # TODO: support negative numbers
        # a_abs = abs(a)
        # b_abs = abs(b)
        # return (max(a_abs,b_abs), a>b, b>a)

    if a>b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a

    quotient, remainder, x, y, iteration = -1, -1, 1, 1, 1

    while remainder != 0:
        quotient, remainder = divmod(bigger, smaller)
        if (remainder != 0):
            if (iteration == 1):
                x = veryOldX = 1
                y = veryOldY = -1*quotient

            elif (iteration == 2):
                oldX = x = -1*quotient
                oldY = y = 1 - quotient

            else:
                    x = veryOldX - quotient*oldX
                    y = veryOldY - quotient*oldY
                    veryOldX, veryOldY = oldX, oldY
                    oldX, oldY = x, y

        bigger = smaller
        smaller = remainder
        iteration += 1
    gcd = smaller
    print(f'{gcd}, {x}, {y}')




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


def modular_exponent(a, d, n):
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