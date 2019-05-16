import logging
from prob_book import parsing

logger = logging.getLogger(__name__)


class Distribution:
    prob_operations = ["="]

    def operator(self,op: str):
        ops = {
            "=":self.eq
        }
        return ops[op]

    def prob_line(self,l: str):
        stmt_split = None
        # Find the operation
        for op in self.prob_operations:
            if op in l:
                stmt_split = l.split(op)
                operation_func = self.operator(op)
                break

        if stmt_split == None:
            logger.error("No operator found with stmt {}".format(stmt))
            return False

        if len(stmt_split) > 2:
            logger.error("Too many elements in split statement {}".format(stmt_split))
            return False

        for x in stmt_split:
            if x != self.name:
                result = operation_func(parsing.eval_line(parsing.parse_line(x)))
                logger.info("Result after evaluation {}".format(result))
                return result
