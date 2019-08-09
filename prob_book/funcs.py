from prob_book import main

def variance(dist_name):
    try:
        dist = main.defined_dists[dist_name]
    except KeyError:
        raise ValueError("Distribution {} not found".format(dist_name))
    return dist.var()