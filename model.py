# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:58:32 2018

@author: gycms
"""
# Set up variable
y0 = 50
x0 = 50

# Import and set a random number
import random
random_number = random.random()
# Move y randomly
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1   

# Move x randomly
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1    


# Set up variable
y1 = 50
x1 = 50

#Import and set a random number
random_number = random.random()
# Move 
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1   

if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1
if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1    
 

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq 
answer = sum**0.5


# Import and set a number at random between 0 and 99
y0 = random.randint(0,99)
x0 = random.randint(0,99)

random_number = random.random()
# Move y randomly
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1   

# Move x randomly
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1    
    
print (y0, x0)

# Set up variable at random between 0 and 99
y1 = random.randint(0,99)
x1 = random.randint(0,99)

#Import and set a random number
random_number = random.random()
# Move 
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1   

if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1
if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1    
    
print (y1, x1)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq 
answer = sum**0.5
print(answer)