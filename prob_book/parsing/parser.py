import os
import inspect
from lark import Lark
from prob_book.parsing import evaluation

# Set the client type to terminal by default, this affects how the plotting functions
# displays the plot
CLIENT = "terminal"

def parse(line):
    parser = Lark.open(os.path.join(os.path.dirname(inspect.stack()[0][1]),"grammar.lark"))

    tree = parser.parse(line)
    # print(tree.pretty())

    return evaluation.EvalLine().transform(tree)
