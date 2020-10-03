# MLclass
Materials for my Machine Learning class(es).<br>
Given in English or French to doctoral and/or master students since 2012. In constant evolution.<br>

# Description
This course offers a discovery of the landscape of Machine Learning through some key algorithms. Although the first session tries to cover the full span of Machine Learning techniques, the subsequent sessions will focus on the Supervized Learning problem and will categorize the algorithms from four distinct points of view (the Bayesian perspective, linear separation, neural networks and ensemble methods). The approach taken mixes voluntarily hands-on practice in Python with theoretical and mathematical understanding of the methods. At the end of the course you will be able to make an informed choice between the main families of ML algorithms, depending on the problem at hand. You will have an understanding of the algorithmic and mathematical properties of each family of methods and you will have a basic practical knowledge of the Scikit-Learn and Keras Python libraries.

# Course goals
By the end of the class, you should be able to:
- implement a generic workflow of data analysis for your application field;
- know the main bottlenecks and challenges of data-driven approaches;
- link some field problems to their formal Machine Learning counterparts;
- know the main categories of Machine Learning algorithms and which formal problem they solve;
- know the name and principles of some key methods in Machine Learning:
    - SVM and kernel methods,
    - Naive Bayes Classification,
    - Gaussian Processes,
    - Artificial Neural Networks and Deep Learning,
    - Decision Trees,
    - Ensemble methods: Boosting, Bagging, Random Forests;
- know the basics of Scikit-Learn and Keras.

# Pre-requisites
- Basic level in Python (language fundamentals, numpy).
- Basic probability and optimization theory.

You must download and install an Anaconda distribution for the latest version of Python before the course ([https://anaconda.org/](https://anaconda.org/)). Alternatively (to downloading Anaconda), you'll need a working Python installation (latest version) with at least, Numpy, Scipy, Matplotlib and Jupyter installed.<br>
If you have a compatible OS, you can [install Docker](https://docs.docker.com/get-docker/) and Docker compose for ready-to use environments. 

Additional required Python packages:
- nltk
- keras (conda install keras)
- tensorflow (conda install tensorflow)
- graphviz (conda install graphviz)

# Typical class outline
Session 1: "Discovering Machine Learning"
- An introduction to Machine Learning
- A few words on the Unsupervized Learning problem
- A few words on the Reinforcement Learning problem
- Discovering scikit-learn

Session 2: "The geometric point of view"
- Optimal linear separation
- Support Vector Machines
- An introduction to kernel theory

Session 3: "The Bayesian point of view"
- The Bayes optimal classifier
- Naive Bayes Classifiers
- Gaussian Processes

Sessions 4 and 5: "Neuro-inspired computation"
- Neural networks
- Deep Learning
- Convolutional Neural Networks

Sessions 6 and 7: "Ensemble and committee-based methods"
- Decision trees
- Boosting
- Bagging
- Random Forests

# Bibliography
**The Elements of Statistical Learning.**<br>
T. Hastie, R. Tibshirani, J. Friedman.<br>
Springer Series in Statistics.<br>
[https://web.stanford.edu/~hastie/ElemStatLearn/](https://web.stanford.edu/~hastie/ElemStatLearn/)<br>

**Deep Learning**<br>
Ian Goodfellow and Yoshua Bengio and Aaron Courville<br>
MIT Press<br>
[https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)<br>

More references will be provided during the first session and during classes.
