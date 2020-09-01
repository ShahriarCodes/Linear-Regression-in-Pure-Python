#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:37:46 2020

@author: shahriar
"""


def zeros(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have

        :return: list of lists that form the matrix
    """
    zero_M = []
    while len(zero_M) < rows:
        zero_M.append([])
        while len(zero_M[-1]) < cols:
            zero_M[-1].append(0.0)

    return zero_M

def ones(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have

        :return: list of lists that form the matrix
    """
    ones_M = []
    while len(ones_M) < rows:
        ones_M.append([])
        while len(ones_M[-1]) < cols:
            ones_M[-1].append(1)

    return ones_M


def eye(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix

        :return: a square identity matrix
    """
    IdM = zeros(n, n)
    for i in range(n):
        IdM[i][i] = 1.0

    return IdM

def transpose(M):
    """
    Returns a transpose of a matrix.
        :param M: The matrix to be transposed

        :return: The transpose of the given matrix
    """
    # Section 1: if a 1D array, convert to a 2D array = matrix
    if not isinstance(M[0],list):
        M = [M]

    # Section 2: Get dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 3: MT is zeros matrix with transposed dimensions
    MT = zeros(cols, rows)

    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT


def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied

        :return: A copy of the given matrix
    """
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 2: Create a new matrix of zeros
    MC = zeros(rows, cols)

    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC


def print_matrix(M, decimals=3):
    """
    Print a matrix one row at a time
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x,decimals)+0 for x in row])


def shape(M):
    if isinstance(M,list) ==True and isinstance(M[0], list) == True:
        rowsM = len(M)
        colsM = len(M[0])
        # return 'Its a {} X {} matrix'.format(rowsM,colsM)
        return rowsM , colsM
    elif isinstance(M,list) ==True and isinstance(M[0], list) == False:
        M_ = [M]
        print(M)
        rowsM_ = len(M_)
        colsM_ = len(M_[0])
        # return 'Its a {} X {} matrix'.format(rowsM_,colsM_)
        return rowsM_ , colsM_



def matrix_addition(A, B):
    """
    Adds two matrices and returns the sum
        :param A: The first matrix
        :param B: The second matrix

        :return: Matrix sum
    """
    # Section 1: Ensure dimensions are valid for matrix addition
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]

    dimB = shape(B)
    rowsB = dimB[0]
    colsB = dimB[1]
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    # Section 2: Create a new matrix for the matrix sum
    C = zeros(rowsA, colsB)

    # Section 3: Perform element by element sum
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] + B[i][j]

    return C

def matrix_subtraction(A, B):
    """
    Subtracts matrix B from matrix A and returns difference
        :param A: The first matrix
        :param B: The second matrix

        :return: Matrix difference
    """
    # Section 1: Ensure dimensions are valid for matrix subtraction
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]

    dimB = shape(B)
    rowsB = dimB[0]
    colsB = dimB[1]
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    # Section 2: Create a new matrix for the matrix difference
    C = zeros(rowsA, colsB)

    # Section 3: Perform element by element subtraction
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]

    return C




def matmul(A, B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    #check if 1D or 2D list
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]

    dimB = shape(B)
    rowsB = dimB[0]
    colsB = dimB[1]
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')

    # Section 2: Store matrix multiplication in a new matrix
    C = zeros(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C


def matrix_exponent(A, x):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    #check if 1D or 2D list
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]


    # Section 2: Create a new matrix of zeros
    ME = zeros(rowsA, colsA)

    # Section 3: Copy values of M into the copy
    for i in range(rowsA):
        for j in range(colsA):
            ME[i][j] = A[i][j] **x

    return ME

def inner_addition(A, x):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    #check if 1D or 2D list
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]


    # Section 2: Create a new matrix of zeros
    IA = zeros(rowsA, colsA)

    # Section 3: Copy values of M into the copy
    for i in range(rowsA):
        for j in range(colsA):
            IA[i][j] = A[i][j] + x

    return IA

