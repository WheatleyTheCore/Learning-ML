# the code I followed while writing this: https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/
#https://github.com/mattnedrich/GradientDescentExample

import matplotlib.pyplot as plt
from numpy import *


points = genfromtxt("./points.csv", delimiter=",")

xPoints = []
for i in range(0, len(points)):
    xPoints.append(points[i, 0])

yPoints = []
for i in range(0, len(points)):
    yPoints.append(points[i, 1])

def calculateError(b, m):
    error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        error += (y - (m * x + b)) ** 2
    return error / float(len(points))

def stepInDirectionOfGradient(current_b, current_m, learning_rate):
    b_partial_deriv = 0
    m_partial_deriv = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_partial_deriv += (2/N) * (y - (current_m * x + current_b))
        m_partial_deriv += (2/N) * x * (y - (current_m * x + current_b))

    new_b = current_b - (learning_rate * (-b_partial_deriv))
    new_m = current_b - (learning_rate * (-m_partial_deriv))

    return [new_b, new_m]

def doTheDescent(beginning_b, beginning_m, learning_rate, epoches):
    b = beginning_b
    m = beginning_m

    for i in range(epoches):
        b, m = stepInDirectionOfGradient(b, m, learning_rate)
    return [b, m]


def runDownTheMountain():
    initial_m = 0
    initial_b = 0
    learningRate = 0.0001
    epoches = 1000
    print("crossing fingers...")
    [b, m] = doTheDescent(initial_b, initial_m, learningRate, epoches)    
    
    lineyPoints = []
    for i in range(0, len(points)):
        lineyPoints.append(points[i, 0]* m + b)

    plt.plot(xPoints, yPoints, 'ro')
    plt.plot(xPoints, lineyPoints)
    plt.show()
    print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(epoches, b, m, calculateError(b, m)))


runDownTheMountain()


