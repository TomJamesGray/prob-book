from prob_book.distributions import base_dist

class DiscreteDist(base_dist.Distribution):
    def less_eq(self,x):
        return sum([self.eq(y) for y in range(0,int(x+1))])

    def greater_eq(self,x):
        return 1-self.less_eq(x-1)

    def greater(self,x):
        return 1-self.less_eq(x)

    def less(self,x):
        return self.less_eq(x-1)