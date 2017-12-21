# AMD Homework 4 - Group 3

This project is a part of a course Algorithmic Methods of Data Mining
Aim of this project is to create a graph from a given dataset and visualize some interesting statistics. 

## Getting data

Data are saved in the folder *Test*
For our homework, we have two datasets:
1. *reduced_dblp.json* - This file contains a reduced dataset, which was used for testing and creating a script.
2. *full_dblp.json* - This is a full dataset for the final project. This file is not included in the Test folder because of its size.

To change the desired dataset, simply rewrite the name of the file you want to use in the *Modules.py* on the line **183**.
### Data

Reduced dataset is just a subset of the full data. Dataset contains the information about the conferences, publications and corresponding authors.

## To run a script:
	
Simply run *Modules.py* using Python in the command line in the folder with the dataset, or change the path to the desired file on the line **183**.

## Script description

For the manipulation of the data, we use the networkx package 1.10, which is really powerful tool for graph tasks.

### First part

The first part of the script creates a graph from a given data. This part runs automatically, because the graph is needed for every other part of the code.
Data is loaded through the loader function, which takes as a parameter name of the dataset or the path. Then we create the dictionaries for authors, publications and conferences.
They will be used later for the visualization and statistic part.
The graph itself contains authors as nodes. Edges are created with weights according to the Jaccard similarity.

Functions used for this part:

data = loader([name of dataset])
dictAuthor = Author(data)
dictPubl = Publ(data)
dictConf = Conf(data)
Gall = createGraph(dictAuthor)
Gall = addEdges(dictPubl)

Also we can plot the graph, but since the graph is too big, this task is really slow. 

After the graph is created, the program will ask the user for input - which action the user wants to perform:
	
### Second part

#### 2a 

User needs to put the ID of the conference(e.g. *3052*). The selected ID is found in the conference dictionary. The script then performs extraction of the subgraph, which is also drawn.
It also computes some statistics as degree, betweenness and closeness. These are then plotted on the log-log plots.

Used functions:
subgraph = Gall.subgraph(dictConf[a]) - create the subgraph according to the input
degree(Gall) - compute and plot the degree rank plot
closeness(Gall) - compute and plot the closeness rank plot
betweeness(Gall) - compute and plot the betweenness rank plot

#### 2b

User is asked for an ID of the author, whose subgraph he wants to visualize with the hop distance. Hop distance means how many steps are needed to get to the others.
For this function we used a function ego_graph from the networkx package. This function uses the given ID of the author as a centre of subgraph and creates the surroundings according to the desired hop distance.

Used functions:
hop_distance(Gall) - function takes graph as a parameter, but later asks the user for an ID of the author and the desired distance.
Output of this function is a subgraph with specific parameters. 

### Third part

#### 3a

This part computes shortest path between given nodes. For this exercise, we cannot use the functions from networkx package and we have to implement it by ourselves. 
In our solution we used Dijkstra algorithm with priority queue. 

To use a function: 
dijkstra(graph, source, target)
graph - specify the graph you want to use for calling the function
source - the starting node
target - the ending node

The output of this function is a weighted path between the nodes.


#### 3b

TBD


### Requirements

Python 3
Packages:
Networkx 1.1
Matplotlib
Heapq
