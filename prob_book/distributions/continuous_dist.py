from prob_book.exceptions import EqualityForCtsDist

class ContinuousDist():
    def less_eq(self,x):
        return self.cdf(x)

    def less(self,x):
        return self.cdf(x)

    def greater_eq(self,x):
        return 1-self.cdf(x)

    def greater(self,x):
        return 1-self.cdf(x)

    def eq(self,_):
        raise EqualityForCtsDist("Equality operation for continutous distribution can't exist")