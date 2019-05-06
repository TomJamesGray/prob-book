from prob_book.distributions import base_dist
import math


class Poison(base_dist.Distribution):
    def __init__(self,mu):
        self.mu = mu

    def __repr__(self):
        return "<Poisson Distribution: Mu = {}>".format(self.mu)

    def eq(self,x):
        return ((self.mu ** x) * math.e ** (-self.mu))/math.factorial(x)
