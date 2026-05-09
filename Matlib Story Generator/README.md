````markdown
# 📖 Mad Libs Story Generator (Python)

## 📌 Description
This is a simple **Mad Libs Story Generator** built using Python.  
The program reads a story template from a text file and replaces placeholder words with user-provided inputs to create a fun and personalized story.

Placeholders inside the story are written using:
```text
<word>
````

The user is asked to provide replacement words, and the final customized story is displayed.

---

## 🎯 Features

* Reads story from external text file
* Detects placeholders automatically
* User-customized story generation
* Uses file handling in Python
* Dynamic text replacement
* Beginner-friendly project

---

## 🕹️ How to Play

1. Create a file named:

   ```text
   story.txt
   ```
2. Write a story using placeholders like:

   ```text
   Once upon a time, there was a <animal> named <name>.
   ```
3. Run the Python program.
4. Enter words when prompted.
5. Enjoy your generated story 🎉

---

## 🧠 Program Logic

* Reads the story using:

  ```python
  open("story.txt", "r")
  ```
* Finds placeholders between:

  ```text
  < >
  ```
* Stores placeholders using a `set`
* Takes user inputs for each placeholder
* Replaces placeholders with user answers
* Prints the final story

---

## 🧪 Difficulty Level

**Easy to Medium 🟡**

Suitable for:

* Python beginners
* Practice for file handling
* Understanding strings and dictionaries

---

## 🛠️ Technologies Used

* Python (No external libraries required)

---

## ▶️ How to Run

```bash
python madlibs.py
```

---

## 📄 Example `story.txt`

```text
One day, a <animal> named <name> went to the <place>.
```

---

## 📊 Example Output

```text
Enter a word for <animal>: tiger
Enter a word for <name>: Leo
Enter a word for <place>: forest

One day, a tiger named Leo went to the forest.
```

---

## 🚀 Future Improvements

* Add multiple story templates
* Random story selection
* Save generated stories to a file
* Add GUI version using Tkinter
* Add colorful terminal output

---

## 🙌 Contribution

Feel free to fork this project and create your own fun stories!

---

## 📄 License

This project is open-source and free to use.

```
```
