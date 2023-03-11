# (SOM) in Python using the MiniSom library:

'''
In this example, we first generate some random input data with 5 features. 
We then initialize a 10x10 SOM using the MiniSom library, and train it on the input data for 100 iterations.

After training the SOM, we visualize it using the pcolor function, which plots the distance map of the SOM. 
The distance map is a matrix where each element represents the average distance between the weights of a node and its neighboring nodes.
We can use this map to visualize the clustering of the input data in the SOM.

Finally, we plot the input data on top of the SOM using colored markers, where the color and shape of the markers represent different clusters of the data.
We first determine the winning node (i.e., the node with the closest weight) 
for each data point using the winner function of the SOM, and then plot the markers at the corresponding node coordinates.


'''
# CODE

import numpy as np
from minisom import MiniSom

# Generate some example data
data = np.random.rand(100, 5)

# Define the size of the SOM grid
grid_x = 10
grid_y = 10

# Initialize the SOM with the specified grid size and input dimension
som = MiniSom(grid_x, grid_y, 5)

# Train the SOM on the input data
som.train(data, 100)

# Visualize the SOM
from pylab import plot, axis, show, pcolor, colorbar
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x in enumerate(data):
    w = som.winner(x)  # get the coordinates of the winning node for data point x
    plot(w[0] + 0.5, w[1] + 0.5, markers[0], markerfacecolor='None', markeredgecolor=colors[0], markersize=12, markeredgewidth=2)
axis([0, grid_x, 0, grid_y])
show()








