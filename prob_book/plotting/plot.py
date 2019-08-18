import matplotlib.pyplot as plt
from prob_book.parsing import evaluation

def plot(x,y,*args):
    kwargs = evaluation.extract_kw_args(args)
    plt.plot(x,y)
    if "xlab" in kwargs:
        plt.xlabel(kwargs["xlab"])
    if "ylab" in kwargs:
        plt.ylabel(kwargs["ylab"])
    plt.show()