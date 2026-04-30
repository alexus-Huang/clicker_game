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


root.mainloop()