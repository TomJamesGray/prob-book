import logging
from prob_book import main
from prob_book import parsing

logger = logging.getLogger(__name__)

def define(x,y):
    if type(x) == str and x not in parsing.functions:
        logger.info("Defining var {} as {}".format(x,y))
        main.defined_vars[x] = y
    elif type(x) != str:
        raise ValueError("Variable name of type {} not str".format(type(x)))
    else:
        raise ValueError("Variable name {} invalid as it is a reserved function name".format(x))

def pdf(dist,val):
    if hasattr(dist,'pdf'):
        return dist.pdf(val)
    else:
        raise ValueError("Distribution {} has no pdf".format(dist))

def sum_f(*args):
    tot = 0
    for val in args:
        if type(val) in (float,int):
            tot += val
        elif hasattr(val,"__iter__"):
            tot += sum(val)
        else:
            raise ValueError("Value {} isn't numeric or iterable")

    return tot
