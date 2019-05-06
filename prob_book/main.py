import logging
import logging.config
from prob_book import parsing

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
            "level": logging.INFO
        },
        "prob_book.prob": {
            "handlers": ["f_parsing"],
            "level": logging.INFO
        }
    }
}
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

defined_dists = {}

def main():
    while True:
        l = input()
        res = parsing.eval_line(parsing.parse_line(l))
        if res != None:
            print(res)
