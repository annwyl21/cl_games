import pytest
from yahtzee_calc import Yahtzee_calc

# Test upper section

@pytest.mark.parametrize("dice_roll, answer", [
        ([1, 1, 1, 1, 1], 5), # This is a yahtzee but it should still return a score in this section
        ([1, 6, 1, 5, 1], 3),
        ([4, 1, 3, 1, 6], 2)
    ])
def test_aces(dice_roll, answer):
    results = Yahtzee_calc.get_upper_score(dice_roll)
    assert results["aces"] == answer, "Total score of aces is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([6, 2, 2, 2, 2], 8),
        ([2, 6, 2, 5, 2], 6),
        ([4, 2, 3, 2, 6], 4)
    ])
def test_twos(dice_roll, answer):
    results = Yahtzee_calc.get_upper_score(dice_roll)
    assert results["twos"] == answer, "Total score of twos is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([3, 3, 3, 6, 3], 12),
        ([3, 6, 3, 5, 3], 9),
        ([4, 3, 1, 3, 6], 6)
    ])
def test_threes(dice_roll, answer):
    results = Yahtzee_calc.get_upper_score(dice_roll)
    assert results["threes"] == answer, "Total score of threes is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([4, 4, 4, 1, 4], 16),
        ([4, 6, 4, 5, 4], 12),
        ([1, 4, 2, 4, 6], 8)
    ])
def test_fours(dice_roll, answer):
    results = Yahtzee_calc.get_upper_score(dice_roll)
    assert results["fours"] == answer, "Total score of fours is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([5, 6, 5, 5, 5], 20),
        ([5, 6, 5, 4, 5], 15),
        ([1, 5, 2, 5, 6], 10)
    ])
def test_fives(dice_roll, answer):
    results = Yahtzee_calc.get_upper_score(dice_roll)
    assert results["fives"] == answer, "Total score of fives is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([1, 6, 6, 6, 6], 24),
        ([6, 5, 6, 4, 6], 18),
        ([1, 6, 2, 6, 3], 12)
    ])
def test_sixes(dice_roll, answer):
    results = Yahtzee_calc.get_upper_score(dice_roll)
    assert results["sixes"] == answer, "Total score of sixes is incorrect"

# Test lower section

@pytest.mark.parametrize("dice_roll, answer", [
        ([6, 6, 6, 2, 3], 18),
        ([6, 5, 4, 4, 4], 12),
        ([1, 6, 6, 6, 3], 18),
        ([2, 1, 2, 3, 2], 6)
    ])
def test_three_of_a_kind(dice_roll, answer):
    results = Yahtzee_calc.get_lower_score(dice_roll)
    assert results["three_of_a_kind"] == answer, "Three of a kind is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([6, 6, 6, 6, 3], 24),
        ([6, 4, 4, 4, 4], 16),
        ([1, 6, 6, 6, 6], 24),
        ([2, 1, 2, 2, 2], 8)
    ])
def test_four_of_a_kind(dice_roll, answer):
    results = Yahtzee_calc.get_lower_score(dice_roll)
    assert results["four_of_a_kind"] == answer, "Four of a kind is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([6, 6, 6, 5, 5], 25),
        ([2, 2, 4, 4, 4], 25),
        ([1, 6, 6, 6, 1], 25),
        ([2, 1, 2, 1, 2], 25)
    ])
def test_full_house(dice_roll, answer):
    results = Yahtzee_calc.get_lower_score(dice_roll)
    assert results["full_house"] == answer, "Full House is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([1, 2, 3, 4, 6], 30),
        ([2, 5, 4, 3, 2], 30),
        ([1, 6, 2, 4, 3], 30),
        ([5, 2, 2, 4, 3], 30)
    ])
def test_small_straight(dice_roll, answer):
    results = Yahtzee_calc.get_lower_score(dice_roll)
    assert results["sm_straight"] == answer, "Small Straight is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([1, 2, 3, 4, 5], 40),
        ([2, 5, 4, 3, 6], 40),
        ([2, 3, 4, 5, 6], 40),
        ([5, 1, 2, 4, 3], 40)
    ])
def test_large_straight(dice_roll, answer):
    results = Yahtzee_calc.get_lower_score(dice_roll)
    assert results["lg_straight"] == answer, "Large Straight is incorrect"

@pytest.mark.parametrize("dice_roll, answer", [
        ([1, 1, 1, 1, 1], 50),
        ([3, 3, 3, 3, 3], 50)
    ])
def test_yahtzee(dice_roll, answer):
    results = Yahtzee_calc.get_lower_score(dice_roll)
    assert results["yahtzee"] == answer, "Yahtzee is incorrect"

def test_chance(dice_roll):
    dice_roll = [5, 1, 5, 2, 3]
    results = Yahtzee_calc.get_lower_score(dice_roll)
    assert results == 16, "Chance is incorrect"