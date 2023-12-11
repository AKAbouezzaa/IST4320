# Im going to attempt and create a burger app which I will also use for the final project.
import tkinter as tk
from tkinter import *
main= tk.Tk()
main.title("Burger Station")
menu= {"Bacon Burger": 10.99, "Cheese Burger": 5.99, "Double Cheese Burger": 9.99, "Drink": 2.99, "Chicken Burger": 9.99}

selected=[]
total=0
row_num=1

#custom functions
def food_selections(burger,price,check_choice):
    '''
    This function is made to take in the food selected, by appending the selecting.
    '''
    global total
    if check_choice.get():
        selected.append(burger)
        total = total + price
    elif burger in selected:
        selected.remove(burger)
        total= total - price
    update_listbox()


#update the list box
def update_listbox():
    '''
    Update the listbox when a burger is selected
    '''
    selected_listbox.delete(0, tk.END)
    for item in selected:
        selected_listbox.insert(tk.END, item)

#checkout popup
def checkout():
    '''
    Checkout button, opens another tab printing total price
    '''
    food = "Total price:  " + str(total)
    popup = tk.Toplevel(main)
    popup.title("Checkout")
    popup_label = tk.Label(popup, text=food, font=('calibre',14,'normal'))
    popup_label.pack()
    exit_button = tk.Button(popup, text = "Exit",command = popup.destroy)
    exit_button.pack()

#create the labels for main
def create_labels():
    '''
    This function makes labels for the menu and for the selected items
    '''
    menu_label=tk.Label(main, text = "Menu")
    menu_label.grid(row = 0, column = 0, padx = 10, columnspan=2)
    selected_label = tk.Label(main, text = "Selected items", font=("Lucida Console", 14), background = 'yellow')
    selected_label.grid(row = row_num +3, pady=5)

#create listbox
selected_listbox = tk.Listbox(main, selectmode=tk.MULTIPLE)
selected_listbox.grid(row=30, column=0, padx=10, pady=5, columnspan=2, sticky=tk.W)


#checkbutton functions
for item, price in menu.items():
    check_choice = tk.BooleanVar()
    check = tk.Checkbutton(main, text="{} -  ${:.2f}".format(item, price), variable=check_choice, command=lambda i=item, p=price, var=check_choice: food_selections(i, p, var))
    check.grid(row=row_num, column=0, padx=10,pady=5, sticky=tk.W)
    row_num = row_num + 1
 

create_labels()

#create checkout button
checkout = tk.Button(main, text = "Checkout", command = checkout, activebackground='yellow')
checkout.grid(row=row_num+5, pady=10,columnspan = 2)

main.mainloop()