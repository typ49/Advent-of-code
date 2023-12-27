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

# Nouvelles données pour les courses
times_new = [44, 70, 70, 80]
records_new = [283, 1134, 1134, 1491]

# Combinaison des temps et des distances des courses pour la partie 2 comme une seule longue course
part_two_time_new = int("".join(map(str, times_new)))  # Concaténation des temps et conversion en entier
part_two_record_new = int("".join(map(str, records_new)))  # Concaténation des records et conversion en entier

# Calcul du nombre de façons de gagner pour cette longue course unique en utilisant la fonction définie précédemment
part_two_result_new = count_ways_to_win(part_two_time_new, part_two_record_new)

# Résultat : le temps combiné, le record combiné et le nombre de façons de gagner
part_two_time_new, part_two_record_new, part_two_result_new

print("Partie 2 :")
print(f"Temps combiné : {part_two_time_new}")
print(f"Record combiné : {part_two_record_new}")
print(f"Nombre de façons de gagner : {part_two_result_new}")
