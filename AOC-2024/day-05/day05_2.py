from collections import defaultdict, deque

def parse_input(input_data):
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.split('\n')]
    updates = [list(map(int, line.split(','))) for line in updates_section.split('\n')]
    return rules, updates

def is_update_correct(rules, update):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def reorder_update(update, rules):
    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}
    
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1

    queue = deque([node for node in update if in_degree[node] == 0])
    ordered_update = []

    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update if len(ordered_update) == len(update) else sorted(update)

def find_middle_page(update):
    return update[len(update) // 2]

def calculate_sum_of_middle_pages(input_data):
    rules, updates = parse_input(input_data)
    
    incorrect_updates = [update for update in updates if not is_update_correct(rules, update)]
    

    reordered_updates = [reorder_update(update, rules) for update in incorrect_updates]
    
    
    all_middle_pages = [find_middle_page(update) for update in reordered_updates]
    
    
    return sum(all_middle_pages)

# Sample input as a multiline string
test_data = open('AOC-2024/day-05/test.txt').read()
input_data = open('AOC-2024/day-05/input.txt').read()

print(calculate_sum_of_middle_pages(test_data))
print(calculate_sum_of_middle_pages(input_data))
