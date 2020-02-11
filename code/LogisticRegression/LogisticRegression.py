# From https://towardsdatascience.com/logistic-regression-python-7c451928efee, modifications made to learn how it works

from scipy.special import expit
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
sns.set()


x, y = make_classification(
    n_samples=100,
    n_features=1,
    n_classes=2,
    n_clusters_per_class=1,
    flip_y=0.03,
    n_informative=1,
    n_redundant=0,
    n_repeated=0
)

plt.scatter(x, y, c=y, cmap='rainbow')

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

lr = LogisticRegression()
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

df = pd.DataFrame({'x': x_test[:, 0], 'y': y_test})
df = df.sort_values(by='x')
sigmoid_function = expit(df['x'] * lr.coef_[0][0] + lr.intercept_[0]).ravel()
plt.plot(df['x'], sigmoid_function)
plt.scatter(df['x'], df['y'], c=df['y'], cmap='rainbow', edgecolors='b')
plt.show()
