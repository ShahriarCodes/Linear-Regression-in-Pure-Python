#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:37:46 2020

@author: shahriar
"""


from linear_algebra import *
from compute_cost import  *
from gradient_descent import *

fileref  = open('ex1data1.txt','r')
data = fileref.readlines()
# print(data)


X = []
y = []
for datum in data:
    X_and_y = datum.strip().split(',')
    X.append(float(X_and_y[0]))
    y.append(float(X_and_y[1]))



X_added_bias = transpose(X)
# print(X_added_bias)

m = len(X_added_bias)

for i in X_added_bias:
    i.insert(0,1)



Theta = zeros(2,1)

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





















# partial_derivative = matmul(transpose(X_added_bias), matrix_subtraction( 
#         matmul(X_added_bias, transpose(Theta)), transpose(y) )) 
        
# gradient = inner_multiplication(partial_derivative, (alpha/m))


# Theta =  matrix_subtraction(transpose(Theta), gradient)


# print(X)
# print(y)


# print(theta)


# print_matrix(X_added_bias)
# print_matrix(matmul([[1,2],[1,2]],[[1,2],[1,2]]))
# print(shape(X),shape(X_added_bias),shape(y))
# # print_matrix(matmul(X, X_added_bias))
# print(5*X_added_bias)


# row_vec = [1,2,3] ## TODO: convert into list of list
# col_vec = [[1],[2],[3]]
# matrix = [[1,2,3],[2,3,4],[3,4,5]]
# print(transpose(matmul(col_vec,transpose(col_vec))))
# print(matmul(col_vec,transpose(col_vec)))
# print(transpose([[6.1101, 5.5277, 8.5186, 7.0032, 5.8598]]))

# print(matrix_addition(row_vec,row_vec))