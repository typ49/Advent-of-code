def parse_input(input_data):
    # Split input data into rules and updates sections
    rules_section, updates_section = input_data.strip().split("\n\n")
    # Parse rules
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.split('\n')]
    # Parse updates
    updates = [list(map(int, line.split(','))) for line in updates_section.split('\n')]
    return rules, updates

def is_update_correct(rules, update):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def calculate_sum_of_middle_pages(input_data):
    rules, updates = parse_input(input_data)
    correct_updates = [update for update in updates if is_update_correct(rules, update)]
    middle_pages = [find_middle_page(update) for update in correct_updates]
    return sum(middle_pages)

# Sample input as a multiline string
test_data = open('AOC-2024/day-05/test.txt').read()
input_data = open('AOC-2024/day-05/input.txt').read()

print(calculate_sum_of_middle_pages(test_data))
print(calculate_sum_of_middle_pages(input_data))
