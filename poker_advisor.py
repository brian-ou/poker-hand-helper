def suggest_action(card1, suit1, card2, suit2):
    # Normalize card input
    card1, card2 = card1.upper(), card2.upper()
    suit1, suit2 = suit1.lower(), suit2.lower()

    # Define strong hands (pairs and high-value suited connectors)
    strong_pairs = {'A', 'K', 'Q', 'J', '10'}
    strong_suited = [('A', 'K'), ('K', 'Q'), ('Q', 'J')]

    # Check for pair
    if card1 == card2:
        if card1 in strong_pairs:
            return "Raise (Strong Pair)"
        else:
            return "Call (Moderate Pair)"

    # Check for suited high cards
    if suit1 == suit2:
        if (card1, card2) in strong_suited or (card2, card1) in strong_suited:
            return "Raise (Suited High Connectors)"
        else:
            return "Call (Suited)"

    # Check for high cards unsuited
    high_cards = {'A', 'K', 'Q', 'J', '10'}
    if card1 in high_cards and card2 in high_cards:
        return "Call (High Cards)"

    return "Fold"

# Example usage
print("Enter your two cards:")
c1 = input("Card 1 (e.g. A, K, Q, J, 10, 9...): ").strip()
s1 = input("Suit 1 (e.g. spades, hearts, diamonds, clubs): ").strip()
c2 = input("Card 2: ").strip()
s2 = input("Suit 2: ").strip()

decision = suggest_action(c1, s1, c2, s2)
print("Recommended action:", decision)
