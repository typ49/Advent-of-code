def parser(file_path):
    """
    Parse a file for the Advent of Code problem of day 8.

    Args:
    file_path (str): The path to the file to parse.

    Returns:
    tuple: A string representing navigation instructions and a dictionary representing the node network.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    instructions = lines[0]

    node_network = {}
    for line in lines[2:]:  # Starting from the third line
        if ' = ' in line:
            node, neighbors = line.split(' = ')
            neighbors = tuple(neighbors.strip('()').split(', '))
            node_network[node] = neighbors

    return instructions, node_network

def nodes_ending_with(network, letter):
    """
    find all the nodes in a network who end with the letter given

    Args:
    network (dictionary) : a node network
    letter (char) ; the char which node name should end with

    Returns:
    List: A liste of nodes who have there name end with the letter given
    """
    res = []
    for node in network:
        if node.endswith(letter):
            res.append(node)
    return res

def all_nodes_end_with(nodes, letter):
    """
    Verify if all the node name in nodes list end with the given letter

    Args:
    nodes (list) : a list of node
    letter (char) : the char which node name should end with

    Returns:
    True if all the node name end with the given letter
    False overwise
    """
    for node in nodes:
        if not node.endswith(letter):
            return False
    return True

def navigate_one_step(instructions, network, nodes, index):
    """
    give the next step from a node to another with the instruction given

    Args:
    instructions (list of char) : the list of instruction
    network (dictionary of node) : the dictionary of the node
    nodes (list of nodes) : the nodes to check
    index (int) : the index to find the right instruction in "instructions"

    Returns:
    the nodes one step ahead
    """
    res = []
    instruction = instructions[index % len(instructions)]
    for node in nodes:
        if instruction == 'L':
            res.append(network[node][0])
        else:
            res.append(network[node][1])
    return res
            


def navigate(instructions, network, start_letter, end_letter):
    """
    start with the node name who end with start_letter and go to the node name end with end_letter

    Args:
    instructions (list of char) : list of instructions
    network (dictionary of node) : all the node
    start_letter (char) : letter to start with 
    end_letter (char) : letter to end with

    Returns:
    the number of step to go to a list of node who end with start_letter to a list of node who end with end_letter
    """
    res = 0
    index = 0
    current_nodes = nodes_ending_with(network, start_letter)
    print("starting nodes : ",current_nodes)
    while not all_nodes_end_with(current_nodes, end_letter):
        current_nodes = navigate_one_step(instructions, network, current_nodes, index)
        # print("current nodes : ",current_nodes)
        index += 1
        res += 1
    return res
    

# Main
file_path_test = "./day08_2_test.txt"
file_path_real = "./day08.txt"

instructions_test, network_test = parser(file_path_test)

res = navigate(instructions_test, network_test, 'A', 'Z')

print(res)

instructions_real, network_real = parser(file_path_real)

res = navigate(instructions_real, network_real, 'A', 'Z')

print (res)

