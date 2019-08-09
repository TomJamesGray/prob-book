from prob_book.distributions import discrete_dist

class Geometric(discrete_dist.DiscreteDist):
    def __init__(self,p):
        self.p = p

    def __repr__(self):
        return "<Geometric Distribution: P = {}>".format(self.p)

    def eq(self,x):
        if x != int(x):
            raise ValueError("Geometric distribution can only be equal to integer values")
        if x == 0:
            return 0
        return (1-self.p) ** (x-1) * self.p

    def var(self):
        return ((1-self.p) / (self.p ** 2))
