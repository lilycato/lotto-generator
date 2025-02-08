import tkinter as tk
from sys import exit
import random

root = tk.Tk()
root.title('Lotto number generator')
root.geometry('800x600')

my_label = tk.Label(text = 'Press "Enter" for 7 numbers. Press "Back" for 6 numbers. "Tab" to quit \n', font=('Arial', 15))
my_label.place(relx=0.5, rely=0.5, anchor='center')

   
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
           42, 43, 44, 45, 46, 47, 48, 49]
    

def lotto_gen_7(event):
    pick = random.sample(numbers, 7)
    pick.sort()
    print(pick)
    my_label['text'] = pick

def lotto_gen_6(event):
    pick = random.sample(numbers, 6)
    pick.sort()
    print(pick)
    my_label['text'] = pick

root.bind("<Return>", lotto_gen_7)
root.bind("<BackSpace>", lotto_gen_6)
root.bind("<Tab>", exit)
root.mainloop()


        
