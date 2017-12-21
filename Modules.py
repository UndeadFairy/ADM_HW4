import json
import networkx as nx
import matplotlib.pyplot as plt
import itertools
import heapq

## first part
def loader(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data


def Author(file):
    dictAuthor = {}
    for i in range(len(file)):
        for author in file[i]["authors"]:
            try:
                dictAuthor[author["author_id"]] += [(file[i]["id_publication_int"])]
            except:
                dictAuthor[author["author_id"]] = [(file[i]["id_publication_int"])]

    return dictAuthor

    
def Publ(file):
    dictPubl = {}
    for i in range(len(file)):
        for author in file[i]["authors"]:
            try:
                dictPubl[file[i]["id_publication_int"]] += [(author["author_id"])]
            except:
                dictPubl[file[i]["id_publication_int"]] = [(author["author_id"])]
    return dictPubl
    

def Conf(file):
    dictConf = {}
    for i in range(len(file)):
        for author in file[i]["authors"]:
            try:
                dictConf[file[i]["id_conference_int"]] += [(author["author_id"])]
            except:
                dictConf[file[i]["id_conference_int"]] = [(author["author_id"])]

    return dictConf

def createGraph(dictAuthor):
    Gall = nx.Graph()
    for k, v in dictAuthor.items():
        Gall.add_node(k, id=v[0])
    return Gall

def JaccardDistance(a,b):
    num = (len(list(set(a)&set(b))))
    den = len(list(set(a)|set(b)))
    j = 1 - num/den
    return j

def addEdges(dictPubl):
    for k, v in dictPubl.items():
        for i in itertools.combinations(v, 2):  # all combinations between 2 values of v (author_id)
            Gall.add_edge(i[0], i[1], weight=JaccardDistance(dictAuthor[i[0]], dictAuthor[i[1]]))
    return Gall

def draw_graph(graph):
    nx.draw_networkx(graph)
    plt.show()
    
    
## Second part
def degree(graph):
    degree_sequence = sorted(nx.degree_centrality(graph),reverse=True)
    plt.loglog(degree_sequence,'b-',marker='o')
    plt.title("Degree rank plot")
    plt.ylabel("Degree")
    plt.xlabel("Rank")
    plt.show()
    
    
def closeness(graph):
    close_centrality = nx.closeness_centrality(graph)
    values_centrality = [i for i in close_centrality.values()]
    plt.hist(values_centrality)
    plt.title("Closeness rank plot")
    plt.ylabel("Closeness")
    plt.xlabel("Rank")
    plt.show()

    
def betweeness(graph):
    bet = nx.betweenness_centrality(graph, weight= 'weight')
    bet2 = sorted(list(bet.values()), reverse=True)
    #values_betweeness = [i for i in bet.values()]
    plt.hist(bet2)
    plt.title("Betweeness rank plot")
    plt.ylabel("Betweeness")
    plt.xlabel("Rank")
    plt.show()
    
    

def hop_distance(graph):
    id_author = int(input('Please, give me an ID of the Author: '))
    neighbor = int(input('Please, tell me, what distance of neighbors do you want?: '))
    sub = nx.ego_graph(graph, id_author, radius = neighbor)
    nx.draw_networkx(sub)
    plt.show()
    
    
## third part
def dijkstra(graph, source, target):
    import heapq
    visited = set()
    heap_distance = []
    INF = ((1<<63) - 1)//2
    #initialization 
    try:
        for node in graph.nodes():
            if node != source:
                heapq.heappush(heap_distance, (INF, node))
            else:
                heapq.heappush(heap_distance, (0, node))
        # for check if the values are connected
        if nx.has_path(graph, source, target):

            while heap_distance:
                wanted_distance, w = heapq.heappop(heap_distance)
                if w == target:
                    break #found him!

                #marking our journey   
                visited.add(w)

                nblist = []
                for x in graph.neighbors(w):
                    if x not in visited:
                        nblist.append(x)

                for nd in nblist:
                    new_distance = wanted_distance + graph.get_edge_data(w, nd)['weight']
                    heapq.heappush(heap_distance, (new_distance, nd))
            return (wanted_distance)
        else:
            print ('You shall not path!!!')
    except:
        print('Choose node from graph, please!')

def function2a(Gall, dictConf):
    a = int(input('Give me an ID of conference, please: '))
    subgraph = Gall.subgraph(dictConf[a])
    nx.draw_networkx(subgraph)
    plt.show()
    degree(subgraph)
    closeness(subgraph)
    betweeness(subgraph)

def function2b(Gall):
    hop_distance(Gall)

def function3a(Gall):
    Aris = 256176
    another_guy = int(input('Who do you want to connect?(ID please): '))
    print(dijkstra(Gall, Aris, another_guy))

#[123456,378531,256716]
def function3b(Gall):
    nodes_list = list(map(int,input('Give me numbers: ').split(",")))
    for node in Gall.node:
        for node_l in nodes_list:
            print("I' m examining these nodes (Example: 123456,378531,256716) :" + str((node_l, node)))
            if node_l in nx.node_connected_component(Gall, node):
                try:
                    print("The nodes:" + str((node, node_l)) + "are connected with distance" + str(
                        dijkstra(Gall, node, node_l)))
                except:
                    print("Not connected")
            else:
                print("The nodes are not connected")


data = loader('reduced_dblp.json')
dictAuthor = Author(data)
dictPubl = Publ(data)
dictConf = Conf(data)
Gall = createGraph(dictAuthor)
Gall = addEdges(dictPubl)
#draw_graph(Gall)

n = 0
while n != 'save me':
    n = input("Enter the number of part you want (2a, 2b, 3a, 3b) or type 'save me', if you want to quit: ")
    if n == '2a':
        function2a(Gall, dictConf)
    elif n =='2b':
        function2b(Gall)
    elif n =='3a':
        function3a(Gall)
    elif n =='3b':
        function3b(Gall)
    elif n == 'save me':
        print ('It was pleasure to meat you')
    else:
        print ('Choose another part, please')

