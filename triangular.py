from numpy import log, random, sqrt, zeros, atleast_1d

def triangular_like(x, mode, minval, maxval):
    """Log-likelihood of triangular distribution"""
    
    x = atleast_1d(x)
    
    # Check for support
    if any(x<minval) or any(x>maxval): return -inf
    
    # Likelihood of left values
    like = sum(log(2*(x[x<=mode] - minval)) - log(mode - minval) - log(maxval - minval))

    # Likelihood of right values    
    like += sum(log(2*(maxval - x[x>mode])) - log(maxval - minval) - log(maxval - mode))
    
    return like

def rtriangular(mode, minval, maxval, size=1):
    """Generate triangular random numbers"""

    # Uniform random numbers
    z = atleast_1d(random.random(size))

    # Threshold for transformation
    threshold = (mode - minval)/(maxval - minval)
    
    # Transform uniforms
    u = atleast_1d(zeros(size))
    u[z<=threshold] = minval + sqrt(z[z<=threshold]*(maxval - minval)*(mode - minval))
    u[z>threshold] = maxval - sqrt((1 - z[z>threshold])*(maxval - minval)*(maxval - mode))
    
    return u