import logging
import argparse
import logging.config
from prob_book import parsing
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
        },
        "prob_book.main":{
            "handlers":["f_parsing"],
            "level":logging.INFO
        }
    }
}
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

defined_dists = {}

class ANSICols:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

def main():
    parser = argparse.ArgumentParser(description="Interactive python shell for probability and other calculations")
    parser.add_argument("--devel",action="store_true",default=False,help="Enables development mode which shows more \
                                                                          logging and doesn't throttle all exceptions")
    parser.add_argument("--precision",action="store",type=int,default=6)
    results = parser.parse_args()

    # Reduce logging if devel is false
    # global logger
    if not results.devel:
        for x in logger.handlers:
            x.setLevel(logging.ERROR)


    while True:
        l = input(">>> ")
        try:
            res = parsing.eval_line(parsing.parse_line(l),results.precision)
        except EqualityForCtsDist:
            print("{}Equality operation can't be used on continuous distribution{}".format(ANSICols.RED,ANSICols.RESET))
            continue
        except MismatchedBrackets:
            print("{}Closing bracket count doesn't match opening bracket count{}".format(ANSICols.RED,ANSICols.RESET))
            continue
        except Exception as e:
            if results.devel:
                raise e
            else:
                print("{}{}{}".format(ANSICols.RED,e,ANSICols.RESET))
                continue

        if res != None:
            print("{}{}{}".format(ANSICols.GREEN,res,ANSICols.RESET))
