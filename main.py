import tkinter as tk 
import math
root = tk.Tk()
root.minsize(1000,500)

#Variables
rate = 1.00
clicks = 0

#Rebirth Data
rebirth_costs = {
    1: 10,
    2: 50,
    3: 100,
    4: 500,
    5: 1000
}


def rebirth_window():
    popup = tk.Toplevel(root)
    popup.title("Rebirth Description")
    popup.minsize(500,450)

    title = tk.Label(popup, text="Rebirth Description")
    title.pack(pady=10)

    #loop through rebirth data to display each cost
    for level, cost in rebirth_costs.items():
        rebirth_text = f"Level {level} : {cost} Clicks"

        rebirth_label = tk.Label(popup,text = rebirth_text, font = ("Arial",12))
        rebirth_label.pack(pady=5)

def rebirth():
    global rate
    rate += 0.2
    print(rate)

def click():
    global clicks
    clicks += math.ceil(1 * rate)
    print(clicks)
    clicksLabel.config(text=f"Clicks: {clicks}")

#labels
titleLabel = tk.Label(root,text="Clicker Game")
titleLabel.pack()

clicksLabel = tk.Label(root,text=f"Clicks {clicks}")
clicksLabel.pack()

#buttons
clickBtn = tk.Button(root,text = "Click!", command=click)
clickBtn.pack()

rebirthBtn = tk.Button(root,text="Rebirth",command = rebirth)
rebirthBtn.pack()

rebirthDescription = tk.Button(root, text = "Rebirth Description", command=rebirth_window)
rebirthDescription.pack(pady=20)

root.mainloop()