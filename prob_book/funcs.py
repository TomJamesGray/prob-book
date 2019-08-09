from prob_book import main

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
    print("Info")
    return dist.__repr__()