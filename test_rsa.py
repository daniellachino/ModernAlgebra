import unittest
import number_theory_functions
from rsa_functions import RSA

class TestNumberTheory(unittest.TestCase):
    def test_extended_gcd(self):
        values = [(119952, 34425, 153),
                 (428848, 123075, 547),
                  (-39,3, 3)
                 ]
        for (a,b,d) in values:
            (gcd,x,y) = number_theory_functions.extended_gcd(a,b)
            self.assertEqual(d, gcd)
            self.assertEqual(gcd, a*x+b*y)

    def test_modular_inverse(self):
        values = [(17,81),
                  (50,137)
                  ]
        for (a,n) in values:
            x = number_theory_functions.modular_inverse(a,n)
            self.assertEqual(1, (a * x) % n)
            self.assertEqual((x % n), x)

        self.assertIsNone(number_theory_functions.modular_inverse(119952,34425))

class TestRSA(unittest.TestCase):
    def test_encrypt_decrypt(self):
        rsa = RSA.generate(10)
        plaintexts = [123456789,17,9999, 102930]
        for M in plaintexts:
            C = rsa.encrypt(M)
            MM = rsa.decrypt(C)
            self.assertEqual(M,MM)

if __name__ == '__main__':
    a = 5279
    b = -797
    r = lambda x: 1*x
    d,x,y = map(r,number_theory_functions.extended_gcd(a, b))
    print(f"{d} = {x}a + {y}b ")
    print(f"Iron man will give  {x} million bills and loki will give back {y} coins")
    N = 12215009
    e = 3499
    d = 5425399
    rsa = RSA((N,e),(N,d))
    m = 42
    print(rsa.decrypt(rsa.encrypt(m)))
    unittest.main()


