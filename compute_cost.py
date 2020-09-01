#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:37:46 2020

@author: shahriar
"""
from linear_algebra import *


def cost_function(X, y, theta, m):
    
    J = 0
    
    loss = inner_sum(matrix_exponent(
    matrix_subtraction( 
        matmul(X, theta), transpose(y) ), 2 ))

    J = (1/ (2 * m)) * loss
    
    return J
