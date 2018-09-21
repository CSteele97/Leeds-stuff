# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:46:13 2018

@author: gycms
"""

import random
import operator
import matplotlib.pyplot

# Create new empty list
agents = [] 
# In agents list, we are adding two coordinates (y,x)
# That have a random number between 0 and 99
# This replaces the y0 and x0 from the previous practical
agents.append([random.randint(0,99),random.randint(0,99)])

# Create random number between 0 and 1 to move the coordinate
random_number = random.random()
# Move y coordinate randomly
# Note - [0][0] refers to the first list, and the first
# value within that list - in this case is the y coordinate
if random_number < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
if random_number < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1   

# Move x randomly
# Note - [0][1] refers to the first list, and the second
# value within that list - in this case is the x coordinate
if random_number < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
if random_number < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1    
    
    
# In agents list, we are adding two coordinates (y,x)
# That have a random number between 0 and 99
# This replaces the y1 and x1 from the previous practical
agents.append([random.randint(0,99),random.randint(0,99)])

#Import and set a random number
random_number = random.random()
# Move y randomly 
if random_number < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
if random_number < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1   

#Move x randomly
if random_number < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
if random_number < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1    
    
print (agents)
# This will just look in each pair of agents and find the 
# largest overall number and the agent (or list) in which it
# is in
print(max(agents))
# This will look at to find the largest number of a certain
# variable in all of the agents (list) i.e. in this case 
# by setting to '1', makes it look for the largest second 
# variable in each agent (list).
# This is the x coordinate in this case.
print(max(agents, key=operator.itemgetter(1)))
# This will look at to find the largest number of a certain
# variable in all of the agents (list) i.e. in this case 
# by setting to '0', makes it look for the largest first 
# variable in each agent (list).
# This is the y coordinate in this case.
print(max(agents, key=operator.itemgetter(0)))


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()