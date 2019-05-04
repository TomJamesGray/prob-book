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
    parsing.eval_line(parsing.parse_line("X~Po(1)"))
    parsing.eval_line(parsing.parse_line("P(X=2)"))
    while True:
        l = input()
        parsing.eval_line(parsing.parse_line(l))
