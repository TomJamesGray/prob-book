import math
import numpy as np
from prob_book.distributions import discrete_dist

def arr_fact(x):
    """
    Computes factorial for individual value of array
    :param x: Integer or array like object containing integers
    :return: Integer or numpy array of integers
    """
    if type(x) in (int,float):
        return math.factorial(x)
    else:
        rtn = np.array([0.0 for _ in range(0,len(x))])
        for i,y in enumerate(x):
            rtn[i] = math.factorial(y)
        return rtn


class Poisson(discrete_dist.DiscreteDist):
    def __init__(self,mu):
        self.mu = mu

    def __repr__(self):
        return "<Poisson Distribution: Mu = {}>".format(self.mu)

    def eq(self,x):
        return ((self.mu ** x) * math.e ** (-self.mu))/arr_fact(x)

    def var(self):
        return self.mu

    def expectation(self):
        return self.mu
