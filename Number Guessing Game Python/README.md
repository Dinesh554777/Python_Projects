# 🎯 Number Guessing Game

## 📌 Description
This is a command-line based **Number Guessing Game** built using Python.  
The program randomly selects a number between **1 and 100**, and the player must guess the correct number.

Unlike basic versions, this game allows **unlimited attempts** until the correct number is guessed. It also tracks how many attempts the user takes.

---

## 🎯 Features
- Random number generation (1 to 100)
- Unlimited attempts until correct guess
- Tracks number of attempts
- Input validation (only numbers allowed)
- Range validation (1–100 only)
- Helpful hints:
  - Too high 📈
  - Too low 📉
- Beginner-friendly logic

---

## 🕹️ How to Play
1. Run the program.
2. Enter a number between **1 and 100**.
3. The game will guide you:
   - “greater” → your guess is too high
   - “lesser” → your guess is too low
4. Keep trying until you guess the correct number.
5. The program will show how many attempts you used.

---

## 🧠 Game Logic
- A random number is generated using:
  ```python
  random.randint(1, 100)