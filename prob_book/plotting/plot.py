import urllib,base64
import matplotlib.pyplot as plt
from io import BytesIO
from prob_book.parsing import evaluation
from prob_book.parsing import parser

class JupyterPlot():
    def __init__(self,data):
        self.data = data
        self.msg_content = {"source": "kernel",
            "data": {
                "image/png": self.data
            },
            "metadata": {
                "image/png": {
                    "width": 600,
                    "height": 400
                }
            }}


def to_png(fig):
    """
    Returns base 64 encoded png from matplotlib fig.
    Taken from https://ipython-books.github.io/16-creating-a-simple-kernel-for-jupyter/
    """
    imgdata = BytesIO()
    fig.savefig(imgdata,format="png")
    imgdata.seek(0)
    return urllib.parse.quote(base64.b64encode(imgdata.getvalue()))

def plot(x,y,*args):
    kwargs = evaluation.extract_kw_args(args)
    fig,ax = plt.subplots(1,1,figsize=(6,4))
    ax.plot(x,y)

    if "xlab" in kwargs:
        plt.xlabel(kwargs["xlab"])
    if "ylab" in kwargs:
        plt.ylabel(kwargs["ylab"])


    if parser.CLIENT == "terminal":
        plt.show()
    elif parser.CLIENT == "jupyter":
        return JupyterPlot(to_png(fig))
