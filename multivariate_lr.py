#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 07:55:46 2020

@author: shahriar
"""


from linear_algebra import *
from compute_cost import  *
from gradient_descent import *
from feature_normalize import *

fileref  = open('ex1data2.txt','r')
data = fileref.readlines()
# print(data)


X1 = []
X2 = [] 
y = []
for datum in data:
    X_and_y = datum.strip().split(',')
    X1.append(float(X_and_y[0]))
    X2.append(float(X_and_y[1]))
    y.append(float(X_and_y[2]))



X1_norm, X2_norm, y_norm = feature_normalized(X1,X2,y)

X = transpose([X1_norm]+[X2_norm])
y = transpose(y_norm)


X = twoD_to_oneD(X)

X_added_bias = copy_matrix(X)
# print(X_added_bias)


for ith_example in X_added_bias:
    ith_example.insert(0,1)



m = len(X_added_bias)     #rows number of features
n = len (X_added_bias[0]) #colums


Theta = zeros(n,1)

alpha = 0.01
max_iter = 1500




print('\nTesting the cost function ...\n')
# compute and display initial cost
cost  = cost_function(X_added_bias, y, Theta, m)
print('With theta = [0 ; 0]\nCost computed = {}\n'.format (cost))
print('Expected cost value (approx) 32.07\n')


print('\nTesting the cost function ...\n')
# compute and display initial cost
cost  = cost_function(X_added_bias, y, [[-1], [2]], m)
print('With theta = [[-1], [2]]\nCost computed = {}\n'.format (cost))
print('Expected cost value (approx) 54.24\n')





print('\nRunning Gradient Descent ...\n')
# run gradient descent
Theta, Partial_Derivative, Gradient = grad_des(X_added_bias, y, Theta, alpha, max_iter, m)




# print theta to screen
print('Theta found by gradient descent:\n')
print('{}\n'.format(Theta))
print('Expected theta values (approx)\n')
print(' -3.6303\n  1.1664\n\n')





print('Final cost function ...\n')
# compute and display final cost
cost  = cost_function(X_added_bias, y, Theta, m)
print('With theta = {}\nCost computed = {}\n'.format (Theta,cost))



predict1 = matmul([[1, 3.5]] , Theta)
print('For population = 35,000, we predict a profit of {}\n'.format(
      inner_multiplication(predict1,10000)))
predict2 = matmul([[1, 7]] , Theta)
print('For population = 70,000, we predict a profit of {}\n'.format(
    inner_multiplication(predict2,10000)))
