def calculate_scratchcard_points(cards):
    total_points = 0

    for card in cards:
        winning_numbers, your_numbers = card.split('|') # Split the card into winning and your numbers
        winning_numbers = set(map(int, winning_numbers.split())) # Convert the winning numbers to a set of integers
        your_numbers = set(map(int, your_numbers.split())) # Convert your numbers to a set of integers

        matches = winning_numbers.intersection(your_numbers) # Find the matches between the two sets
        if matches:
            # Calculate the points for this card
            points = 1 << (len(matches) - 1)  # 2^(number of matches - 1)
            total_points += points

    return total_points

def parse_cards_with_extra_text(cards_data):
    cards = []
    for line in cards_data:
        # Removing the "Card x:" part and then splitting the line
        card_numbers = line.split(':')[1].strip()
        winning_numbers, your_numbers = card_numbers.split('|')
        cards.append(winning_numbers.strip() + " | " + your_numbers.strip())
    return cards

# Read the contents of the file
file_path = './day4.txt'
with open(file_path, 'r') as file:
    cards_data = file.readlines()

# Parse the cards data with the adjusted function
parsed_cards_corrected = parse_cards_with_extra_text(cards_data)

# Calculate total points with the new data
total_points_corrected = calculate_scratchcard_points(parsed_cards_corrected)
print(total_points_corrected)