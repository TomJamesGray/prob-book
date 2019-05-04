from prob_book.distributions import base_dist


class Poison(base_dist.Distribution):
    def __init__(self,mu):
        self.mu = mu

    def __repr__(self):
        return "<Poisson Distribution: Mu = {}>".format(self.mu)
