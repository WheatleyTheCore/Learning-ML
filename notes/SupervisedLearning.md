# Supervised Learning 
 
 ## Basic Definition:



 Supervised leraning uses a set of data to learn from. The data is split into a group of data used for learning(which has no labels or correct output given, just the input), or "training"(basically having the input data and the correct output(called the label)), and  a group of data to test. It tries to do whatever its goal is with the training data, checks that against the test data, and figures out how wrong it is. It then makes changes to be less wrong, and then repeats that process.

 ### Areas I need to learn some more about:
  - The steps taken to minimize error 
  - How to actually put together a model
  - The parts of the model itself 

  ### There are two types of supervised learning, Classification and Regression
  - Classification- Classify the data(kinda obvious)
  - Regression- Predict something based on some input(s)

# Regression Models
#### It predicts stuff that can be continuous, like prices or liklihood of cats to appear, by looking at some input data 

Continuous stuff is stuff that can have any value, like price or probability, but not things that are discrete or can only have certain values.

The input stuff are called features(for example age, which is numerical, or hair color, which would be categorial)

Basically: Input Features => Model => Prediction

## Supervised Learning Algorithms

### Linear Regression
If you were to plot all your data, this basically
draws a line of best fit, so you can guess based on where that line goes.

This line could be defined as = slope*input + y intercept + error

in order to find the best fitting line, we  
- use a cost/loss function that tells us how wrong we are
- find the slope and y intercept that make the least error

All of ^^ assumes 2D data, for 3D inputs, it would be a plane of best fit, etc.

So how do we do the error minimization bit?

add up the square of the error for each guess(we square it to make the math easier I think?), divide by the numbers of guesses(sometimes multipied by two to make the math easier), and take the derivative so you know how to change the parameters(which are slope and y intercept) to make the loss less.

When you get to have lots of inputs taking the derivative is impractical, so we use gradient decent

Gradient Decent- Take partial derivatives for each parameter, then walk in the direction that decreases the error; repeat.

Partial derivatives are basically taking the derivative with respect to one input while holding all the others constant.

### Overfitting is the equivalent to memorizing the answer key to a test, you get the right answers for those questions, but if you are asked anything else you have no idea what the answer is

To avoid overfitting, the model has to be generic.
- Use as much training data as possible
- add a penalty for overfitting using a regularization term

# Label Prediction
Predicting labels or classes based on some input

## Logistic Regression
Insead of using a line, we use a logs and stuff. 

Gives probability of a thing belonging to a class

To do this it uses a sigmoid function to squish the probability between 0 and 1 to make a percent.

The thing that we are sqishing to between 0 and 1 is the liklihood of whatever our input is being something divided by the probability of that not happening. Basically

sigmoid(probability that thing happens)

or mathematically:
ln(p/(p-1)) = b + mx + epsilon

To minimize loss we do gradient descent

## Support Vector Machines
SVMs basically just draw a line(or hyperplane depending on how many dimensions you're in) separating your input spaces into "classification zones."