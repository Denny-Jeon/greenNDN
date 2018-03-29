

''' winter  (0 - 23)
    spring  (24 - 47)
    summer  (48 - 71)
    fall    (72 - 95) '''

# Normalized CO2 emission of Solar, Wind and Fossil power
CO2_SOLAR = 0.43
CO2_WIND = 1
CO2_FOSSIL = 0
# Total number of nodes in the graph_distance
N = 14
# Total power consumption of node
PC = 700

# Time of renewable energy generation
TIME = 75
RATIO = 0.2


import csv
import networkx as nx
import fnss
import copy


def calculate_greenness (node_id, time):

    if node_id == 0:
        with open ('/home/skjo/python/NSF/weather_data/node_0.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()

    elif node_id == 1:
        with open ('/home/skjo/python/NSF/weather_data/node_1.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()

    elif node_id == 2:
        with open ('/home/skjo/python/NSF/weather_data/node_2.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()

    elif node_id == 3:
        with open ('/home/skjo/python/NSF/weather_data/node_3.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


    elif node_id == 4:
        with open ('/home/skjo/python/NSF/weather_data/node_4.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


    elif node_id == 5:
        with open ('/home/skjo/python/NSF/weather_data/node_5.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


    elif node_id == 6:
        with open ('/home/skjo/python/NSF/weather_data/node_6.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()



    elif node_id == 7:
        with open ('/home/skjo/python/NSF/weather_data/node_7.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


    elif node_id == 8:
        with open ('/home/skjo/python/NSF/weather_data/node_8.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


    elif node_id == 9:
        with open ('/home/skjo/python/NSF/weather_data/node_9.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()



    elif node_id == 10:
        with open ('/home/skjo/python/NSF/weather_data/node_10.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


    elif node_id == 11:
        with open ('/home/skjo/python/NSF/weather_data/node_11.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()



    elif node_id == 12:
        with open ('/home/skjo/python/NSF/weather_data/node_12.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


    elif node_id == 13:
        with open ('/home/skjo/python/NSF/weather_data/node_13.csv', mode = 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == str(time+1):
                    solar_available = float (row[1])
                    wind_available = float (row[2])
                    g = (wind_available+CO2_SOLAR*solar_available)/PC
                    # print 'Available renewable energy: Solar %.2f, Wind %.2f' %(solar_available, wind_available)
                    # print 'Greenness of Node (%d) = %.2f' %(node_id, g)
                    return g
        f.close()


def generate_graph ():

    graph_distance = fnss.parse_topology_zoo('NSFNET.graphml').to_undirected()

    fnss.set_weights_constant(graph_distance, 1100.0, [(0, 1)])
    fnss.set_weights_constant(graph_distance, 600.0, [(1, 2)])
    fnss.set_weights_constant(graph_distance, 1600.0, [(0, 2)])
    fnss.set_weights_constant(graph_distance, 1000.0, [(1, 3)])
    fnss.set_weights_constant(graph_distance, 2800.0, [(0, 7)])
    fnss.set_weights_constant(graph_distance, 600.0, [(3, 4)])
    fnss.set_weights_constant(graph_distance, 2000.0, [(2, 5)])
    fnss.set_weights_constant(graph_distance, 2400.0, [(3, 10)])
    fnss.set_weights_constant(graph_distance, 800.0, [(4, 6)])
    fnss.set_weights_constant(graph_distance, 1100.0, [(4, 5)])
    fnss.set_weights_constant(graph_distance, 700.0, [(6, 7)])

    fnss.set_weights_constant(graph_distance, 2000.0, [(5, 13)])
    fnss.set_weights_constant(graph_distance, 1200.0, [(5, 9)])
    fnss.set_weights_constant(graph_distance, 900.0, [(9, 8)])
    fnss.set_weights_constant(graph_distance, 700.0, [(7, 8)])
    fnss.set_weights_constant(graph_distance, 800.0, [(10, 11)])
    fnss.set_weights_constant(graph_distance, 800.0, [(10, 12)])
    fnss.set_weights_constant(graph_distance, 500.0, [(8, 11)])
    fnss.set_weights_constant(graph_distance, 500.0, [(8, 12)])
    fnss.set_weights_constant(graph_distance, 300.0, [(11, 13)])
    fnss.set_weights_constant(graph_distance, 300.0, [(13, 12)])

    return graph_distance


def generate_green_graph (g):
   G = nx.DiGraph()
   # print 'g of nodes[dic] =', g.items()
   # print 'greenness of node 8', g[8]

   # Links between 0 and 1 (link id = 0)
   G.add_edge(0, 1, weight = 1 - g[1])
   G.add_edge(1, 0, weight = 1 - g[0])

   # Links between 1 and 2 (link id = 1)
   G.add_edge(1, 2, weight = 1 - g[2])
   G.add_edge(2, 1, weight = 1 - g[1])

   # Links between 0 and 2 (link id = 2)
   G.add_edge(0, 2, weight = 1 - g[2])
   G.add_edge(2, 0, weight = 1 - g[0])

   # Links between 1 and 3 (link id = 3)
   G.add_edge(1, 3, weight = 1 - g[3])
   G.add_edge(3, 1, weight = 1 - g[1])

   # Links between 0 and 7 (link id = 4)
   G.add_edge(0, 7, weight = 1 - g[7])
   G.add_edge(7, 0, weight = 1 - g[0])

   # Links between 3 and 4 (link id = 5)
   G.add_edge(3, 4, weight = 1 - g[4])
   G.add_edge(4, 3, weight = 1 - g[3])

   # Links between 2 and 5 (link id = 6)
   G.add_edge(2, 5, weight = 1 - g[5])
   G.add_edge(5, 2, weight = 1 - g[2])

   # Links between 3 and 10 (link id = 7)
   G.add_edge(3, 10, weight = 1 - g[10])
   G.add_edge(10, 3, weight = 1 - g[3])

   # Links between 4 and 6 (link id = 8)
   G.add_edge(4, 6, weight = 1 - g[6])
   G.add_edge(6, 4, weight = 1 - g[4])

   # Links between 4 and 5 (link id = 9)
   G.add_edge(4, 5, weight = 1 - g[5])
   G.add_edge(5, 4, weight = 1 - g[4])

   # Links between 6 and 7 (link id = 10)
   G.add_edge(6, 7, weight = 1 - g[7])
   G.add_edge(7, 6, weight = 1 - g[6])

   # Links between 5 and 13 (link id = 11)
   G.add_edge(5, 13, weight = 1 - g[13])
   G.add_edge(13, 5, weight = 1 - g[5])

   # Links between 5 and 9 (link id = 12)
   G.add_edge(5, 9, weight = 1 - g[9])
   G.add_edge(9, 5, weight = 1 - g[5])

   # Links between 9 and 8 (link id = 13)
   G.add_edge(9, 8, weight = 1 - g[8])
   G.add_edge(8, 9, weight = 1 - g[9])

   # Links between 7 and 8 (link id = 14)
   G.add_edge(7, 8, weight = 1 - g[8])
   G.add_edge(8, 7, weight = 1 - g[7])

   # Links between 1 and 3 (link id = 15)
   G.add_edge(10, 11, weight = 1 - g[11])
   G.add_edge(11, 10, weight = 1 - g[10])

   # Links between 10 and 12 (link id = 16)
   G.add_edge(10, 12, weight = 1 - g[12])
   G.add_edge(12, 10, weight = 1 - g[10])

   # Links between 8 and 11 (link id = 17)
   G.add_edge(8, 11, weight = 1 - g[11])
   G.add_edge(11, 8, weight = 1 - g[8])

   # Links between 8 and 12 (link id = 18)
   G.add_edge(8, 12, weight = 1 - g[12])
   G.add_edge(12, 8, weight = 1 - g[8])

   # Links between 11 and 13 (link id = 19)
   G.add_edge(11, 13, weight = 1 - g[13])
   G.add_edge(13, 11, weight = 1 - g[11])

   # Links between 13 and 12 (link id = 20)
   G.add_edge(13, 12, weight = 1 - g[12])
   G.add_edge(12, 13, weight = 1 - g[13])

   # nx.write_graphml(G, "NSFNET_g.graphml")
   # print '..... Graph file is generated ! .....'
   return G

   # Test if the weight can be inserted correctly
   print '************* Test Graph APIs *************************'
   print (nx.shortest_path(G, source=6, target=13, weight = 'weight'))
   print (nx.shortest_path_length(G, source=6, target=13, weight = 'weight'))

   print (nx.shortest_path(G, source=6, weight = 'weight'))

   print (nx.dijkstra_path(G, source=6, target=13, weight='weight'))
   print (nx.dijkstra_path_length(G, source=6, target=13, weight='weight'))

   print (G.neighbors(6))

   print '*********************************************************'


def check_duplication (graph, g_nodes):

    neighbor_pool = []      # List of GNs' neighbors with duplication
    gn_neighbors_dict = {}
    duplicated_list = []    # Nodes are stored in this list with duplication



######### Duplication check ##########
    # 1. Find out nodes who connect multiple GNs
    for i in g_nodes :
        neighbor_pool = neighbor_pool + graph.neighbors(i)
        # for j in graph.neighbors(str(i)) :
        #     neighbor_pool[g_nodes[i][j]] = graph.neighbors(str(i))

    # print '********** List of neighbors of GNs with duplication **********'
    # print neighbor_pool

    print '********** List of neighbors of GNs **********'
    print list(set(neighbor_pool))

    k = list(set(neighbor_pool))

    for i in neighbor_pool :
        if neighbor_pool.count(i) >=2 :
            # print 'Node connected multiple GNs [%d]' %int(i)
            duplicated_list = duplicated_list + [i]
            neighbors_list = list(set(duplicated_list))


    for i in g_nodes :
        if i in neighbors_list:
            neighbors_list.remove(i)

    print '********** Neighbor nodes with multiple GNs ********** '
    print neighbors_list


    for i in g_nodes :
        if i in k :
            k.remove(i)
    print '********** Lists of neighbor nodes ********** '
    print k     # list of neighboring nodes


    for i in g_nodes :
        gn_neighbors_dict[i] = graph.neighbors(i)
    # print '********** Dictionary of gn:[neighbors]: gn_neighbors_dict **********   '
    # print gn_neighbors_dict


    # 2. Decide which nodes to select (higher greenness value)
    dic_result = {}
    # list_g = []
    for i in neighbors_list :
        unduplicated_neighbors_dic = sort_neighbors_not_duplicated (gn_neighbors_dict, g_nodes, i, dic_result)

    # print '********** Unduplicated {neighbors: [GNs]} pairs ********** '
    # print unduplicated_neighbors_dic


    # Now calculate greenness of connected GN, then select maximized GN
    dic_final_pairs = {}
    for i in unduplicated_neighbors_dic.keys() :
        list_g = []
        # final_pairs_dic = {}
        for j in unduplicated_neighbors_dic[i] :
            # print 'greenness[%d] = %f' %(j, greenness[j])
            # make new list for neighboring greenness
            list_g = list_g + [greenness[j]]
            # print list_g
            greenest_node = list_g.index(max(list_g))
            # print max (list_g)
            # print list_g.index(max(list_g))
            # print list_g
        print 'GN of node [%s] = node [%d]' %(i, unduplicated_neighbors_dic[i][greenest_node])
        dic_final_pairs[i] = unduplicated_neighbors_dic[i][greenest_node]




    print '********** Duplication is resolved. Final pairs of "neighbor : its GN" are '
    print dic_final_pairs


    # [TODO] add more nodes who have single GN

    # a = list(set(neighbor_pool))

    # for i in neighbors_list :
    #     if i in a:
    #         a.remove(i)
    # print 'removed duplication list of neighbor', a

    for i in k :
        for j in gn_neighbors_dict:
            if i in gn_neighbors_dict[j]:
                dic_final_pairs[i] = j

    print '*************** Pairs of neighbor_node : GN  ***************'
    print dic_final_pairs
    return dic_final_pairs


def sort_neighbors_not_duplicated (gn_dict, gn_list, node_id, z):
    neighbor_nodes_list = {}
    temp_list = []

    for i in gn_list :
        if node_id in gn_dict[int(i)] :
            # print 'node %s is neighbor of node %s' %(node_id, i)
            temp_list = temp_list + [i]
            neighbor_nodes_list[node_id] = temp_list
            # print neighbor_nodes_list

    z.update(neighbor_nodes_list)

    return z


def calculate_green_path_neighbor_nodes (pair_dict, green_path_dict):
    # calculate original shortest path of each node --> don't need to this because it just send packet to GN
    green_path_neighbor_nodes_dict = {}

    # print ('pair_dict = ', pair_dict)
    # print ('green_path_dict = ', green_path_dict)
    #
    # print ('********** green path of node 5', green_path_dict[5])
    # print ('********** green path of node 11', green_path_dict[11])

    for key, value in pair_dict.iteritems():
        temp = {}

        temp[key] = copy.deepcopy(green_path_dict[value])

        for j in range(0, 14):
            if (temp[key][j][0] != key):
                temp[key][j].insert(0, key)

        green_path_neighbor_nodes_dict[key] = copy.deepcopy(temp[key])

    print 'neighbor dic= ', green_path_neighbor_nodes_dict

    #
    # # then bring GN's green path
    # for i in pair_dict.keys() :
    #
    #     green_path_neighbor_nodes_dict[i] = green_path_dict[pair_dict[i]]
    #     # green_path_neighbor_nodes_dict[i] = green_path_dict[pair_dict[i]]
    #
    #     # print ('green_path_neighbor_nodes_dict = ', i, green_path_neighbor_nodes_dict[i])
    #
    #
    #
    #
    #
    #
    #
    #     # for j in list(map(str, range(N))):      # make ['1', '2', ...]
    #     for j in range(0, N) :
    #         green_path_neighbor_nodes_dict[i][j].insert(0, i)

    # print '*********** green_path_neighbors =', green_path_neighbor_nodes_dict





    for i in pair_dict :
        print 'Green path from neighbor node [%d] = ' %i
        print green_path_neighbor_nodes_dict[i]

    return green_path_neighbor_nodes_dict


def calculate_green_path (graph, gn_id) :
    print 'Green path from green node [%d] = ' %(gn_id)
    print nx.single_source_dijkstra_path (graph, source = gn_id, weight = 'weight')

    return nx.single_source_dijkstra_path (graph, source = gn_id, weight = 'weight')


def calculate_shortest_path (graph, node_id) :
    print 'Shortest path from node [%d] = ' %(node_id)
    print nx.single_source_dijkstra_path (graph, source = node_id, weight = 'weight')

    return nx.single_source_dijkstra_path (graph, source = node_id, weight = 'weight')


if __name__ == '__main__':
    greenness = {}
    sorted_nodes_list = []
    green_nodes_list = []
    neighbor_gn_pair_dict = {}
    green_sum = 0           # to find out average greenness value
    final_green_path_gn_dict = {}
    final_shortest_path_nodes_dict = {}
    neighbor_node_list = []
    n_GN = int(RATIO * N)

    for node in range(0, N):
        green = calculate_greenness(node, TIME)
        greenness[node] = round(green, 4)
        green_sum = green_sum + green
        # if node == 13:
    print 'Greenness of nodes[dict] =', greenness.items()
    print 'greenness', greenness

    # Make directed Graph using greenness value, then return graph
    Graph = generate_green_graph(greenness)

    # Sort nodes with higher greenness values
    sorted_nodes_list = sorted(greenness.iterkeys(), key=lambda k: greenness[k], reverse=True)
    print 'Sorted greenness by node ID:', sorted_nodes_list
    print '********** Average greenness of time [%d] = %.4f' %(TIME, green_sum/N)

    print '********** GN ratio =', RATIO
    print '********** Number of Green Node(s) = %d' %n_GN

    green_nodes_list = sorted_nodes_list[:n_GN]
    print '********** Green Nodes =', green_nodes_list

    print '********** Neighbor nodes of Green Nodes **********'
    for i in green_nodes_list :
         print 'Neighbors of GN [%d] = ' %i, Graph.neighbors(i)

    neighbor_gn_pair_dict = check_duplication (Graph, green_nodes_list)
    # for example, {3: 10, 2: 5, 13: 5} 3--> neighbor node, 10 --> 3's GN

    # Calculate of green path from GNs
    for i in green_nodes_list :
        green_path_gn = calculate_green_path(Graph, i)
        # print green_path_gn
        final_green_path_gn_dict[i] = green_path_gn
    # print '********** Dictionary of green path of GN ==> GN : path to all destination **********'
    # print final_green_path_gn_dict

    # Calculate of shortest path from normal nodes

    k = generate_graph()   # native graph with weight

    # print nx.single_source_dijkstra_path (k, source = 1, weight = 'weight')

    normal_nodes = list(range(N))

    for i in range(len(green_nodes_list)):
        normal_nodes.remove(green_nodes_list[i])     # remove GNs

    # for i in neighbor_gn_pair_dict.keys():
    #     normal_nodes.remove(int(i))             # remove the node with multiple GNs

    # print '********** List of normal nodes (NOT GN & NOT node with multiple GN) **********'
    # print normal_nodes

    for i in neighbor_gn_pair_dict.keys():
        neighbor_node_list = neighbor_node_list + [int(i)]
    # print '********** List of neighbor node = ', neighbor_node_list           # node which has multiple GNs

    for i in neighbor_node_list :
        if i in normal_nodes :
            normal_nodes.remove(i)

    print '********** List of normal_node =', normal_nodes

    for i in normal_nodes:
        shortest_path_node = calculate_shortest_path(k, i)
        final_shortest_path_nodes_dict[i] = shortest_path_node
    

    print '********** List of neighbor node = ', neighbor_node_list
    final_green_path_neighbor_nodes_dict = calculate_green_path_neighbor_nodes (neighbor_gn_pair_dict, final_green_path_gn_dict)


    ''' Green path of GN is stored in                   ---> final_green_path_gn_dict   '''
    ''' Green path of associated GN is stored in        ---> final_green_path_neighbor_nodes_dict   '''
    ''' Shortest path of normal node is stored in       ---> final_shortest_path_nodes_dict   '''










