# Name: Alice Mee Seon Chung
# hw3.py

##### Template for Homework 3, exercises 1 -  ######
import math
import random

# ********** Exercise 1 ********** 

# Define is_divisible function here
def is_divisible(m, n):
    '''
    test m is divisible by n

    Inputs: two itegers m and n
    Return: Boolean value, True if m is divisible by n, otherwise False
    '''
    if n == 0:
        return False
    if (m % n) == 0:
        return True
    else:
        return False


# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print (is_divisible(10, 5))  # This should return True
print (is_divisible(18, 7))  # This should return False
print (is_divisible(42, 0))  # What should this return?

# ********** Exercise 2 ********** 

# Define not_equal function here
def not_equal(m,n):
    '''
    test m is not equal to n

    Inputs: two itegers m and n
    Return: Boolean value, True if m is not equal to n, otherwise False
    '''
    if m == n:
        return False
    else:
        return True

# Test cases for not_equal
print (not_equal(10, 5))  # This should return True
print (not_equal(18, 18))  # This should return False

# ********** Exercise 3 ********** 

## 1 - multadd function
def multadd(a, b, c):
    result = a * b + c
    return result

## 2 - Equations
angle_test = multadd((math.cos(math.pi/4)), 1/2, math.sin(math.pi/4)) 
ceiling_test = multadd(math.log(12,7), 2, math.ceil(276/19))

# Test Cases
# angle_test =
print ("sin(pi/4) + cos(pi/4)/2 is:")
print (angle_test)

# ceiling_test =
print ("ceiling(276/19) + 2 log_7(12) is:")
print (ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    randomnum = random.randint(0,100)
    print("Random Number: ",randomnum)
    if is_divisible(randomnum, 3):
        return True
    else:
        return False

# Test Cases
for i in range(5):
    print(rand_divis_3())


