from prob_book.distributions import continuous_dist
import math
import logging

logger = logging.getLogger(__name__)

def phi(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2


class Normal(continuous_dist.ContinuousDist):
    def __init__(self,mu,var):
        self.mu = mu
        self._var = var

    def __repr__(self):
        return "<Normal Distribution: Mu = {}, Var = {}>".format(self.mu,self._var)

    def cdf(self,x):
        return phi((x-self.mu)/math.sqrt(self._var))

    def pdf(self,x):
        return (1 / math.sqrt(2 * math.pi * self._var)) * math.e ** ((-(x-self.mu) ** 2)/(2 * self._var))

    def var(self):
        return self._var

    def expectation(self):
        return self.mu
