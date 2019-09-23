import os
import inspect
from lark import Lark
from prob_book.parsing import evaluation
from prob_book.exceptions import MismatchedBrackets

# Set the client type to terminal by default, this affects how the plotting functions
# displays the plot
CLIENT = "terminal"

class Parser:
    def __init__(self):
        self.eval = evaluation.EvalLine()
        self.parser = Lark.open(os.path.join(os.path.dirname(inspect.stack()[0][1]), "grammar.lark"))

    def parse(self,line):
        if line.count("(") != line.count(")"):
            raise MismatchedBrackets

        tree = self.parser.parse(line)

        return self.eval.transform(tree)

