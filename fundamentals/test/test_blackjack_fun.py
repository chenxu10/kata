import pytest
from fundamentals.blackjack_fun_learn import (
    card_value, dealer_final_hand, calculate_stand_value,
    optimal_strategy, play_hand, simulate_game
)

@pytest.mark.parametrize("card, expected", [
    ('2', 2), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11)
])
def test_card_value(card, expected):
    """
    Test the card_value function with various input cards.
    
    This test ensures that the card_value function correctly calculates
    the numerical value of different cards in a deck.
    """
    assert card_value(card) == expected

@pytest.mark.parametrize("initial_card, expected", [
    ('6', 19), ('10', 20), ('A', 21)
])
def test_dealer_final_hand(initial_card, expected):
    assert dealer_final_hand(initial_card) == expected

@pytest.mark.parametrize("dealer_hand, player_sum, expected", [
    (20, 19, -1),
    (22, 18, 1),
    (18, 18, 0),
    (17, 21, -1),
    (19, 20, 1)
])
def test_calculate_stand_value(dealer_hand, player_sum, expected):
    assert calculate_stand_value(dealer_hand, player_sum) == expected

def test_optimal_strategy():
    deck = ['A', '10', '5', '6']
    assert optimal_strategy(deck) > 0

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    assert optimal_strategy(deck) > -1 and optimal_strategy(deck) < 1

def test_play_hand():
    player_cards = ['A', '7']
    dealer_upcard = '9'
    deck = ['5', '6', '10', 'J', 'Q', 'K']
    result = play_hand(player_cards, dealer_upcard, deck)
    assert result in [-1, 0, 1]

def test_simulate_game():
    avg_profit = simulate_game(num_hands=1000)
    assert -0.1 < avg_profit < 0.1
    
      # Expected value should be close to 0