#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:50:22 2020

@author: shahriar
"""

from linear_algebra import *

def grad_des(X, y, theta, alpha, num_iters, m):
    # theta = transpose(theta)
        
    for i in range(0, num_iters):
        
        partial_derivative = matmul(transpose(X), matrix_subtraction( 
        matmul(X, theta), transpose(y) )) 
        
        gradient = inner_multiplication(partial_derivative, (alpha/m))
        
        theta =  matrix_subtraction(theta, gradient)
        

    return theta, partial_derivative, gradient

# m = length(y); % number of training examples
# J_history = zeros(num_iters, 1);

# for iter = 1:num_iters

#     % ====================== YOUR CODE HERE ======================
#     % Instructions: Perform a single gradient step on the parameter vector
#     %               theta. 
#     %
#     % Hint: While debugging, it can be useful to print out the values
#     %       of the cost function (computeCost) and gradient here.
#     %

#     theta = theta - (alpha/m) * X' * (X*theta - y);
#     %theta(iter) = theta(iter) - (alpha/m) * X' * sum(X*theta(iter) - y); 




    # % ============================================================

    # % Save the cost J in every iteration    
    # J_history(iter) = computeCost(X, y, theta);

    