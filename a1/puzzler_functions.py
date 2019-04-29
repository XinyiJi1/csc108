"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    return puzzle == view



def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return True if and only if 
    the puzzle is the same as the view or the current_selection is QUIT.
    
    Precondition:current_selection == CONSONANT 
    or current_selection == VOWEL 
    or current_selection == SOLVE 
    or current_selection == QUIT
    
    >>>game_over('banana', 'banana', SOLVE)
    True
    >>>game_over('apple', 'a^^le', QUIT)
    True
    """
    return puzzle == view or current_selection == QUIT



def bonus_letter(puzzle: str, view: str, evaluate_letter: str) -> bool:
    """Return True if and only if 
    the evaluate_letter appears in the puzzle but not in its view.
    
    >>>bonus_letter('apple', 'a^^le', 'p')
    True
    >>>bonus_letter('apple', 'a^^le', 'l')
    False
    """
    return £¨evaluate_letter in puzzle£© and £¨not evaluate_letter in view£©



def update_letter_view(puzzle: str, view: str, index: int, guess_letter: str) -> str:
    """Return a single character string representing the next view of 
    the character at the given index.
    If the character at that index of the puzzle matches the guess_letter, 
    then return the character. 
    Otherwise, return the character at that index of the view.
    
    >>>update_letter_view('apple', 'a^^le', 2, 'p')
    'p'
    >>>update_letter_view('apple', 'a^^le', 2, 'l')
    '^'
    """
    if puzzle[index] == guess_letter:
        return puzzle[index]
    else:
        return view[index]
  
  
  
def calculate_score(current_score: int, occurrence_number: int, letter_type: str) -> int:
    """Return the new score by adding the product of the occurrence_number 
    and the point for consonant to the current_score 
    when the letter_type is a consonant.
    or by deducting the price for vowel from the current_score 
    if the letter_type is a vowel.
    
    >>>calculate_score(15, 5, CONSONANT)
    20
    >>>calculate_score(20, 3, VOWEL)
    19
    """
    if letter_type == CONSONANT:
        return current_score + occurrence_number * CONSONANT_POINTS
    elif letter_type == VOWEL:
        return current_score-VOWEL_PRICE
  
  
def next_player(current_player: str, occurrence_number: int) -> str:
    """If and only if the occurrence_number is greater than zero, 
    the current_player plays again. Return the next player.
    
    Precondition:current_player == PLAYER_ONE
    or current_player == PLAYER_TWO
    
    >>>next_player(PLAYER_ONE, 1)
    'Player One'
    >>>next_player(PLAYER_TWO, 0)
    'Player One'
    """
    if occurrence_number > 0:
        return current_player
    else:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        else:
            return PLAYER_ONE
        