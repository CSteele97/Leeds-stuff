# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:46:13 2018

@author: gycms
"""

import random
import matplotlib.pyplot

# Control how many agents there are
num_of_agents = 10

# Make coordinates change a number of times
num_of_iterations = 100

# Create new empty list
agents = [] 
# In agents list, we are adding two coordinates (y,x)
# That have a random number between 0 and 99
# Create a loop to make as many agents as desired
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


# Move coordinates randomly
# This next step creates a loop which gives a set of 
# conditions i.e. < or > 0.5. 
# [i][0] refers to the first value (0) in every agent (i) 
# i.e. y
# [i][1] refers to the second value (1) in every agent (i) 
# i.e. x
# By doing this twice, with a different random number, this
# makes the coordinate move twice each
for i in range(num_of_agents):
    if random.random() < 0.5:
        agents[i][0] += 1
        agents[i][1] += 1
    else:
        agents[i][0] -= 1
        agents[i][1] -= 1
    if random.random() < 0.5:
        agents[i][0] += 1
        agents[i][1] += 1
    else:
        agents[i][0] -= 1
        agents[i][1] -= 1
        
# This sets the coordinates to move 100 times each
for i in range(num_of_agents):
    if random.random() < 0.5:
        agents[i][0] += num_of_iterations
        agents[i][1] += num_of_iterations
    else:
        agents[i][0] -= num_of_iterations
        agents[i][1] -= num_of_iterations
    if random.random() < 0.5:
        agents[i][0] += num_of_iterations
        agents[i][1] += num_of_iterations
    else:
        agents[i][0] -= num_of_iterations
        agents[i][1] -= num_of_iterations

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# Note that the plot does not fit on the graph
# Can change the size of the graph to fit the coordinates
# Do not need to worry about this now