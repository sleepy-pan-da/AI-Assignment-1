import json
from queue import PriorityQueue


# dictionaries of json files
dist_btw_2_nodes_dictionary = {} # this is for g(n)
graph_dictionary = {} # this is to find neighbours of node


def convert_json_files_to_dictionaries():
    f = open('Dist.json', )
    global dist_btw_2_nodes_dictionary
    dist_btw_2_nodes_dictionary = json.load(f)

    f = open('G.json', )
    global graph_dictionary
    graph_dictionary = json.load(f)


class Node: # generated_nodes_dictionary will have Nodes as values
    expanded : bool = False
    def __init__(self, path_cost_from_starting_node_to_current_node : int, previous_node : str) -> None:
        self.path_cost_from_starting_node_to_current_node = path_cost_from_starting_node_to_current_node
        self.previous_node = previous_node

def uniform_cost_search_1(start_node : str, end_node : str):
    # Initialise Data Structures
    nodes_to_expand : PriorityQueue = PriorityQueue() # nodes with the lowest cumulative distance will be expanded
    visited_nodes_dictionary = {}

    # Set up starting node
    nodes_to_expand.put((0,start_node)) # first element is cumulative distance, second element is the node label
    visited_nodes_dictionary[start_node] = Node(0, "0")

    while nodes_to_expand.not_empty:
        current_expanded_node = nodes_to_expand.get()[1]
        visited_nodes_dictionary[current_expanded_node].expanded = True

        if current_expanded_node == end_node:
            break

        neighbours_of_expanded_node = graph_dictionary[current_expanded_node]
        for i in neighbours_of_expanded_node:

            # don't explore expanded nodes, prevents traversal of nodes from looping
            if visited_nodes_dictionary.get(i) is not None and visited_nodes_dictionary.get(i).expanded:
                continue
            
            # g(n)
            path_cost_from_starting_node_to_neighbour = visited_nodes_dictionary[current_expanded_node].path_cost_from_starting_node_to_current_node 
            two_nodes_string : str = current_expanded_node + "," + i 
            path_cost_from_starting_node_to_neighbour += dist_btw_2_nodes_dictionary[two_nodes_string]

            if visited_nodes_dictionary.get(i) is not None:
                if path_cost_from_starting_node_to_neighbour < visited_nodes_dictionary[i].path_cost_from_starting_node_to_current_node:
                    # found a better route to node i

                    # update node i in generated_nodes_dictionary
                    visited_nodes_dictionary[i].path_cost_from_starting_node_to_current_node = path_cost_from_starting_node_to_neighbour
                    visited_nodes_dictionary[i].previous_node = current_expanded_node

                    # update node i in nodes_to_expand by
                    # popping out the elements in nodes_to_expand into temp_list to find node i
                    # afterwards push all the elements from temp_list back to nodes_to_expand
                    temp_list = []
                    while not nodes_to_expand.empty():
                        next_item = nodes_to_expand.get()
                        if next_item[1] == i:
                            # update the node i's totalcost
                            updated_node = (path_cost_from_starting_node_to_neighbour, i)
                            temp_list.append(updated_node)
                            break
                        temp_list.append(next_item)

                    for x in temp_list:
                        nodes_to_expand.put(x)
            else:
                nodes_to_expand.put((path_cost_from_starting_node_to_neighbour, i))
                # update generated_nodes_dictionary with neighbour node's info
                visited_nodes_dictionary[i] = Node(path_cost_from_starting_node_to_neighbour, current_expanded_node)
    
    shortest_path = [end_node]
    current_node = shortest_path[0]
    while True:
        node_to_backtrack_to = visited_nodes_dictionary[current_node].previous_node
        if node_to_backtrack_to == "0":
            break
        else:
            shortest_path.append(node_to_backtrack_to)  
            current_node = node_to_backtrack_to
    
    print("Shortest path: ", end = "")
    for node_label in shortest_path[::-1]:
        if node_label != end_node:
            print(node_label + "->", end = "")
        else:
            print(node_label + ".")

    print()    
    print("Shortest distance: " + str(visited_nodes_dictionary[end_node].path_cost_from_starting_node_to_current_node) + ".")





def main():
    convert_json_files_to_dictionaries()
    uniform_cost_search_1("1", "50")

if __name__ == "__main__":
    main()
