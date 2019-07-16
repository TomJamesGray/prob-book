from prob_book.distributions import continuous_dist
import math
import logging

logger = logging.getLogger(__name__)

def phi(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

class Normal(continuous_dist.ContinuousDist):
    def __init__(self,mu,var):
        self.mu = mu
        self.var = var

    def __repr__(self):
        return "<Normal Distribution: Mu = {}, Var = {}>".format(self.mu,self.var)

    def cdf(self,x):
        return phi((x-self.mu)/math.sqrt(self.var))

