import math
import logging
import numpy as np
from lark import Transformer
from lark import v_args
from prob_book.distributions import binomial,exponential,poisson,geometric,normal
from prob_book import main
from prob_book import extra_funcs

logger = logging.getLogger(__name__)

funcs = {
    "sin":{
        "n": 1,
        "func": lambda x: np.sin(x),
    },
    "cos": {
        "n": 1,
        "func": lambda x: np.cos(x),
    },
    "tan": {
        "n": 1,
        "func": lambda x: np.tan(x)
    },
    "B": {
        "n":2,
        "func":lambda n,p: binomial.Binomial(n,p)
    },
    "Geo": {
        "n":1,
        "func":lambda p: geometric.Geometric(p)
    },
    "N": {
        "n":2,
        "func":lambda mu,sig: normal.Normal(mu,sig)
    },
    "Po": {
        "n":1,
        "func":lambda x: poisson.Poisson(x)
    },
    "Exp": {
        "n":1,
        "func":lambda x: exponential.Exponential(x)
    },
    "Var":{
        "n":1,
        "func":lambda x: extra_funcs.variance(x)
    },
    "E":{
       "n":1,
        "func":lambda x:extra_funcs.expectation(x)
    },
    "Info":{
       "n":1,
        "func":lambda x:extra_funcs.info(x)
    }
}

@v_args(inline=True)
class EvalLine(Transformer):
    from operator import add,sub,mul,truediv as div,neg
    number = float

    def unpack_args(self,x):
        """
        Unpacks arguments from *args sent by lark and yields them
        :param x: The *args paramater
        """
        for val in x[0].children:
            yield val.children[0]

    def func_call(self,name,*args):
        """
        Handles functions calls from the program
        :param name: Name of the function
        :param args: Arguments to be used by the function
        :return: The value of the function called with the specified arguments
        """
        f = funcs[name]["func"]
        unpacked = []
        for val in self.unpack_args(args):
            unpacked.append(val)
        print(unpacked)
        return f(*unpacked)

    def tilde(self,name,dist):
        """
        Handles defining distributions with the tilde ("~") operator
        :param name: Name of the distribution
        :param dist: Object referring to the distribution
        :return: None
        """
        main.defined_dists[name] = dist
        main.defined_dists[name].name = name
        logger.info("Defined dist {} = {}".format(name, dist))

    def gen_arr(self,*args):
        """
        Generates arrays for the program using numpy arrays
        :param args: The values to be put into the array
        :return: The numpy array generated
        """
        # Get length of array to be generated
        n = len(args[0].children)
        arr = np.array([0.0 for _ in range(0,n)])

        for i,val in enumerate(self.unpack_args(args)):
            arr[i] = val

        return arr

    def find_dist(self,name):
        """
        Helper function to retrieve a given distriution by name
        :param name: Name of the distribution
        :return: Distribution object
        """
        try:
            dist = main.defined_dists[name]
        except KeyError:
            e = "No {} dist found".format(x)
            logger.error(e)
            raise ValueError(e)
        return dist

    def prob_eq(self,dist,val):
        return self.find_dist(dist).eq(val)

    def prob_gt(self,dist,val):
        return self.find_dist(dist).greater(val)

    def prob_gt_eq(self,dist,val):
        return self.find_dist(dist).greater_eq(val)

    def prob_lt(self,dist,val):
        return self.find_dist(dist).less(val)

    def prob_lt_eq(self,dist,val):
        return self.find_dist(dist).less_eq(val)

