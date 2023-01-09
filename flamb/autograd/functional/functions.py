import flamb
import math

def exp(x):
    if isinstance(x, flamb.Variable):
        return x.exp()
    else:
        return math.exp(x)

def cos(x):
    if isinstance(x, flamb.Variable):
        return x.cos()
    else:
        return math.cos(x)

def sin(x):
    if isinstance(x, flamb.Variable):
        return x.sin()
    else:
        return math.sin(x)


def tan(x):
    if isinstance(x, flamb.Variable):
        return x.tan()
    else:
        return math.tan(x)


def tanh(x):
    if isinstance(x, flamb.Variable):
        return x.tanh()
    else:
        return math.tanh(x)
