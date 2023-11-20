import networkx as nx

#entrada: estado inicial (estação/cor)
#saída: estado final, custo da fronteira/interação
#vel. m. trem = 0.5km/h; t = d*2

direct_dist_map = [
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

city_trails = nx.Graph()
frontier = list()

#Criação dos vértices
for station in range(14):
    city_trails.add_node(station + 1)

#(edge1, edge2, weight, color)
edge_list = [(1, 2, 10, "blue"),
            (2, 3, 8.5, "blue"),
            (2, 9, 10, "yellow"),
            (2, 10, 3.5, "yellow"),
            (3, 4, 6.3, "blue"),
            (3, 9,9.4, "red"),
            (3, 13, 18.7, "red"),
            (4, 5, 13, "red"),
            (4, 8, 15.3, "green"),
            (4, 13, 12.8, "green"),
            (5, 6, 3, "blue"),
            (5, 7, 2.4, "yellow"),
            (5, 8, 30, "yellow"),
            (8, 9, 9.6, "yellow"),
            (8, 12, 6.4, "green"),
            (9, 11, 12.2, "red"),
            (13, 14, 5.1, "green"),
            ]

#Criação das arestas
for edge in edge_list:
    city_trails.add_edge(edge[0], edge[1], weight = edge[2], color = edge[3])


#Função heuristica
def directDistance(inicial, final) -> float:
    try:
        value = direct_dist_map[inicial - 1][final - 1]
        return value * 2
    except TypeError:
        try:
            value = direct_dist_map[final - 1][inicial - 1]
            return value * 2
        except Exception:
            print("Could not calculate the distance")
            
#   city_trails[1][2]["color"] = "blue"
#   print(dict(city_trails[1][2]))
#   print(list(city_trails.edges))
#   print(list(nx.neighbors(city_trails, 7)))