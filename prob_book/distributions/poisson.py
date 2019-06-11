from prob_book.distributions import base_dist
import math


class Poison(base_dist.Distribution):
    def __init__(self,mu):
        self.mu = mu

    def __repr__(self):
        return "<Poisson Distribution: Mu = {}>".format(self.mu)

    def eq(self,x):
        return ((self.mu ** x) * math.e ** (-self.mu))/math.factorial(x)

    def less_eq(self,x):
        return sum([self.eq(y) for y in range(0,int(x+1))])

    def greater_eq(self,x):
        return 1-self.less_eq(x-1)