import math
import logging
import numpy as np
from lark import Transformer
from lark import v_args
from prob_book.distributions import binomial,exponential,poisson,geometric,normal
from prob_book import main
from prob_book.plotting import plot
from prob_book import extra_funcs
from prob_book import exceptions

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
    "range":{
        "n":(2,3),
        "func":lambda *args:np.arange(*args)
    },
    "pdf":{
        "n":2,
        "func":lambda dist,val:extra_funcs.pdf(dist,val)
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
        "func":lambda x: x.var()
    },
    "E":{
       "n":1,
        "func":lambda x:x.expectation()
    },
    "max":{
        "n":-1,
        "func":lambda *args:extra_funcs.max_f(*args)
    },
    "min":{
        "n":-1,
        "func":lambda *args:extra_funcs.min_f(*args)
    },
    "plot":{
        "n":-1
    },
    "bar":{
        "n":-1
    },
    "sum":{
        "n":-1,
        "func":lambda *args:extra_funcs.sum_f(*args)
    }
}

@v_args(inline=True)
class EvalLine(Transformer):
    from operator import add,sub,mul,truediv as div,neg
    number = float

    def __init__(self,*args,**kwargs):
        super(EvalLine,self).__init__(*args,**kwargs)
        self.plot = plot.Plot()

    def string(self,x):
        # Remove " from start and end of str
        return x[1:-1]

    def bool_t(self):
        return True

    def bool_f(self):
        return False

    def pow(self,x,y):
        return x**y

    def unpack_args(self,x):
        """
        Unpacks arguments from *args sent by lark and yields them
        :param x: The *args paramater
        """
        for val in x[0].children:
            if len(val.children) > 1:
                yield tuple([x for x in val.children])
            else:
                yield val.children[0]

    def func_call(self,name,*args):
        """
        Handles functions calls from the program
        :param name: Name of the function
        :param args: Arguments to be used by the function
        :return: The value of the function called with the specified arguments
        """
        unpacked = []
        for val in self.unpack_args(args):
            unpacked.append(val)

        if name == "plot":
            return self.plot.plot(*unpacked)
        elif name == "bar":
            return self.plot.bar(*unpacked)
        else:
            f = funcs[name]["func"]
            n = funcs[name]["n"]
            if type(n) == tuple:
                if len(unpacked) not in n:
                    raise exceptions.IncorrectNumberOfArgs("{} arguments supplied, should be {} arguments".format(
                        len(unpacked),n
                    ))
            elif n != -1 and n != len(unpacked):
                raise exceptions.IncorrectNumberOfArgs("{} arguments supplied, should be {} arguments".format(
                    len(unpacked), n
                ))
            return f(*unpacked)

    def tilde(self,name,dist):
        """
        Handles defining distributions with the tilde ("~") operator
        :param name: Name of the distribution
        :param dist: Object referring to the distribution
        :return: None
        """
        main.defined_vars[name] = dist
        main.defined_vars[name].name = name
        logger.info("Defined dist {} = {}".format(name, dist))

    def var_def(self,name,val):
        """
        Handles defining variables
        :param name: Variable name
        :param val: Value to be assigned
        :return: None
        """
        main.defined_vars[name] = val
        # logger.info("Defined var {} = {}".format(name, val))

    def get_var(self,name):
        """
        Retrieves variable
        :param name: Variable name
        :return: Varianble value
        """
        return main.defined_vars[name]

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
            dist = main.defined_vars[name]
        except KeyError:
            e = "No {} dist found".format(name)
            logger.error(e)
            raise ValueError(e)
        return dist

    def handle_dist(self,fn,val):
        """
        Handles evaluating functions where the argument could be an individual number or a list of numbers
        :param fn: Function
        :param val: Single number or iterable object containing numbers
        """
        if type(val) in (int,float):
            return fn(val)
        else:
            return [fn(x) for x in val]

    def prob_eq(self,dist,val):
        return self.handle_dist(self.find_dist(dist).eq,val)

    def prob_gt(self,dist,val):
        return self.handle_dist(self.find_dist(dist).greater, val)

    def prob_gt_eq(self,dist,val):
        return self.handle_dist(self.find_dist(dist).greater_eq, val)

    def prob_lt(self,dist,val):
        return self.handle_dist(self.find_dist(dist).less, val)

    def prob_lt_eq(self,dist,val):
        return self.handle_dist(self.find_dist(dist).less_eq, val)


def extract_kw_args(args):
    """
    Extracts KW args and turns them into a dictionary
    :param args: 2d tuple of form ((TOKEN,VALUE),..)
    :return: Dictionary with key being token data and value being the value
    """
    d = {}
    for child in args:
        if len(child) == 2:
            d[child[0].value] = child[1]

    return d