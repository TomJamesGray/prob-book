class Poison:
    def __init__(self,mu):
        self.mu = mu

    def __repr__(self):
        return "<Poisson Distribution: Mu = {}>".format(self.mu)