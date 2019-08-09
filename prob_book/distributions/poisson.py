from prob_book.distributions import discrete_dist
import math


class Poison(discrete_dist.DiscreteDist):
    def __init__(self,mu):
        self.mu = mu

    def __repr__(self):
        return "<Poisson Distribution: Mu = {}>".format(self.mu)

    def eq(self,x):
        return ((self.mu ** x) * math.e ** (-self.mu))/math.factorial(x)

    def var(self):
        return self.mu

    def expectation(self):
        return self.mu
