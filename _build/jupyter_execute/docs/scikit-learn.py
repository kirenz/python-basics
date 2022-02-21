#!/usr/bin/env python
# coding: utf-8

# # Scikit-learn
# 
# Scikit-learn is a popular open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection, model evaluation, and many other utilities.
# 
# - Simple and efficient tools for predictive data analysis
# - Built on NumPy, SciPy, and matplotlib
# 
# Scikit-learn provides dozens of built-in machine learning algorithms and models, called **estimators**. Each estimator can be fitted to some data using its fit method.
# 
# Let's create some simple data with two classes (0 and 1) and 3 features to demonstrate the usage of some classification algorithms:
# 
# class |feature 1 | feature 2 | feature 3
# --- | --- | --- | ---
# 0 | 1 | 2 | 3
# 1 | 11 | 12 | 13

# In[1]:


# Create data

X = [[ 1,  2,  3],  # 2 samples, 3 features
     [11, 12, 13]]

y = [0, 1]  # classes of each sample

print(list(zip(X, y)))


# Here is an example where we fit a `RandomForestClassifier` to our very basic data:

# In[2]:


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state=0) # create estimator and call it clf
clf.fit(X, y) # fit estimator to our data


# The **fit** method generally accepts 2 inputs:
# 
# The samples matrix (or design matrix) *X*:
# 
# - The size of X is typically (n_samples, n_features)
# - samples are represented as rows and features are represented as columns.
# 
# The target values *y* which are:
# 
# - real numbers for regression tasks
# - integers for classification (or any other discrete set of values) 
# - For unsupervized learning tasks, y does not need to be specified. 
# 
# y is usually 1d array where the i th entry corresponds to the target of the i th sample (row) of X.
# 
# Both X and y are usually expected to be *numpy* arrays or equivalent array-like data types, though some estimators work with other formats such as sparse matrices.
# 
# Once the estimator is fitted, it can be used for predicting target values of new data. You don’t need to re-train the estimator:

# In[3]:


clf.predict(X)  # predict classes of the training data


# In[4]:


clf.predict([[4, 5, 6], [14, 15, 16]])  # predict classes of new data


# In[5]:


clf.predict_proba(X)


# In[6]:


clf.score(X, y)


# Same procedure with different estimator:

# In[7]:


from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state=0)

clf.fit(X, y)

clf.predict(X)


# In[8]:


clf.predict_proba(X)


# In[9]:


clf.score(X, y)


# ## Important methods
# 
# Given a scikit-learn estimator object, the following methods are available:
# 
# Available in all estimators
# 
# - `.fit()` : fit training data. For supervised learning applications, this accepts two arguments: the data X and the labels y (e.g. model.fit(X, y)). For unsupervised learning applications, this accepts only a single argument, the data X (e.g. model.fit(X)).
# 
# Available in supervised estimators
# 
# - `.predict()` : given a trained model, predict the label of a new set of data. This method accepts one argument, the new data X_new (e.g. model.predict(X_new)), and returns the learned label for each object in the array.
# 
# - `.predict_proba()` : For classification problems, some estimators also provide this method, which returns the probability that a new observation has each categorical label. In this case, the label with the highest probability is returned by model.predict().
# 
# - `.score()` : for classification or regression problems, most estimators implement a score method. Scores are between 0 and 1, with a larger score indicating a better fit.
# 
# Available in unsupervised estimators
# 
# - `.predict()` : predict labels in clustering algorithms.
# 
# - `.transform()` : given an unsupervised model, transform new data into the new basis. This also accepts one argument X_new, and returns the new representation of the data based on the unsupervised model.
# 
# - `model.fit_transform()` : some estimators implement this method, which more efficiently performs a fit and a transform on the same input data.
