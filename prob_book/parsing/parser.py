import os
import inspect
from lark import Lark

def parse(line):
    parser = Lark.open(os.path.join(os.path.dirname(inspect.stack()[0][1]),"grammar.lark"))
    return parser.parse(line).pretty()
