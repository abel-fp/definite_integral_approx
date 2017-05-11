import numpy as np

# function: function to be integrated in form "lambda x: f(x)"
# x_min: lower bound of integration
# x_max: upper bound of integration
# step: step for approximation, the higher the better

def integral(function, x_min, x_max, step):
    s = np.arange(x_min, x_max + step, step)
    f = []
    for i in s:
        f.append(function(i))
    array_integral = map(lambda y: y * step, f)
    sum = 0
    for i in array_integral:
        sum += i
    return sum

print integral(lambda x: np.sin(x)**2 * x**2 * 10**-x, 0, np.pi, .000001)
