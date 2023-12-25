def calculate_total_scratchcards_efficient(cards):
    total_cards = len(cards)
    card_copies = [1] * total_cards  # Start with one copy of each card

    for i in range(total_cards):
        winning_numbers, your_numbers = cards[i].split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))

        matches = winning_numbers.intersection(your_numbers)
        num_matches = len(matches)

        # Add copies to the subsequent cards
        for j in range(i + 1, min(i + 1 + num_matches, total_cards)):
            card_copies[j] += card_copies[i]

    return sum(card_copies)

# Read the contents of the file
file_path = './day4.txt'
with open(file_path, 'r') as file:
    cards_data = file.readlines()

def parse_cards_with_extra_text(cards_data):
    cards = []
    for line in cards_data:
        # Removing the "Card x:" part and then splitting the line
        card_numbers = line.split(':')[1].strip()
        winning_numbers, your_numbers = card_numbers.split('|')
        cards.append(winning_numbers.strip() + " | " + your_numbers.strip())
    return cards

# Parse the cards data with the adjusted function
parsed_cards_corrected = parse_cards_with_extra_text(cards_data)

# Calculate the total number of scratchcards with the efficient method
total_scratchcards_efficient = calculate_total_scratchcards_efficient(parsed_cards_corrected)
print(total_scratchcards_efficient)
