import logging
from prob_book import parsing

logger = logging.getLogger(__name__)


class Distribution:
    def prob_line(self,l: str):
        stmt_split = None
        # Find the operation
        if ">=" in l:
            op_fn_1 = self.greater_eq
            op_fn_2 = self.less_eq
            stmt_split = l.split(">=")
        elif ">" in l:
            op_fn_1 = self.greater
            op_fn_2 = self.less
            stmt_split = l.split(">")
        elif "<=" in l:
            op_fn_1 = self.less_eq
            op_fn_2 = self.greater_eq
            stmt_split = l.split("<=")
        elif "<" in l:
            op_fn_1 = self.less
            op_fn_2 = self.greater
            stmt_split = l.split("<")

        elif "=" in l:
            stmt_split = l.split("=")
            if len(stmt_split) != 2:
                logger.error("Incorrect amount of elements in split statement {}".format(stmt_split))
                return False
            for i, x in enumerate(stmt_split):
                # TODO Handling if name not in stmt
                if x == self.name:
                    # Evaluate the other section of the split statement
                    result = self.eq(parsing.eval_line(parsing.parse_line(stmt_split[not i])))
                    logger.info("Result after evaluation {}".format(result))

                    return result
            return None

        if len(stmt_split) != 2:
            logger.error("Incorrect amount of elements in split statement {}".format(stmt_split))
            return False

        if stmt_split[0] == self.name:
            result = op_fn_1(parsing.eval_line(parsing.parse_line(stmt_split[1])))
            logger.info("Result after evaluation {}".format(result))
            return result

        elif stmt_split[1] == self.name:
            result = op_fn_2(parsing.eval_line(parsing.parse_line(stmt_split[0])))
            logger.info("Result after evaluation {}".format(result))
            return result

        else:
            return None



