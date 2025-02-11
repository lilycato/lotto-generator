import tkinter as tk
from sys import exit
import random

root = tk.Tk()
root.title('Lotto number generator')
root.geometry('800x600')

my_label = tk.Label(text = 'Press buttons to generate. Press "Tab" to quit \n', font=('Arial', 15))
my_label.place(relx=0.5, rely=0.2, anchor='center')

   
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
           42, 43, 44, 45, 46, 47, 48, 49]
    
list_box = tk.Listbox(font=('Arial', 15))
list_box.place(relx=0.5, rely=0.7, anchor='center', height=300)

def lotto_gen_7():
    pick = random.sample(numbers, 7)
    pick.sort()
    print(pick)
    list_box.insert(tk.END, pick)

def lotto_gen_6():
    pick = random.sample(numbers, 6)
    pick.sort()
    print(pick)
    list_box.insert(tk.END, pick)

button_7 = tk.Button(root, text="Generate 7 numbers", command = lotto_gen_7)
button_7.place(relx=0.5, rely=0.3, anchor='center')

button_6 = tk.Button(root, text="Generate 6 numbers", command = lotto_gen_6)
button_6.place(relx=0.5, rely=0.4, anchor='center')


root.bind("<Tab>", exit)
root.mainloop()
