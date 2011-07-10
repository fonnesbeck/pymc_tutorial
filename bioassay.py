from pymc import *
from numpy import array

n = [5]*4
dose = [-.86,-.3,-.05,.73]
response = [0,1,3,5]

alpha = Normal('alpha', mu=0, tau=0.01)
beta = Normal('beta', mu=0, tau=0.01)
    
theta = Lambda('theta', lambda a=alpha, b=beta: invlogit(a + b*array(dose)))

@observed
def deaths(value=response, n=n, p=theta):
    """deaths ~ binomial_like(n, p)"""
    return binomial_like_like(value, n, p)