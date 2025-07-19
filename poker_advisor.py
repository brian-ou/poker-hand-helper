import random

def parse_card_input(card_input):
    card_input = card_input.strip().upper()
    suits = {'S': 'spades', 'H': 'hearts', 'D': 'diamonds', 'C': 'clubs'}
    ranks = {'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'}

    for suit_char, suit_name in suits.items():
        if card_input.endswith(suit_char):
            rank = card_input[:-1].upper()
            if rank in ranks:
                return rank, suit_name
    raise ValueError("Invalid card input. Please use formats like 'Ah' (Ace of hearts), '10d' (Ten of diamonds), etc.")

def calculate_equity(card1, card2):
    # Simulate a random placeholder probability for demonstration
    rank_strength = {
        'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9,
        '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
    }
    score = rank_strength.get(card1, 0) + rank_strength.get(card2, 0)
    if card1 == card2:
        score += 10  # bonus for pairs
    return min(100, max(0, score / 28 * 100))  # simple normalized equity

def suggest_action(card1, suit1, card2, suit2, position='middle', num_players=6):
    # Normalize input
    card1, card2 = card1.upper(), card2.upper()
    suit1, suit2 = suit1.lower(), suit2.lower()
    position = position.lower()

    # Define strong hands and suited connectors
    strong_pairs = {'A', 'K', 'Q', 'J', '10'}
    strong_suited = [('A', 'K'), ('K', 'Q'), ('Q', 'J')]
    high_cards = {'A', 'K', 'Q', 'J', '10'}

    # Convert card ranks to numerical values for connectedness
    rank_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Position modifiers
    position_aggression = {
        'early': -1,
        'middle': 0,
        'late': 1
    }

    # Player count adjustment (more players = tighter play)
    aggression_adjustment = position_aggression.get(position, 0) - (num_players - 6) // 2

    # Calculate hand equity
    equity = calculate_equity(card1, card2)

    # Evaluate hand strength
    if card1 == card2:
        if card1 in strong_pairs:
            return f"Raise (Strong Pair, Equity: {equity:.1f}%)" if aggression_adjustment >= 0 else f"Call (Strong Pair, Equity: {equity:.1f}%)"
        else:
            return f"Call (Moderate Pair, Equity: {equity:.1f}%)" if aggression_adjustment >= 0 else f"Fold (Equity: {equity:.1f}%)"

    if suit1 == suit2:
        if (card1, card2) in strong_suited or (card2, card1) in strong_suited:
            return f"Raise (Suited High Connectors, Equity: {equity:.1f}%)" if aggression_adjustment >= 0 else f"Call (Equity: {equity:.1f}%)"
        # Check for suited connectors
        r1, r2 = rank_map.get(card1, 0), rank_map.get(card2, 0)
        if abs(r1 - r2) == 1:
            return f"Call (Suited Connectors, Equity: {equity:.1f}%)" if aggression_adjustment >= 0 else f"Fold (Equity: {equity:.1f}%)"
        else:
            return f"Call (Suited, Equity: {equity:.1f}%)" if aggression_adjustment >= 0 else f"Fold (Equity: {equity:.1f}%)"

    if card1 in high_cards and card2 in high_cards:
        return f"Call (High Cards, Equity: {equity:.1f}%)" if aggression_adjustment >= 0 else f"Fold (Equity: {equity:.1f}%)"

    return f"Fold (Equity: {equity:.1f}%)"

# Example usage
print("Enter your two cards (e.g. 'Ah' for Ace of hearts, 'Ks' for King of spades):")
try:
    card_input1 = input("Card 1: ")
    c1, s1 = parse_card_input(card_input1)

    card_input2 = input("Card 2: ")
    c2, s2 = parse_card_input(card_input2)

    position = input("Your position (early, middle, late): ").strip().lower()
    num_players = int(input("Number of players at the table: ").strip())

    decision = suggest_action(c1, s1, c2, s2, position, num_players)
    print("Recommended action:", decision)

except ValueError as e:
    print("Error:", e)
    print("Please enter valid cards using the format like 'Ah', '10d', 'Qs', etc.")
