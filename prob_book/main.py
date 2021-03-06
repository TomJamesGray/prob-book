import logging
import argparse
import numpy as np
import logging.config
from prob_book.parsing import parser
from prob_book.exceptions import *
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "main": {"format": "%(levelname)s-%(name)s-%(lineno)d: %(message)s"}
    },
    "handlers": {
        "f_parsing": {
            "class": "logging.StreamHandler",
            "formatter": "main",
            "level": logging.INFO}
    },
    "loggers": {
        "":{
            "handlers":["f_parsing"],
            "level":logging.INFO
        },
        "prob_book.main": {
            "handlers": ["f_parsing"],
            "level": logging.INFO
        },
        "prob_book.parsing": {
            "handlers": ["f_parsing"],
            "level": logging.DEBUG
        },
        "prob_book.base_dist": {
            "handlers": ["f_parsing"],
            "level": logging.INFO
        },
        "prob_book.distributions.prob": {
            "handlers": ["f_parsing"],
            "level": logging.INFO
        }
    }
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

defined_vars = {}

class ANSICols:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

def main():
    arg_parse = argparse.ArgumentParser(description="Interactive python shell for probability and other calculations")
    arg_parse.add_argument("--debug",action="store_true",default=False,help="Enables development mode which shows more "
                                                                         "logging and doesn't throttle all exceptions")
    arg_parse.add_argument("--precision",action="store",type=int,default=6,help="Integer value that controls the maximum "
                                                                             "amount of numbers after the decimal point, "
                                                                             "defaults to 6")
    results = arg_parse.parse_args()
    parser_cls = parser.Parser()
    # Reduce logging if devel is false
    # global logger
    if not results.debug:
        for x in logger.handlers:
            x.setLevel(logging.ERROR)

    while True:
        l = input(">>> ")
        try:
            res = parser_cls.parse(l)
        except EqualityForCtsDist:
            print("{}Equality operation can't be used on continuous distribution{}".format(ANSICols.RED,ANSICols.RESET))
            continue
        except MismatchedBrackets:
            print("{}Closing bracket count doesn't match opening bracket count{}".format(ANSICols.RED,ANSICols.RESET))
            continue
        except IncorrectNumberOfArgs:
            print("{}Incorrect number of arguments supplied to function{}".format(ANSICols.RED, ANSICols.RESET))
        except Exception as e:
            if results.debug:
                raise e
            else:
                print("{}{}{}".format(ANSICols.RED,e,ANSICols.RESET))
                continue

        if type(res) == np.ndarray:
            print("{}{}{}".format(ANSICols.GREEN, res, ANSICols.RESET))
        elif res != None:
            # Numpy arrays don't like being tested with None
            print("{}{}{}".format(ANSICols.GREEN,res,ANSICols.RESET))
