def count_ways_to_win(time, record):
    # Counts the number of ways to beat the record in a single race
    ways_to_win = 0
    for hold_time in range(time):
        speed = hold_time
        travel_time = time - hold_time
        distance = speed * travel_time
        if distance > record:
            ways_to_win += 1
    return ways_to_win

# Part One - Multiple Races
times = [7, 15, 30]
records = [9, 40, 200]
part_one_result = 1  # To multiply the number of ways for each race

for time, record in zip(times, records):
    ways = count_ways_to_win(time, record)
    part_one_result *= ways

# Part Two - Single Long Race
part_two_time = 71530
part_two_record = 940200
part_two_result = count_ways_to_win(part_two_time, part_two_record)

print(part_one_result)
print(part_two_result)

