def calculate_ways_to_win(races):
    def ways_to_win(time, record):
        ways = 0
        for t in range(time):
            if t * (time - t) > record:
                ways += 1
        return ways

    total_ways = 1
    for time, record in races:
        total_ways *= ways_to_win(time, record)

    return total_ways

# Example races from the puzzle description
example_races = [(7, 9), (15, 40), (30, 200)]
calculate_ways_to_win(example_races)


# New race data from the user
new_races = [(44, 283), (70, 1134), (70, 1134), (80, 1491)]

# Calculate the total number of ways to win with the new data
print(calculate_ways_to_win(new_races))
