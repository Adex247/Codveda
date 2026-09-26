# Number Guessing Game

A simple command-line game written in Python. The program randomly generates a number between 1 and 100, and the player has a limited number of attempts to guess it, receiving "too high" or "too low" feedback after each guess.

## Features

- Random number generation using Python's built-in `random` module
- Configurable maximum number of attempts (default: 7)
- Feedback after each guess ("Too high!" / "Too low!")
- Input validation for non-numeric or out-of-range guesses
- Game ends when the number is guessed correctly or attempts run out
- Option to play again without restarting the script

## Requirements

- Python 3.x (no external dependencies)

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game
python number_guessing_game.py
```

Then follow the on-screen prompts to guess the number.

## Example

```
I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it.

Attempt 1/7 - Enter your guess: 50
Too high!

Attempt 2/7 - Enter your guess: 25
Too low!

Attempt 3/7 - Enter your guess: 37
Correct! You guessed it in 3 attempt(s).

Play again? (y/n):
```

## Project Structure

```
number-guessing-game/
├── number_guessing_game.py   # Main game script
└── README.md                 # Project documentation
```

## Customization

To change the number of attempts, edit the `max_attempts` parameter in `play_game()`:

```python
def play_game(max_attempts=7):
```

## License

Feel free to use, modify, and distribute this project for learning purposes.