def inner_subtraction(A, x):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    #check if 1D or 2D list
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]


    # Section 2: Create a new matrix of zeros
    IS = zeros(rowsA, colsA)

    # Section 3: Copy values of M into the copy
    for i in range(rowsA):
        for j in range(colsA):
            IS[i][j] = A[i][j] - x

    return IS


def inner_multiplication(A, x):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    #check if 1D or 2D list
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]


    # Section 2: Create a new matrix of zeros
    IM = zeros(rowsA, colsA)

    # Section 3: Copy values of M into the copy
    for i in range(rowsA):
        for j in range(colsA):
            IM[i][j] = A[i][j] *x

    return IM

def inner_division(A, x):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    #check if 1D or 2D list
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]


    # Section 2: Create a new matrix of zeros
    ID = zeros(rowsA, colsA)

    # Section 3: Copy values of M into the copy
    for i in range(rowsA):
        for j in range(colsA):
            ID[i][j] = A[i][j] / x

    return ID

        

def inner_sum(A):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]
    
    IS = 0
    # for i in range(shape(A)[0]): #select all rows
    for i in range(rowsA):
        for j in range(colsA):
            IS += A[i][j]
    
    return IS
    # return sum(map(sum,A)) # this also works without any extra code 



def row_sum(A):
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]
    
    ID = 0
    RS = []
    # for i in range(shape(A)[0]): #select all rows
    for i in range(rowsA):
        ID = 0
        for j in range(colsA):
            ID += A[i][j]
        # print(ID)
        RS.append(ID)
    return transpose(RS)

def col_sum(A):
    
    
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]
    
    ID = 0
    CS = []
    # for i in range(shape(A)[0]): #select all rows
    for j in range(colsA):
        ID = 0
        for i in range(rowsA):
            ID += A[i][j]
        # print(ID)
        CS.append(ID)
    return CS

def mean(A):
    """
    Returns the Mean of the matrix A 
        :param CS: Sum of all row in order of columns of Matrix A 
        :param MN: Element wise division of Matrix A by number of rows

        :return: A 1X(number of columns) matrix having the mean of every rows 
    """
    #check the dimension of the matrix
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1]

    CS = col_sum(A)
    MN = inner_division([CS], rowsA) 

    # Section 2: Create a new matrix of zeros
    

    return MN

def twoD_to_oneD(A):
    
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1] 
    
    b = []
    
    for i in range(rowsA):
        for j in range(colsA):
             b.append(A[i][j])
    
    return b

def nD_to_oneD(A, x):
    
    dimA = shape(A)
    rowsA = dimA[0]
    colsA = dimA[1] 
    
    b = []
    
    while x > 1:
        A = twoD_to_oneD(A)
                
        x -= 1
    return A



# def std_dev(A):
#     dimA = shape(A)
#     rowsA = dimA[0]
#     colsA = dimA[1] 
    
    
#     MN = mean(A)
    
#     # ID = 0
#     STD =[]
    
    
    
#     for i in range(rowsA):
#         # ID = 0
#        # for j in range(colsA):
#        ID = matrix_subtraction([A[i][:]], MN)    
#        STD.append(ID)
    
#     STD = twoD_to_oneD(STD) 
    

#     STD = inner_division(col_sum(STD) , rowsA)
#     return STD


def sqrt(x):
    return x**(0.5)    




def calculateMean(data):

    summmation = 0.0
    mean = 0.0
    standardDeviation = 0.0

    

    for i in range(len(data)):
    
        summmation += data[i]
    

    mean = summmation/len(data)
    
    return mean


def calculateSD(data):

    summmation = 0.0
    mean = 0.0
    standardDeviation = 0.0

    

    for i in range(len(data)):
    
        summmation += data[i]
    

    mean = summmation/len(data)

    for i in range(len(data)):
        standardDeviation += pow(data[i] - mean, 2)

    return sqrt(standardDeviation / (len(data)-1))
    





