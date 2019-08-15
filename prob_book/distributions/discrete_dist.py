import math

class DiscreteDist():
    def less_eq(self,x):
        if int(x+1) < 0:
            return 0
        return sum([self.eq(y) for y in range(0,int(x+1))])

    def greater_eq(self,x):
        return 1-self.less_eq(x-1)

    def greater(self,x):
        return 1-self.less_eq(x)

    def less(self,x):
        if x <= 0:
            return 0
        return self.less_eq(math.ceil(x)-1)