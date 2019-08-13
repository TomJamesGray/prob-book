from lark import Transformer
from lark import v_args

@v_args(inline=True)
class EvalLine(Transformer):
    from operator import add,sub,mul,truediv as div,neg
    number = float