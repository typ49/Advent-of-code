def map_number(number, map_list):
    """
    Map a number from the source to the destination using the provided map list.
    Each entry in the map list is a tuple of (destination start, source start, range length).
    """
    for dest_start, source_start, length in map_list:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number  # Return the same number if it's not in the map


def parse_file(file_path):
    """
    Parse the file to extract seeds and maps.
    """
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')

    seeds = [int(x) for x in lines[0].split(':')[1].split()]
    
    # Extract maps from the file
    maps = []
    current_map = []
    for line in lines[2:]:  # Skip the first two lines (seeds and empty line)
        if line.strip() == '':
            if current_map:
                maps.append(current_map)
                current_map = []
            continue
        if line.endswith('map:'):  # Skip map titles
            continue
        current_map.append(tuple(map(int, line.split())))
    if current_map:
        maps.append(current_map)

    return seeds, maps




def process_seeds(seeds, maps):
    location_numbers = []
    for seed in seeds:
        number = seed
        for map_list in maps:
            number = map_number(number, map_list)
        location_numbers.append(number)
    return min(location_numbers)

# main
file_path = './input.txt'
seeds, maps = parse_file(file_path)
lowest_location = process_seeds(seeds, maps)
print(lowest_location)
