import logging
from prob_book import main
from prob_book import parsing

logger = logging.getLogger(__name__)

def variance(dist_name):
    try:
        dist = main.defined_dists[dist_name]
    except KeyError:
        raise ValueError("Distribution {} not found".format(dist_name))
    return dist.var()

def expectation(dist_name):
    try:
        dist = main.defined_dists[dist_name]
    except KeyError:
        raise ValueError("Distribution {} not found".format(dist_name))
    return dist.expectation()

def info(dist_name):
    try:
        dist = main.defined_dists[dist_name]
    except KeyError:
        raise ValueError("Distribution {} not found".format(dist_name))
    return dist.__repr__()

def define(x,y):
    if type(x) == str and x not in parsing.functions:
        logger.info("Defining var {} as {}".format(x,y))
        main.defined_vars[x] = y
    elif type(x) != str:
        raise ValueError("Variable name of type {} not str".format(type(x)))
    else:
        raise ValueError("Variable name {} invalid as it is a reserved function name".format(x))
