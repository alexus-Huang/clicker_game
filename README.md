# 🖱️ Python Tkinter Clicker Game

## 📌 Overview

This is a simple clicker game built using Python’s Tkinter library. The player gains clicks by pressing a button and can **rebirth** to reset progress in exchange for a higher click rate.

The project focuses on building an interactive GUI while managing game state, user feedback, and progression mechanics.

---

## 🚀 Features

* Click button to gain points
* Dynamic click scaling based on a rate multiplier
* Rebirth system that:

  * Resets clicks
  * Increases click rate
  * Requires increasing costs per level
* Rebirth description popup window
* Temporary warning messages for invalid actions

---

## 🧠 What I Learned

Through this project, I developed a stronger understanding of:

* Using `tk.Label` to dynamically display and update information
* Handling button events with `command`
* Managing application state with global variables
* Creating popup windows with `tk.Toplevel`
* Using functions to organize logic (e.g., click handling, rebirth system)
* Implementing a **warning system** using `after()` to display temporary messages
* Working with dictionaries to store structured data (rebirth costs)
* Updating the UI in real-time based on user interaction

---

## 🛠️ Technologies Used

* Python
* Tkinter (built-in GUI library)
* Math module

---

## ▶️ How to Run

1. Make sure Python is installed
2. Download or clone this repository
3. Run the file:

```bash
python main.py
```

---

## 🎮 How to Play

* Click the **"Click!"** button to earn clicks
* Use **"Rebirth"** when you have enough clicks to reset and increase your rate
* View rebirth requirements by clicking **"Rebirth Description"**

---

## 📈 Future Improvements

* Add save/load system for progress
* Improve UI design (colors, layout, styling)
* Add upgrades besides rebirth
* Introduce animations or sound effects
* Balance rebirth scaling for better gameplay

---

## 💡 Notes

This project was built as a way to practice GUI development and understand how front-end interaction connects with underlying logic in Python.
