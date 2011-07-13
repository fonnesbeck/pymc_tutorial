import pymc

# Some fake data
alpha = 3
beta = 5
N = 100
dataset = pymc.rweibull(alpha,beta, N)

# Model
a = pymc.Uniform('a', lower=0, upper=10, value=5, doc='Weibull alpha parameter')
b = pymc.Uniform('b', lower=0, upper=10, value=5, doc='Weibull beta parameter')
like = pymc.Weibull('like', alpha=a, beta=b, value=dataset, observed=True)