import math

#input data
D = 2500.
X = 2500
A = 100.
E = 5e5
F = 1.5e7

#calculated data
L = math.sqrt(X**2 + D**2)
V = A*L

def residual(x):
    T = s*a*x/l
    return T-F
    
def stiffness(x):
    K = E*A*L*(x/l/l)**2 + s*A*L*(l**2-2*x**2)/l**4
    return K

#initialize variables
s = 0.
l = L
a = A
x = X

cnorm = 1e-12 #numerical zero for the stop condition
miter = 200 #max. number of iterations  
rnorm = cnorm*2 #initial value for the residual norm
niter = 0 #initial value for the number of iterations
while (rnorm > cnorm) and (niter<miter):
    niter = niter + 1
    
    #stiffness and residual
    K = stiffness(x)
    if abs(K) < 1e-20:
        print('Near zero stiffness --> STOP')
    R = residual(x)
    
    #geometry increment
    u = -R/K
    x = x + u
    l = math.sqrt(x**2 + D**2)
    a = V/l
    
    #stress
    s = E*math.log(l/L)
    
    #residual norm
    rnorm = abs(R)
    print('residual norm after iteration #{} : {}'.format(niter,rnorm))
    
print('solution : x = {}'.format(x))