import numpy as np

# function: function to be integrated in form "lambda x: f(x)"
# x_min: lower bound of integration
# x_max: upper bound of integration
# step: step for approximation, the smaller the better

def sum_left(function, x_min, x_max, step):
    s = np.arange(x_min, x_max, step)
    f = []
    for i in s:
        f.append(function(i))
    array_integral = map(lambda x: x * step, f)
    sum = 0
    for i in array_integral:
        sum += i
    return sum

def sum_right(function, x_min, x_max, step):
    s = np.arange(x_min + step, x_max + step, step)
    f = []
    for i in s:
        f.append(function(i))
    array_integral = map(lambda x: x * step, f)
    sum = 0
    for i in array_integral:
        sum += i
    return sum

# integral is close to the average of these two sums
# the error in this average lies in the idea that the right sum is bigger than the left sum
# this means that the actual value of the integral lies in between these two sums
# then the error is the difference in these two sums over two

def ave_riemann_sum(function, x_min, x_max, step):
     ave = (sum_left(function, x_min, x_max, step) + sum_right(function, x_min, x_max, step)) / float(2)
     error = (sum_right(function, x_min, x_max, step) - sum_left(function, x_min, x_max, step)) / float(2)
     result = (ave, error)
     return result

## example 
Int = ave_riemann_sum(lambda x: np.sin(x)**2 * x**2 * 10**-x, 0, np.pi, .0001)

print "The integral of sin(x)^2 * x^2 * 10^(-x) from 0 to pi is", Int[0], "with an uncertainty of", Int[1]
