# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
i. The hints were wrong
ii. hard level has low range to guess than than the normal
iii. the secret number kept changing



## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
:- I used Copilot. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
:- The AI suggested to change the hints that were wrong. I verified the logic by reading myself.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
:- I did not get any wrong suggestion.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
:- I checked manually by running the test cases and also running the app.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
:- I ran the app, saw a secret, and test putting incorrect guess to verify if hints were right or not. 

- Did AI help you design or understand any tests? How?
:- Yes, AI wrote the test cases more thoroughly to check every breakpoints. 


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
:- The secret number was getting converted to string. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
