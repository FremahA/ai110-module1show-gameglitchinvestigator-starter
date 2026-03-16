# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game has a selected difficulty level, you guess a number between 1 and 100 and it tells you if you have won the game or it gives you hints on whether to guess a higher number or a lower number. You get 5 attempts and you get a score.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The secret number kept changing everytime i made a new guess/attempt in the same game.  
  The hints were backwards. It said to lower at times i was supposed to guess higher and it said to higher at time i was supposed to guess lower.  
  Another bug is that when you select the difficulty. It sates the expected range of numbers you can guess from but when you check the developer info, the secret number is is sometimes outside that range.  
  The range for "Hard" diffulty level was lower than that of the "Normal level.  
  Scoring logic was confusing and did not factor in the number of attempts based on the difficulty level.  
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?  
I used Claude, Chat GPT and Copilot.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).  

When I asked Claude to help fix the backwards hint bug, it correctly identified that the check_guess function in logic_utils.py had the hint messages swapped — "Too High" was saying "Go HIGHER!" and "Too Low" was saying "Go LOWER!" Claude suggested reversing them so guess > secret returns "Go LOWER!" and guess < secret returns "Go HIGHER!". I verified it was correct by playing the game and testing edge cases: guessing above the secret now correctly tells you to go lower, and guessing below tells you to go higher.  

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).  

The AI suggested that the wrong hints bug was caused by app.py converting the secret to a string on even-numbered attempts. The AI's fix was to add int() conversion inside check_guess to force numeric comparison.

Why it was misleading: This explanation described a real flaw in the code's error handling, but it misidentified the root cause of the wrong hint directions. Even after applying the fix, the hints were still wrong.

How I verified it: I applied the AI's fix and tested the game by entering a number I knew was above the secret. The game still told me to go higher instead of lower, which proved the type-comparison theory was not causing the wrong directions. I reverted the change.

The actual bug: The hint messages inside check_guess were themselves reversed — "Too High" returned "Go HIGHER!" and "Too Low" returned "Go LOWER!". Swapping those two message strings fixed the behavior. The AI had analyzed the wrong layer of the code.  

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?  
I considered a bug fixed when I could both play through the scenario manually in the app and have a pytest test pass that directly asserted the correct behavior. Just seeing the app run without crashing wasn't enough — I needed to verify the specific output was right (e.g., that guessing too high actually returned "Too High" and showed "Go LOWER!").  

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.  

I ran pytest on the hint direction bug. The tests test_too_high_message_says_go_lower and test_too_low_message_says_go_higher in tests/test_game_logic.py directly call check_guess(80, 50) and check_guess(20, 50) and assert that the message contains "LOWER" or "HIGHER" respectively. Before the fix, these tests would have failed. They showed me the exact strings the function was returning and made it obvious the messages were swapped.   

- Did AI help you design or understand any tests? How?  
Yes. Claude helped me understand what to test, not just how to write the syntax. For example, for the string-vs-integer comparison bug, Claude suggested testing check_guess(99, 10) where the numbers are far apart enough that string comparison would give the wrong answer ("99" < "10" is False, but 99 > 10 is True), making the bug detectable. That helped me see that a test like check_guess(42, 42) alone wouldn't catch it. I needed cases where int and string ordering disagree.   

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?  

I learned that Streamlit reruns the script from top to bottom whenever the user interacts with the app. Because of that, values that are supposed to stay the same across interactions need to be stored in session state. Otherwise, things like the secret number can get reset every time the app reruns.

If I were explaining it to a friend, I would say Streamlit is like restarting the script every time you click something, and session state is the place where you keep the important values so they do not get lost between reruns.  
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?  

One thing I would do differently next time is ask AI more specific questions earlier, especially about what I expected to happen, what actually happened, and what part of the code seemed related. That would probably make the suggestions more accurate and save time.  

- In one or two sentences, describe how this project changed the way you think about AI generated code.  

This project changed how I think about AI-generated code because I realized AI suggestions should be treated as hypotheses rather final answers. All AI generated code must be carefully tested and verified to make sure it fixes the problem correctly.  