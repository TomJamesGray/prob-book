from prob_book.distributions import base_dist
import math
import logging

logger = logging.getLogger(__name__)

def phi(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

class Normal(base_dist.Distribution):
    def __init__(self,mu,var):
        self.mu = mu
        self.var = var

    def __repr__(self):
        return "<Normal Distribution: Mu = {}, Var = {}>".format(self.mu,self.var)

    def normalise(self,x):
        return (x-self.mu)/math.sqrt(self.var)

    def less_eq(self,x):
        return phi(self.normalise(x))

    def less(self,x):
        return phi(self.normalise(x))

    def greater_eq(self,x):
        return 1-phi(self.normalise(x))

    def greater(self,x):
        return 1-phi(self.normalise(x))