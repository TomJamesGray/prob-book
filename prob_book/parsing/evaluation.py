import math
from lark import Transformer
from lark import v_args

funcs = {
    "sin":{
        "n": 1,
        "func": lambda x: math.sin(x),
        "level": 5,
        "regex_name": "sin"
    },
    "cos": {
        "n": 1,
        "func": lambda x: math.cos(x),
        "level": 5,
        "regex_name": "cos"
    },
    "tan": {
        "n": 1,
        "func": lambda x: math.tan(x),
        "level": 5,
        "regex_name": "tan"}
}

@v_args(inline=True)
class EvalLine(Transformer):
    from operator import add,sub,mul,truediv as div,neg
    number = float

    def func_call(self,name,*args):
        f = funcs[name]["func"]
        print(args)
        unpacked = []
        for val in args[0].children:
            unpacked.append(val.children[0])
        print(unpacked)
        return f(*unpacked)
