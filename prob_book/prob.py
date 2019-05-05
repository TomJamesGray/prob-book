from prob_book import main
from prob_book import parsing
import logging
import string

logger = logging.getLogger(__name__)

def prob(stmt):
    logger.info(stmt)
    dist = None
    for i,c in enumerate(stmt):
        if c in main.defined_dists.keys() and stmt[i-1] not in string.ascii_letters \
                and stmt[i+1] not in string.ascii_letters:
            dist = main.defined_dists[c]
            dist_name = c

    if dist == None:
        logger.error("No dist found for prob function with stmt {}".format(stmt))
        return False

    logger.info("Dist chosen: {}".format(dist))
    stmt_split = None
    # Find the operation
    for op in dist.prob_operations:
        if op in stmt:
            stmt_split = stmt.split(op)
            operation_func = dist.operator(op)
            break

    if stmt_split == None:
        logger.error("No operator found with stmt {}".format(stmt))
        return False

    if len(stmt_split) > 2:
        logger.error("Too many elements in split statement {}".format(stmt_split))
        return False

    for x in stmt_split:
        if x != dist_name:
            result = operation_func(parsing.eval_line(parsing.parse_line(x)))
            logger.info("Result after evaluation {}".format(result))
            return result
