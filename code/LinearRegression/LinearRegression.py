# From https://towardsdatascience.com/introduction-to-linear-regression-in-python-c12a072bedf0
# Just to stress, this is mainly the code from the above article, but changed a bit as I messed around with it to figure it out.

import pandas as pd #provides dataframe
import numpy as np #lets us do cool math stuff
from matplotlib import pyplot as plt #lets us plot stuff

#Get some random x coordinates(called X), and use them to calculate some Y values with some noise added(which we use res for)
X = np.random.randn() * np.random.randn(200) + 7
res = 0.4 * np.random.randn(200)       #The static we add so the points do not make an actual line
Y = 9 + np.random.randn() * X + res                 


df = pd.DataFrame(
    {'X': X,
     'y': Y}
)

xmean = np.mean(X)
ymean = np.mean(Y)


df['xycov'] = (df['X'] - xmean) * (df['y'] - ymean)
df['xvar'] = (df['X'] - xmean)**2


b = df['xycov'].sum() / df['xvar'].sum() #calculate the slope the line should have
a = ymean - (b * xmean) #calculate the y intercept our line should have
print(f'α = {a}')
print(f'ß = {b}')

ypred = a + b * X

plt.figure(figsize=(12, 6))
plt.plot(X, ypred, color="purple")    
plt.plot(X, Y, 'r+', )  
plt.title('Linear Regression!')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
