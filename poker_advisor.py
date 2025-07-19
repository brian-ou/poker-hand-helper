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

    # Evaluate hand strength
    if card1 == card2:
        if card1 in strong_pairs:
            return "Raise" if aggression_adjustment >= 0 else "Call (Strong Pair)"
        else:
            return "Call (Moderate Pair)" if aggression_adjustment >= 0 else "Fold"

    if suit1 == suit2:
        if (card1, card2) in strong_suited or (card2, card1) in strong_suited:
            return "Raise (Suited High Connectors)" if aggression_adjustment >= 0 else "Call"
        # Check for suited connectors
        r1, r2 = rank_map.get(card1, 0), rank_map.get(card2, 0)
        if abs(r1 - r2) == 1:
            return "Call (Suited Connectors)" if aggression_adjustment >= 0 else "Fold"
        else:
            return "Call (Suited)" if aggression_adjustment >= 0 else "Fold"

    if card1 in high_cards and card2 in high_cards:
        return "Call (High Cards)" if aggression_adjustment >= 0 else "Fold"

    return "Fold"

# Example usage
print("Enter your two cards:")
c1 = input("Card 1 (e.g. A, K, Q, J, 10, 9...): ").strip()
s1 = input("Suit 1 (e.g. spades, hearts, diamonds, clubs): ").strip()
c2 = input("Card 2: ").strip()
s2 = input("Suit 2: ").strip()
position = input("Your position (early, middle, late): ").strip()
num_players = int(input("Number of players at the table: ").strip())

decision = suggest_action(c1, s1, c2, s2, position, num_players)
print("Recommended action:", decision)
