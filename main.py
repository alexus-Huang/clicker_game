import tkinter as tk 
import math
root = tk.Tk()
root.minsize(1000,500)

#Variables
rate = 1.00
clicks = 0
rebirth_level = 0
#Rebirth Data
rebirth_costs = {
    1: 5,
    2: 10,
    3: 15,
    4: 20,
    5: 1000,
    6: 1500,
    7: 2000,
    8: 2500,
    9: 3000,
    10: 3500
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
def show_warning(msg):
    warningLabel.config(text=msg)
    root.after(2000,lambda:warningLabel.config(text=""))

def rebirth():
    #check if user has correct amount of clicks to rebirth
    global rebirth_level
    global rate
    global clicks

    cost = rebirth_costs.get(rebirth_level + 1, float('inf'))
    if clicks >= cost:
        rebirth_level+=1
        clicks = 0
        rate += 0.2
        clicksLabel.config(text=f"Clicks: {clicks}")
        rebirth_level_label.config(text=f"Rebirth level: {rebirth_level}")
    else:
        show_warning("⚠️ Not enough clicks to rebirth!")

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

rebirth_level_label = tk.Label(root,text=f"Rebirth Level:{rebirth_level}")
rebirth_level_label.pack(pady=10)

warningLabel = tk.Label(root,text="",fg="red",font=("Arial",12,"bold"))
warningLabel.pack(pady=5)
#buttons
clickBtn = tk.Button(root,text = "Click!", command=click)
clickBtn.pack()

rebirthBtn = tk.Button(root,text="Rebirth",command = rebirth)
rebirthBtn.pack()

rebirthDescription = tk.Button(root, text = "Rebirth Description", command=rebirth_window)
rebirthDescription.pack(pady=20)

root.mainloop()