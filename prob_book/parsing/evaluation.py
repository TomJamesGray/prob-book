import math
import logging
from lark import Transformer
from lark import v_args
from prob_book.distributions import binomial,exponential,poisson,geometric,normal
from prob_book import main
from prob_book import extra_funcs

logger = logging.getLogger(__name__)

funcs = {
    "sin":{
        "n": 1,
        "func": lambda x: math.sin(x),
    },
    "cos": {
        "n": 1,
        "func": lambda x: math.cos(x),
    },
    "tan": {
        "n": 1,
        "func": lambda x: math.tan(x)
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

    def func_call(self,name,*args):
        f = funcs[name]["func"]
        unpacked = []
        for val in args[0].children:
            unpacked.append(val.children[0])
        print(unpacked)
        return f(*unpacked)

    def tilde(self,name,dist):
        main.defined_dists[name] = dist
        main.defined_dists[name].name = name
        logger.info("Defined dist {} = {}".format(name, dist))

    def find_dist(self,name):
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

