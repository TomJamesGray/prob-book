from prob_book.distributions import base_dist
import math


def nCr(n,r):
    return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))

class Binomial(base_dist.Distribution):
    def __init__(self,n,p):
        self.n = n
        self.p = p

    def __repr__(self):
        return "<Binomial Distribution: N = {}, P = {}>".format(self.n,self.p)

    def eq(self,x):
        if x != int(x):
            raise ValueError("Binomial distribution can only be equal to integer values")
        return nCr(self.n,x) * self.p ** x * (1-self.p) ** (self.n - x)