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
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?  
I used Claude, Chat GPT and Copilot.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

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
