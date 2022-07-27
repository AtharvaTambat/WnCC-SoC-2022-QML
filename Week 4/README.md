# **Linear Regression**
Linear Regression is a machine learning algorithm based on supervised learning. As indicated by the name, the hypothesis (***y***), that the computer has to find the value of to guess the value of something (weather, house prices etc), is approximated as a linear combination of the parameters ***x***

$$h_{\theta}(x) = \theta_{0} + \theta_1x_1 + \theta_2x_2 ...$$

where, $\theta_i$'s are called the weights.

## Vectorization of the hypothesis

Instead of long summations the hypothesis can be represented in terms of vectors $\theta$ and $x$ (not counting $x_0$ which, by convention is taken to be 1)

$$h(x) = \theta^{T}x$$

## Cost function 💰 💸

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

# Neural Networks :spider_web:
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

## The Sigmoid Neuron :brain:
The sigmoid neuron has output $\sigma(w\cdot x + b)$  for:

$$\begin{eqnarray} 
  \sigma(z) \equiv \frac{1}{1+e^{-z}}.
\end{eqnarray} $$

The output of a sigmoid neuron with inputs $x_1,x_2,…,$ weights $w_1,w_2,…,$ and bias b is

$$\begin{eqnarray} 
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}.
\end{eqnarray}$$

The sigmoid neuron is just the "smoothened" out version of the step function used in the preceptron to remove the difficulty of abrupt changes in the output, for small changes in the weights of the preceptrons. 

## How Neural Networks work?
Let's say that the problem at hand is to identify the digit shown to the network. The network consists of input layers, hidden layers, and output layers.
A specific part of the network is assigned to identify the "shape" in a portion(say, top-right corner) of the image - as shown in the following figure.

![image](https://user-images.githubusercontent.com/95964330/180626267-062a96b5-1c64-46af-b373-cd45c51df7c9.png)

The pixels are broken down in an array and fed to the neural net. The neurons then initialize random weights and just like in the Least Mean Square Algorithm, minimizing the cost function, using gradient descent algorithm: 

$$\begin{eqnarray}  C(w,b) \equiv
  \frac{1}{2n} \sum_x \|| y(x) - a\||^2.
\end{eqnarray} $$

where, y(x) is a 10 dimensional vector. For example, if a particular training image, x, depicts a 6, then $y(x)=(0,0,0,0,0,0,1,0,0,0)^T$ is the desired output from the network.

The gradients required in the algorithm, are calculated using a method called **back-propogation method**.

# Support Vector Machine
Support Vector Machines are used to find the **hyperplane** which classifies the given dataset. Consider a liner SVM classifier. It tries to find the hyperplane, in which the distance between the positive and the negative "gutter" (meaning explained ahead) is maximum

<img src = "https://user-images.githubusercontent.com/95964330/180627046-3e56673a-a7f6-441e-bbf3-b3d6dd8e80a2.png" width = 300>

We suppose that the data is linearly classifiable i.e. a single "line" (let us call it the decision line)(in possibly, N dimensions) can classify the data.
Let the line parallel to this decision line, passing through the data points closest to the line on either side be called positive and negative edges of the "gutter". For a good classification, we need that the distance between the two gutters be the largest.

For a unit vector, perpendicular to the decision line be $\hat{w}$ and we choose real number b such that for a vector $\bar{x}$:

$$ \bar{x} \cdot \hat{w} + b \ge 1$$ 

for one cluster (let's call that the "positive" cluster) of data and 

$$ \bar{x} \cdot \hat{w} + b \le 1$$ 

for the other cluster (let's call that the "negative" cluster) of data

Let $y_i$ be 1, for "positive" data cluster and -1, for "negative" data cluster. Which means that, for some $i$:

$$ y_i(\bar{x}_i \cdot \hat{w} + b) \ge 1$$

Therefore, the width of the gutter is

$$\left( X_{+} - X_{-} \right) \cdot \frac{\bar{w}}{||\bar{w}||} = \left( 1 + b + 1 - b \right)\frac{1}{||\bar{w}||}  = \frac{2}{||\bar{w}||}$$

for $X_{+}\  and\  X_{-}$ on the positive and negative edge of the gutter.

Therefore, to maximize the width of the gutter, we have to minimize the following loss function:

$$cost(x) = \frac{1}{2}||\bar{w}||^2$$

under the conditions: 

$$ y_i(\bar{x}_i \cdot \bar{w} + b) = 1 $$

Using Lagranges Multipliers method on the function:

$$ L = \frac{1}{2}||\bar{w}||^2 - \sum_{i = 1} ^{n} \alpha_i \left(y_i(\bar{x}_i \cdot \bar{w} + b) - 1\right) $$

The minimum of the modified loss function is:

$$L = \sum_{i} \alpha_1 - \frac{1}{2}\sum_i \sum_j \alpha_i \alpha_j y_i y_j \bar{x}_i \cdot \bar{x}_j $$

> The important thing to notice in this is that the value depends on the dot product of the $\bar{x}_i s$. Now, suppose the data was not linearly classifiable, we can use a mapping ( $\phi(x_i)$ ) from the given datset to some other dataset which is linearly classifiable. What we need is the the function $K(x_i,x_j) = \phi(x_i)\cdot \phi(x_j)$ (the Kernel) and not the transformation $\phi$. This is the power :muscle: of SVMs.

# **Implementation**
The following programs for ML have been implemented as a part of evaluation for this week:
1. [Linear regression - Weather Dataset - Part 1](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%204/Linear_Regression_Weather_Dataset_1.ipynb)
2. [Linear regression - Weather Dataset - Part 2](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%204/Linear_Regression_Weather_Dataset_2.ipynb)
3. [Clustering - Iris Flower Dataset](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%204/Clustering_Iris_Flower_Dataset.ipynb)
4. [Support Vector Machine - Breast Cancer Dataset](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%204/SVM_Breast_Cancer_Dataset.ipynb)
5. [Neural networks - Recognising digits from the MNIST Dataset](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%204/Neural_Network_Classifying_Digits.ipynb)
