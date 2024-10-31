import tkinter as tk

root = tk.Tk()
root.title("game")
root.geometry("1000x800")

Money=0

point_click = 1
total_upgrade = 0
autoclick=0
autoclickcost=20
auto_click_speed_upgrade=0
auto_click_speed_upgrade_cost=100
def click():
    global Money
    Money += point_click
    money_label.config(text=f"Money: {Money}")

def upgrade():
    global Money,point_click,total_upgrade
    if Money >= 5 :
        Money -= 5
        money_label.config(text=f"Money: {Money}")
        point_click +=1
        total_upgrade +=1
        total_label.config(text=f"Total Upgrade Click Count: {total_upgrade}")
    else:
        upgrade_button.config(text=f"Not Enough Money",fg="red")
        root.after(1000, reset_upgrade2_button)

def upgrade2():
    global Money,autoclick,autoclickcost
    if Money >=autoclickcost:
        Money -=autoclickcost
        autoclick +=1
        upgrade2_button.config(text=f"Buy Auto-Clicker (+{autoclick}/sec) - {autoclickcost} points", fg="black")
        money_label.config(text=f"Money: {Money}")
        
    else:
        upgrade2_button.config(text=f"Not Enough Money",fg="red")
        root.after(1000, reset_upgrade2_button)

def reset_upgrade2_button():
    upgrade2_button.config(text=f"Buy Auto-Clicker (+{autoclick}/sec) - {autoclickcost} points", fg="black")
    upgrade_button.config(text=f"Upgrade Click (+1)", fg="black")

def auto_click():
    global Money,autoclick
    Money +=autoclick
    money_label.config(text=f"Money: {Money}")
    root.after(1000, auto_click)

def upgradespeed():
    global Money,autoclick,auto_click_speed_upgrade_cost,auto_click
    if Money >=auto_click_speed_upgrade_cost:
        Money -= auto_click_speed_upgrade_cost
        root.after(800, auto_click)



money_label = tk.Label(root, text="Money: 0", font=("Arial", 24))
money_label.grid(row=0,column=2)

click_button = tk.Button(root, text="Get Money", font=("Arial", 18), command=click)
click_button.grid(row=1,column=2)

total_label = tk.Label(root, text="Total Upgrade Click Count = 0", font=("Arial", 14))
total_label.grid(row=2,column=1)

upgrade_button = tk.Button(root,text="Upgrade Click (+1)",font=("Arial", 14), command=upgrade)
upgrade_button.grid(row=3,column=1)

upgrade2_button = tk.Button(root, text=f"Buy Auto-Clicker (+{autoclick}/sec) - {autoclickcost} points", fg="black",font=("arial",14),command=upgrade2)
upgrade2_button.grid(row=2,column=1)

upgrade2_label = tk.Label(root, text="Auto Click Upgrade",font=("arial",14))
upgrade2_button.grid(row=2,column=5)

upgradeS= tk.Button(root, text=f"Buy Auto-Clicker Speed Upgrade (+{autoclick}/sec) - {auto_click_speed_upgrade_cost} points", fg="black",font=("arial",14),command=upgradespeed)
upgradeS.grid(row=3,column=1)

upgradeS_label = tk.Label(root, text="Auto Click Speed Upgrade",font=("arial",14))
upgradeS.grid(row=3,column=5)

root.after(1000, auto_click)



root.mainloop()
