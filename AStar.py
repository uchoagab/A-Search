import networkx as nx
import heapq

#entrada: estado inicial (estação/cor)
#saída: estado final, custo da fronteira/interação
#vel. m. trem = 0.5km/h; t = d*2

direct_dist_map = [
            #E1 E2   E3    E4    E5    E6    E7    E8    E9   E10   E11   E12   E13   E14
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

transfer_list = { 2: ["amarela","azul"], 
                  3: ["azul","vermelha"], 
                  4: ["azul","verde"], 
                  5: ["azul","amarela"],
                  8: ["amarela","verde"], 
                  9: ["amarela","vermelha"], 
                  13: ["verde","vermelha"]}

#(edge1, edge2, weight, color)
edge_list = [(1, 2, 10, "azul"),
            (2, 3, 8.5, "azul"),
            (2, 9, 10, "amarela"),
            (2, 10, 3.5, "amarela"),
            (3, 4, 6.3, "azul"),
            (3, 9,9.4, "vermelha"),
            (3, 13, 18.7, "vermelha"),
            (4, 5, 13, "azul"),
            (4, 8, 15.3, "verde"),
            (4, 13, 12.8, "verde"),
            (5, 6, 3, "azul"),
            (5, 7, 2.4, "amarela"),
            (5, 8, 30, "amarela"),
            (8, 9, 9.6, "amarela"),
            (8, 12, 6.4, "verde"),
            (9, 11, 12.2, "vermelha"),
            (13, 14, 5.1, "verde"),
            ]

#Criação das arestas
for edge in edge_list:
    city_trails.add_edge(edge[0], edge[1], weight = edge[2], color = edge[3])


#Função heuristica
def directDistance(startStation: int, finalStation: int) -> float:
    try:
        value = direct_dist_map[startStation - 1][finalStation - 1]
        return value * 2
    except TypeError:
        try:
            value = direct_dist_map[finalStation - 1][startStation - 1]
            return value * 2
        except Exception:
            print("Could not calculate the distance")

def astar_with_line_change(start, end, inicial_color, final_color, graph = city_trails):
    frontier = [(0, start, inicial_color)]
    lastFrontier = None
    came_from = {start: None}
    cost_so_far = {start: 0}
    transfer_check = {x: False for x in transfer_list.keys()}
    line_change_cost = 4  # Tempo de baldeação em minutos

    while frontier:
        current_cost, current_node, current_line = heapq.heappop(frontier)
        
        print(f"\n\nIndo para estação:", current_node, "com custo:", current_cost, "na linha:", current_line)

        if current_node == end and current_line == final_color:
            break

        neighbors = dict(graph[current_node])  # Criar uma cópia do dicionário para evitar problemas de mutabilidade
        print("Vizinhos:")
        if current_node in transfer_list.keys():
            if(current_line == transfer_list[current_node][0]):
                neighbors[current_node] = {'weight': 0, 'color': transfer_list[current_node][1]}
            else:
                neighbors[current_node] = {'weight': 0, 'color': transfer_list[current_node][0]}
            
        for next_node, edge_data in neighbors.items():
            new_cost = cost_so_far[current_node] + (edge_data['weight'] / 0.5)

            # Adiciona o tempo de baldeação se estiver mudando de linha
            if current_node in transfer_list.keys() and current_node == next_node:
                new_cost += line_change_cost


            if (edge_data['color'] == current_line and current_node != next_node) or current_node == next_node:
                total_cost = new_cost + directDistance(next_node, end)
                print(f"  {next_node}: g(x) = {new_cost} | h(x) = {directDistance(next_node, end)} | f(x) = {total_cost}  | aresta conexão {edge_data['color']}")
                if (next_node == current_node and transfer_check[current_node] != True) or (next_node not in cost_so_far or new_cost < cost_so_far[next_node]):
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + directDistance(next_node, end)
                    heapq.heappush(frontier, (priority, next_node, edge_data['color']))
                    if next_node != current_node:
                        came_from[next_node] = current_node
                    elif next_node == current_node:
                        transfer_check[current_node] = True
            last_node = current_node
            frontier = heapq.nsmallest(len(frontier), frontier)  # Sort na fronteira

        if lastFrontier is not None:
            temp_frontier = frontier.copy()
            for item in lastFrontier:
                if item not in temp_frontier:
                    temp_frontier.append(item)
            frontier = temp_frontier


        result = [(tuple[1], tuple[0]) for tuple in frontier]
        print("Fronteira:\n" + str(result))

    print("_____________________________________________________________")

    return came_from, cost_so_far

#Consulta o caminho percorrido no grafo
def recursive_search(dict, start, end, path):
    path.insert(0, end)
    if dict[end] == None:
        return path
    else:
        return recursive_search(dict, start, dict[end], path)
    

def main() -> None:   
    maintain = 1

    while maintain:
        start_station = int(input("Qual a estação de partida? "))
        inicial_color = input("Qual cor da estação inicial? ")
        goal_station = int(input("Qual a estação de destino? "))
        final_color = input("Qual cor da estação final? ")

        path = list()

        came_from, cost_so_far = astar_with_line_change(start_station, goal_station,inicial_color,final_color)
        
        print(f"\nCaminho percorrido: " + str(recursive_search(came_from, start_station, goal_station, path)))
        print("Tempo gasto: {:.2f} minutos\n".format(cost_so_far[goal_station]))

        ans = None
        while ans not in ("Y", "N"):
            try:
                ans = input("Deseja consultar outra viagem?(Y/N) ").upper()
                if ans == "Y":
                    maintain = 1
                elif ans == "N":
                    maintain = 0
            except:
                pass
    
    return 0


if __name__ == '__main__':
         main()
