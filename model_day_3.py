import random
import operator
import matplotlib.pyplot
import agentframework
import matplotlib.animation

#ax.set_autoscale_on(False)

# Import the csv module in order to read in the txt file
import csv
# Make a blank list called environment
environment = []
# Create a new label called "f" and open the txt file containing the data
f = open('in.txt', newline='') 
# Use the csv reader function within the csv module to open the file
# Non-numeric converts the integers into floats
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# Set a loop - for every row in the file
for row in reader:
# Create a blank list called rowlist within this first loop 		
    rowlist = []
# Create a new loop within the first that appends every value within the row to the 
# rowlist
    for value in row:				
        rowlist.append(value)
# Once each value has been appended to a row within the rowlist, append each rowlist to
# the environment
# Note - this is indented one BEFORE the second loop and is therefore in-line with the
# original loop - this is because we want each rowlist to be added to the environment
# only once the rowlist has been processed
    environment.append(rowlist)
f.close()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

num_of_agents = 10
num_of_iterations = 1
neighbourhood = 20
agents = []

# Creates a new variable called a that is assigned to the Agent class in the agentframework
# file
a = agentframework.Agent(environment,agents)
print(a.y, a.x)
a.move()
print(a.y, a.x)
            
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
    
carry_on = True	

# Move the agents.
def update(frame_number):
        
    fig.clear()   
    matplotlib.pyplot.imshow(environment) 
    for j in range(num_of_iterations):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i][0],agents[i][1])
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    
for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = agents[x].distance_between(agents[z])
        print(distance)
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
matplotlib.pyplot.show()

# Display the environment that has been eaten by the agents
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.imshow(environment)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#matplotlib.pyplot.show()
