#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:06:00 2020

@author: shahriar
# """
# [X_norm, y_norm, mu, sigma, mu_y, sigma_y] >>> output

from linear_algebra import  *

def feature_normalized(X1,X2, y):


    # X_norm = copy_matrix(X)
    # mu = zeros(1, shape(X)[1])
    # sigma = zeros(1, shape(X)[1])
    # num_features = shape(X)[1]
    
    
    # y_norm = copy_matrix(y)
    # mu_y = zeros(1, shape(y)[1])
    # sigma_y = zeros(1, shape(y)[1])
    # num_features_y = shape(y)[1]
    
    
    mu_X1 = calculateMean(X1)
    sigma_X1 = calculateSD(X1)
    X1_norm = inner_division(inner_subtraction(transpose(X1), mu_X1), sigma_X1)
    
    mu_X2 = calculateMean(X2)
    sigma_X2 = calculateSD(X2)
    X2_norm = inner_division(inner_subtraction(transpose(X2), mu_X2), sigma_X2)
    
    
    mu_y = calculateMean(y)
    sigma_y = calculateSD(y)
    y_norm = inner_division(inner_subtraction(transpose(y), mu_y), sigma_y)
    
    
    
    
    return X1_norm, X2_norm, y_norm
    
#     for i = 1:num_features,
#       mu(i) = mean(X(:,i));
#       sigma(i) = std(X(:,i));
     
#     end;
    
#     X_norm = (X - mu)./sigma;
    
#     for i = 1:num_features_y,
    
#       mu_y(i) = mean(y(:,i));
#       sigma_y(i) = std(y(:,i));
      
#     end;
    
#     y_norm = (y - mu_y)./sigma_y

# end