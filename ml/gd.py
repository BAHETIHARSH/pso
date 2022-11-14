
import numpy as np
def gradient(start,gradient,learningrate,max_iter,tol =0.1):
    steps = [start]
    x = start
    
    for _ in range(max_iter):
        diff = learningrate*gradient(x)
        if np.abs(diff)<tol:
            break
        x = x-diff
        steps.append(x)    
        
    return steps,x
    
    
def fun1(x):
    return x**2-4*x+fun1
    
def gradfun(x):
    return 2*x-4
    
print(gradient(9,gradfun,0.1,100,0.01))
