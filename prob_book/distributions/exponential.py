from prob_book.distributions import continuous_dist
import logging
import math

logger = logging.getLogger(__name__)

class Exponential(continuous_dist.ContinuousDist):
    def __init__(self,mu):
        self.mu = mu

    def __repr__(self):
        return "<Exponential Distribution: Mu = {}>".format(self.mu)

    def cdf(self,x):
        if x < 0:
            return 0
        return 1-math.exp(-self.mu * x)

    def var(self):
        return self.mu ** (-2)

    def expectation(self):
        return 1/self.mu
