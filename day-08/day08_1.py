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
    for line in lines[2:]:
        if ' = ' in line:
            node, neighbors = line.split(' = ')
            neighbors = tuple(neighbors.strip('()').split(', '))
            node_network[node] = neighbors

    return instructions, node_network

def navigate(instructions, network, start_node, end_node):
    current_node = start_node
    step_count = 0
    index = 0

    # Optimiser en pré-calculant la longueur des instructions
    instructions_length = len(instructions)

    while current_node != end_node:
        index %= instructions_length  # Utiliser l'opérateur modulo pour éviter l'indexation hors limites
        instruction = instructions[index]

        current_node = network[current_node][1] if instruction == "R" else network[current_node][0]

        index += 1
        step_count += 1
        # print(current_node)  # Commenter pour améliorer les performances

    return step_count


# Main
file_path0 = "./day08_1_test.txt"
file_path1 = "./day08_1_test2.txt"
file_path2 = "./day08.txt"
instructions0, network0 = parser(file_path0)
result0 = navigate(instructions0, network0, "AAA", "ZZZ")
print("for test 1 : ",result0)

instructions1, network1 = parser(file_path1)
result1 = navigate(instructions1, network1, "AAA", "ZZZ")
print("for test 2 : ",result1)

instructions2, network2 = parser(file_path2)
result = navigate(instructions2, network2, "AAA", "ZZZ")
print("for real : ",result)
