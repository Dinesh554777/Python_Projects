# 🎲 Dice Rolling Game (Multiplayer - Python)

## 📌 Description
This is a command-line based **multiplayer dice rolling game** built using Python.  
Players take turns rolling a dice and try to reach a target score. The first player to reach the maximum score wins the game.

The game supports **2 to 4 players** and includes turn-based gameplay with risk decisions.

---

## 🎯 Features
- Multiplayer support (2–4 players)
- Turn-based gameplay
- Random dice rolling (1–6)
- Risk-based decision system (continue or stop)
- Score tracking for each player
- Automatic winner detection

---

## 🕹️ How to Play
1. Run the program.
2. Enter the number of players (**2 to 4**).
3. Each player takes turns:
   - Choose to roll the dice (`y`)
   - If you roll:
     - **1 → Turn ends, no points added ❌**
     - **2–6 → Points added ✅**
4. You can stop rolling anytime to save your points.
5. First player to reach **50 points** wins 🏆

---

## 🧠 Game Logic
- Dice values are generated using:
  ```python
  random.randint(1, 6)