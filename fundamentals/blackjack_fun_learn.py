def card_value(card):
    """
    Calculate the numerical value of a card.
    
    Args:
    card (str): A string representing the card ('2' to '10', 'J', 'Q', 'K', or 'A')
    
    Returns:
    int: The numerical value of the card (2-11)
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def dealer_final_hand(initial_card):
    """
    Simulate the dealer's final hand value based on their initial card.
    
    Args:
    initial_card (str): The dealer's initial card
    
    Returns:
    int: The final value of the dealer's hand (17-21)
    """
    total = card_value(initial_card)
    while total < 17:
        total += 7  # Simplified: assume dealer draws a 7 (average card)
    return min(total, 21)

def calculate_stand_value(dealer_hand, player_sum):
    """
    Calculate the outcome of standing with the current hand.
    
    Args:
    dealer_hand (int): The dealer's final hand value
    player_sum (int): The player's current hand value
    
    Returns:
    int: 1 if player wins, -1 if dealer wins, 0 if it's a tie
    """
    if player_sum > 21:
        return -1
    if dealer_hand > 21:
        return 1
    if dealer_hand > player_sum:
        return -1
    if player_sum > dealer_hand:
        return 1
    return 0

def optimal_strategy(deck):
    """
    Calculate the optimal strategy for the given deck using dynamic programming.
    
    Args:
    deck (list): A list of cards representing the current deck
    
    Returns:
    float: The expected value of playing optimally from the start of the deck
    """
    n = len(deck)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        player_sum = 0
        dealer_card = deck[i]
        j = i

        # Stand immediately
        dealer_hand = dealer_final_hand(dealer_card)
        stand_value = calculate_stand_value(dealer_hand, player_sum)
        best_value = stand_value

        # Try hitting
        while j < n and player_sum <= 21:
            player_sum += card_value(deck[j])
            j += 1
            if player_sum > 21:
                hit_value = -1
            else:
                hit_value = calculate_stand_value(dealer_final_hand(dealer_card), player_sum) + dp[j]
            best_value = max(best_value, hit_value)

        dp[i] = best_value

    return dp[0]

def play_hand(player_cards, dealer_upcard, deck):
    """
    Simulate playing a single hand of blackjack using the optimal strategy.
    
    Args:
    player_cards (list): The player's initial cards
    dealer_upcard (str): The dealer's up card
    deck (list): The remaining deck of cards
    
    Returns:
    int: The outcome of the hand (1 for win, -1 for loss, 0 for tie)
    """
    player_sum = sum(card_value(card) for card in player_cards)
    while player_sum < 21:
        if optimal_strategy(deck) > 0:
            # Hit
            new_card = deck.pop()
            player_cards.append(new_card)
            player_sum += card_value(new_card)
        else:
            # Stand
            break
    
    dealer_hand = dealer_final_hand(dealer_upcard)
    return calculate_stand_value(dealer_hand, player_sum)

def simulate_game(num_hands=1000):
    """
    Simulate multiple hands of blackjack to estimate the average profit.
    
    Args:
    num_hands (int): The number of hands to simulate (default: 1000)
    
    Returns:
    float: The average profit per hand
    """
    import random
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    total_profit = 0
    
    for _ in range(num_hands):
        random.shuffle(deck)
        player_cards = [deck.pop(), deck.pop()]
        dealer_upcard = deck.pop()
        
        result = play_hand(player_cards, dealer_upcard, deck)
        total_profit += result
    
    return total_profit / num_hands

def test_play_hand():
    player_cards = ['A', '7']
    dealer_upcard = '9'
    deck = ['5', '6', '10', 'J', 'Q', 'K']
    result = play_hand(player_cards, dealer_upcard, deck)
    assert result in [-1, 0, 1]

if __name__ == "__main__":
    test_play_hand()