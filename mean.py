from pymc.gp import *

# Generate mean 
def quadfun(x, a, b, c):
	return (a * x ** 2 + b * x + c)

M = Mean(quadfun, a = 1., b = .5, c = 2.)