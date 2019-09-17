import urllib,base64
import matplotlib.pyplot as plt
from io import BytesIO
from prob_book.parsing import evaluation
from prob_book.parsing import parser

class JupyterPlot():
    def __init__(self,fig,ax):
        self.fig = fig
        self.ax = ax
        self.data = to_png(fig)
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

class Plot:
    def __init__(self):
        self.refresh()

    def refresh(self):
        """Refreshes the plot"""
        self.fig, self.ax = plt.subplots(1, 1, figsize=(6, 4))

    def plot(self,x,y,*args):
        """
        Implements the plot function using pyplot
        :param x: X data
        :param y: Y data
        :param args: Allows labels, titles and styles to be set. The syntax for the style
        is the same as used in regular pyplot
        """
        kwargs = evaluation.extract_kw_args(args)

        if not kwargs.get("add",False):
            self.refresh()

        if "style" in kwargs:
            plt.plot(x,y,kwargs["style"])
        else:
            plt.plot(x,y)

        if "xlab" in kwargs:
            plt.xlabel(kwargs["xlab"])
        if "ylab" in kwargs:
            plt.ylabel(kwargs["ylab"])
        if "title" in kwargs:
            plt.title(kwargs["title"])



        if parser.CLIENT == "terminal":
            plt.show()
        elif parser.CLIENT == "jupyter":
            return JupyterPlot(self.fig,self.ax)
