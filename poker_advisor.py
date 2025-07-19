def suggest_action(card1, card2):
    strong_hands = [('A', 'A'), ('K', 'K'), ('Q', 'Q'), ('A', 'K'), ('J', 'J')]
    if (card1, card2) in strong_hands or (card2, card1) in strong_hands:
        return "Raise"
    elif card1 == card2:
        return "Call"
    else:
        return "Fold"

# Example usage
c1 = input("Enter your first card (e.g. A, K, Q, J, 10...): ").upper()
c2 = input("Enter your second card: ").upper()

decision = suggest_action(c1, c2)
print("Recommended action:", decision)
