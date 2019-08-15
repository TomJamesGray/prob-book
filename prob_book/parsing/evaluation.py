import math
import logging
from lark import Transformer
from lark import v_args
from prob_book.distributions import binomial,exponential,poisson,geometric,normal
from prob_book import main

logger = logging.getLogger(__name__)

funcs = {
    "sin":{
        "n": 1,
        "func": lambda x: math.sin(x),
        "level": 5,
        "regex_name": "sin"
    },
    "cos": {
        "n": 1,
        "func": lambda x: math.cos(x),
        "level": 5,
        "regex_name": "cos"
    },
    "tan": {
        "n": 1,
        "func": lambda x: math.tan(x),
        "level": 5,
        "regex_name": "tan"},
    "B": {
        "n":2,
        "func":lambda n,p: binomial.Binomial(n,p)
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
            e = "No dist found for prob function with stmt {}".format(stmt)
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

