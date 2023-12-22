def parser(file_path):
    """
    Parse a file for the Advent of Code problem.

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
    return [node for node in network if node.endswith(letter)]

def all_nodes_end_with(nodes, letter):
    return all(node.endswith(letter) for node in nodes)

def navigate_one_step(instructions, network, start_node, index):
    instruction = instructions[index % len(instructions)]
    return network[start_node][0 if instruction == "L" else 1]

def navigate(instructions, network, start_letter, end_letter):
    starting_nodes = nodes_ending_with(network, start_letter)
    current_nodes = starting_nodes
    index = 0

    while True:
        if all_nodes_end_with(current_nodes, end_letter):
            return index + 1
        index += 1
        # print("Current nodes:", current_nodes)
        starting_nodes = current_nodes

# Main
file_path_test = "./day08_2_test.txt"
file_path_real = "./day08.txt"

instructions_test, network_test = parser(file_path_test)
instructions_real, network_real = parser(file_path_real)

nodes = nodes_ending_with(network_real, "A")
test = all_nodes_end_with(nodes, "A")
print("Real nodes:", nodes)
print("Test:", test)

result_test = navigate(instructions_test, network_test, "A", "Z")
print("Test result:", result_test)

result_real = navigate(instructions_real, network_real, "A", "Z")
print("Real result:", result_real)
