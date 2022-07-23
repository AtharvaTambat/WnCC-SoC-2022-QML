# **Linear Regression**
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
We want to minimize $J(\theta)$. Let us initialize random values for all the weights $\theta_{i}$ s and then repeatedly change $\theta$ to make $J(\theta)$ smaller, until hopefully we converge to a value of $\theta$ that minimizes $J(\theta)$. Specifically, let’s consider the gradient descent algorithm, which starts with some initial $\theta$, and repeatedly performs the update:

$$ \theta_j := \theta_j - \alpha\frac{\partial}{\partial \theta_j}J(\theta)$$

Here, $\alpha$ is called the learning rate. In order to calculate the partial derivative:

$$\frac{\partial}{\partial\theta_{j}} J(\theta) = \frac{\partial}{\partial\theta_{j}} (h_{\theta}(x) - y)^2$$

$$  = (h_{\theta}(x) - y)\frac{\partial}{\partial\theta_{j}}(h_{\theta}(x) - y) $$

$$ = (h_{\theta}(x) - y)\frac{\partial}{\partial\theta_{j}} \left(\sum_{i = 0} ^{d} \theta_i x_i - y\right)$$

$$ = (h_{\theta}(x) - y)x_j $$

For a single training example, this gives the update rule:

$$ \theta_j := \theta_j + \alpha (y_j^{(i)} - h_{\theta}(x^{(i)})) x_j^{(i)}$$

This is called the **LMS update rule**. The above rule is only for a single training example. Modifying it for multiple training examples by vectorization, the algorithm is:

Repeat until convergence {

$$ \theta := \theta + \alpha \sum_{j = 1} ^{n} (y^{(i)} - h_{\theta}(x^{(i)})) x^{(i)}$$

}

This is the basic overview of the algorithm. More fine-tuning of the algorithm can be done with adjusting the weights of differnt input parameters, and choosing hyperparameters such as number of steps, the learning rate $\alpha$ etc.

# Clustering 
Clustering is a part of unsupervised learning algorithm - which means that the dataset does not have a value that we have to guess, like in linear regression.
Here, we are given data as a scatter plot in multiple dimensions, and we have to divide them in a given number of groups. Foe this, we use the k-means algorithm.

The k-means clustering algorithm is as follows:

1. Initialize cluster centroids $\mu_1, \mu_2, . . . , \mu_k \in \mathbb{R}^d$ randomly.
2. Repeat until convergence {

For every i, set:

$$c^{(i)} :=  argmin_{j} || x^{(i)} - \mu_j ||^2$$

For each j, set:

$$\mu_j := \frac{ \Sigma_{i = 1} ^{n} x^{(i)} (c^{(i)} = j) } { \Sigma_{i = 1} ^{n} 1 (c^{(i)} = j ) } $$

}

3. The above two steps basically means that we first initialize randomly n points ($a_1, a_2,...a_n$) (n = number of groups) , and then we iterate over all the points in the dataset and group the points into n sets ($S_k$)

$\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ S_k$ = { $x^{(i)} : x^{(i)}$ is closest to $a_k$}

4. We then calculate the mean of all the points in a particular set, $S_k$, and re-initialize the point $a_k$ to the mean of all the points in that set
5. We iterate over the above two steps, hoping to converge to an answer.

How do we know that we will converge to an answer? To get a quantitative measure for that we define the **distortion function**:

$$J(c, \mu) =  \sum_{i = 1} ^{n} ||x^{(i)} - \mu_{c^{(i)}}||^2$$

Thus, J measures the sum of squared distances between each training example $x^{(i)}$ and the cluster centroid $\mu_{c^{(i)}}$ to which it has been assigned.
The distortion function J is a non-convex function, and so coordinate descent on J is not guaranteed to converge to the global minimum.

This is the general overview of the k-means clustering algorithm. It can get stuck in a bad local minima or, the no. of groups selected, might not be appropriate to group the cluster etc. So, run the k-means algorithm multiple times, with different initial points and number of groupd to see which set of hyper-parameters works the best.

# Neural Networks
The human visual system is one of the wonders of the world. Most people effortlessly recognize digits. The difficulty of visual pattern recognition becomes apparent if you attempt to write a computer program to recognize digits. Neural networks approach the problem in a different way. 

## The Perceptrons
The preceptron is kind of an artificial neuron. A perceptron takes several binary inputs, $x_1,x_2,…,$ and produces a single binary output. Each input is associated with a weight $w_i$.

![image](https://user-images.githubusercontent.com/95964330/180625680-8da6ea83-a390-4d11-8d6b-7c3d6e02e2a0.png)

The neuron's output, 0 or 1, is determined by whether the weighted sum $\Sigma_j w_j x_j$ is less than or greater than some threshold value ( = -b). 
We define x and w vector, so, $\Sigma_j w_j x_j$ = $w\cdot x$.

So, **output =**

$$\begin{array}{ll}
		0  & \mbox{if } w\cdot x + b \geq 0 \\
		1 & \mbox{if } w\cdot x + b < 0
	\end{array}
$$

But how can we devise such algorithms for a neural network? Suppose we make a neural network out of preceptrons and train it to recognize one image. We would want that a small change in output, to cause a small change in the learnt values of the parameters of the precetron, but with the "abrupt" nature of the output of the preceptron, this is not possible. Therefore we replace it with another neuron.

## The sigmoid neuron
The sigmoid neuron has output $\sigma(w\cdot x + b)$ $$ for:

$$\begin{eqnarray} 
  \sigma(z) \equiv \frac{1}{1+e^{-z}}.
\end{eqnarray} $$

The output of a sigmoid neuron with inputs $x_1,x_2,…,$ weights $ w_1,w_2,…,$ and bias b is

$$\begin{eqnarray} 
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}.
\end{eqnarray}$$

The sigmoid neuron is just the "smoothened" out version of the step function used in the preceptron to remove the difficulty of abrupt changes in the output, for small changes in the weights of the preceptrons. 

## How Neural Networks work?

# **Implementation**
The following programs for ML have been implemented as a part of evaluation for this week:
1. Linear regression - Weather Dataset
2. Clustering - Iris Flower Dataset
3. Support Vector Machine - Breast Cancer Dataset
4. Neural networks - Recognising digits from the MNIST Dataset
