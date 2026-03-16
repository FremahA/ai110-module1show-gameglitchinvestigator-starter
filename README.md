# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.  
Glitchy Guesser is a number-guessing game built with Streamlit. The player selects a difficulty level (Easy, Normal, or Hard), which determines how large the number range is and how many attempts they get. The game picks a secret number in that range, and the player tries to guess it. After each guess, the game gives a directional hint (go higher / go lower) until the player either guesses correctly or runs out of attempts. A score is tracked based on how few attempts it takes to win.  

- [ ] Detail which bugs you found.
Four bugs were present in the starter code:

Changing secret number — The secret number was regenerated on every button click because it was not stored in session state. Each Streamlit rerun called randint() again, so the target kept changing mid-game, making it impossible to win.

Backwards hint messages — In check_guess(), when the guess was too high it said "Go HIGHER!" and when too low it said "Go LOWER!" — exactly backwards.

Secret number ignored difficulty range — The secret was always randint(1, 100) regardless of which difficulty was selected, so the prompt could tell you "guess between 1 and 20" while the actual secret could be 87.

Hard difficulty range was easier than Normal — Hard was set to 1-50, which is a smaller (easier) range than Normal's 1-100. Hard should be the hardest.

Scoring system logic was confusing and did not factor in the number of attempts based on the difficulty level.

- [ ] Explain what fixes you applied.

Session state for the secret — Wrapped the secret generation in a `if "secret" not in st.session_state`  check so the secret is only created once per game and survives reruns.

Hint direction — Swapped the return messages in check_guess() so guess > secret returns "Go LOWER!" and guess < secret returns "Go HIGHER!".

Difficulty-aware secret generation — Extracted the difficulty ranges into get_range_for_difficulty() in logic_utils.py, then called it in app.py so both the displayed range and the secret use the same values.

Hard difficulty range — Changed Hard's range from 1-50 to 1-200, making it correctly harder than Normal's 1-100. 

Scoring logic - Tracked scores based on how few attempts it takes to win in relation to the attempt limit for the selected difficulty level.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
