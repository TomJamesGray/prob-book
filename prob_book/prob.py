from prob_book import main
import logging

logger = logging.getLogger(__name__)

def prob(stmt):
    logger.info(stmt)
    dist = None
    for i,c in enumerate(stmt):
        if c in main.defined_dists.keys():
            dist = main.defined_dists[c]
            dist_name = c

    if dist == None:
        logger.error("No dist found for prob function with stmt {}".format(stmt))
        return False

    logger.info("Dist chosen: {}".format(dist))

    return dist.prob_line(stmt)
