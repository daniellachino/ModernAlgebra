from number_theory_functions import *
from math import ceil
class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        p =generate_prime(digits//2)
        q = generate_prime(ceil(digits/2))
        N = p*q
        phi_N = (p-1)*(q-1)
        N_digits = len(bin(N)[2:])
        e = generate_prime(floor(sqrt(N_digits)))
        while(extended_gcd(e,(phi_N))[0] != 1):
            e = generate_prime(int(floor(sqrt(N_digits))))

        d = modular_inverse(e,phi_N)
        public_key = (N,e)
        private_key = (N,d)
        return RSA(public_key, private_key)








    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        N = self.public_key[0]
        e = self.public_key[1]

        c = modular_exponent(m,e,N)
        return c


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        N = self.public_key[0]
        d = self.private_key[1]

        m = modular_exponent(c, d, N)
        return m

