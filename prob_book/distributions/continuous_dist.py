from prob_book.distributions import base_dist

class ContinuousDist(base_dist.Distribution):
    def less_eq(self,x):
        return self.cdf(x)

    def less(self,x):
        return self.cdf(x)

    def greater_eq(self,x):
        return 1-self.cdf(x)

    def greater(self,x):
        return 1-self.cdf(x)