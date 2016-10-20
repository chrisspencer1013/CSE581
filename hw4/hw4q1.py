#This code is from the following link, 
#I have done nothing to modify it but change the data
# https://blog.dbrgn.ch/2013/3/26/perceptrons-in-python/ 

from random import choice
from numpy import array, dot, random
from plotly import plotly

unit_step = lambda x: 0 if x < 0 else 1

training_data = [
    (array([2,2,1]),0),
    (array([3,5,1]),0),
    (array([1,3,1]),1),
    (array([-1,-.5,1]),1)
]

w = array([1.0,1.0,1.0])

errors = []
eta = .2
n = 100

for i in range(n):
    x, expected = choice(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)
    w += eta * error * x

for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))

print (w)