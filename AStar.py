import networkx as nx

city_trails = nx.Graph()


true_dist = [
            #E1 E2   E3    E4    E5    E6    E7    E8    E9   E10   E11   E12   E13   14
            [0, 10, None, None, None, None, None, None, None, None, None, None, None, None],    #E1
            [None, 0, 8.5, None, None, None, None, None, 10, 3.5, None, None, None, None],      #E2
            [None, None, 0, 6.3, None, None, None, None, 9.4, None, None, None, 18.7, None],    #E3
            [None, None, None, 0, 13, None, None, 15.3, None, None, None, None, 12.8, 11],      #E4
            [None, None, None, None, 0, 3, 2.4, 30, None, None, None, None, None, None],        #E5
            [None, None, None, None, None, 0, None, None, None, None, None, None, None, None],  #E6
            [None, None, None, None, None, None, 0, None, None, None, None, None, None, None],  #E7
            [None, None, None, None, None, None, None, 0, 9.6, None, None, 6.4, None, None],    #E8
            [None, None, None, None, None, None, None, None, 0, None, 12.2, None, None, None],  #E9
            [None, None, None, None, None, None, None, None, None, 0, None, None, None, None],  #E10
            [None, None, None, None, None, None, None, None, None, None, 0, None, None, None],  #E11
            [None, None, None, None, None, None, None, None, None, None, None, 0, None, None],  #E12
            [None, None, None, None, None, None, None, None, None, None, None, None, 0, 5.1],   #E13
            [None, None, None, None, None, None, None, None, None, None, None, None, None, 0],  #E14
            ]

direct_dist = [
            #E1 E2   E3    E4    E5    E6    E7    E8    E9   E10   E11   E12   E13   14
            [0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],     #E1
            [None, 0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],      #E2
            [None, None, 0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],    #E3
            [None, None, None, 0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],    #E4
            [None, None, None, None, 0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],      #E5
            [None, None, None, None, None, 0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],   #E6
            [None, None, None, None, None, None, 0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],      #E7
            [None, None, None, None, None, None, None, 0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6],    #E8
            [None, None, None, None, None, None, None, None, 0, 13.5, 12.2, 10.9, 21.2, 26.6],  #E9
            [None, None, None, None, None, None, None, None, None, 0, 17.6, 24.2, 18.7, 21.2],  #E10
            [None, None, None, None, None, None, None, None, None, None, 0, 14.2, 31.5, 35.5],  #E11
            [None, None, None, None, None, None, None, None, None, None, None, 0, 28.8, 33.6],  #E12
            [None, None, None, None, None, None, None, None, None, None, None, None, 0, 5.1],   #E13
            [None, None, None, None, None, None, None, None, None, None, None, None, None, 0],  #E14
            ]

#Criação dos vértices
for station in range(14):
    city_trails.add_node(station + 1)

#Criação das arestas
for station_a in range(14):
    for station_b in range(14):
        station_curr = true_dist[station_a][station_b]

        if not (station_curr == None or station_curr == 0):
            city_trails.add_edge(station_a + 1, station_b + 1, weight = int(station_curr))

print(list(city_trails.edges))