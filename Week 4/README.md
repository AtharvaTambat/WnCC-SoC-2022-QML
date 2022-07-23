# **Linear & Logistic Regression**
Linear Regression is a machine learning algorithm based on supervised learning. As indicated by the name, the hypothesis (***y***), that the computer has to find the value of to guess the value of something (weather, house prices etc), is approximated as a linear combination of the parameters ***x***

$$h_{\theta}(x) = \theta_{0} + \theta_1x_1 + \theta_2x_2 ...$$

where, $\theta_i$'s are called the weights.

## Vectorization of the hypothesis

Instead of long summations the hypothesis can be represented in terms of vectors $\theta$ and $x$ (not counting $x_0$ which, by convention is taken to be 1)

$$h(x) = \theta^{T}x$$

## Cost function

We have to define some function, which gives us a measure of how far our guess is from the given dataset. We do this by defining the cost function - which uses least squares summation - to "measure the sum of all distances" between our guess and actual value of parameter, we have to guess.

$$ J(\theta) = \frac{1}{2} \sum_{i = 1} ^{n} (h_{\theta}(x^{(i)}) - y^{(i)})^2$$

## Least Mean Square Algorithm



# **Implementation**
The following programs for ML have been implemented as a part of evaluation for this week:
1. Linear regression - Weather Dataset
2. Clustering - Iris Flower Dataset
3. Support Vector Machine - Breast Cancer Dataset
4. Neural networks - Recognising digits from the MNIST Dataset
