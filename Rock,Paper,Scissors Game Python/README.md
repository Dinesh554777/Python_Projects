# ✊✋✌️ Rock Paper Scissors Game (Python)

## 📌 Description
This is a simple command-line based **Rock Paper Scissors Game** built using Python.  
The user plays against the computer, which randomly selects its move.

The game continues until the user chooses to quit, and it keeps track of the total wins for both the user and the computer.

---

## 🎯 Features
- Play against computer 🤖
- Random computer choice using Python
- Continuous gameplay until user quits
- Score tracking system
- Case-insensitive input handling
- Beginner-friendly implementation

---

## 🕹️ How to Play
1. Run the program.
2. Type:
   - `rock`
   - `paper`
   - `scissors`
3. The computer will randomly choose its move.
4. The winner of each round is displayed.
5. Type **Q** to quit the game.
6. Final scores are shown at the end.

---

## 🧠 Game Logic
- Choices are stored in a list:
  ```python
  ["rock", "paper", "scissors"]
````

* Computer selects a move using:

  ```python
  random.randint(0, 2)
  ```
* Conditions determine the winner:

  * Rock beats Scissors
  * Paper beats Rock
  * Scissors beats Paper
* Scores are updated after each round

---

## 🧪 Difficulty Level

**Easy 🟢**

Suitable for:

* Beginners learning Python
* Practice for loops and conditions
* Understanding lists and randomness

---

## 🛠️ Technologies Used

* Python (Standard Library: `random`)

---

## ▶️ How to Run

```bash
python rock_paper_scissors.py
```

---

## 📊 Example Output

```id="rpsout1"
Type Rock/Paper/Scissors or Q to Quit: rock
Computer pick scissors.
You won!

Type Rock/Paper/Scissors or Q to Quit: paper
Computer pick scissors.
You lost!

Type Rock/Paper/Scissors or Q to Quit: q

You won 1 times.
Computer won 1 times.
Thank you for playing!
```

---

## 🚀 Future Improvements

* Add tie/draw condition handling
* Add emojis or better UI output
* Add best-of-3 or best-of-5 mode
* Add score history tracking
* Convert into GUI or web version

---

## 🙌 Contribution

Feel free to fork and improve this project!

---

## 📄 License

This project is open-source and free to use.

```

---

If you want next level 🚀, I can:
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}

```
