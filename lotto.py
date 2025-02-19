import sys
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import messagebox
import random
import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
           42, 43, 44, 45, 46, 47, 48, 49]

root = tk.Tk()
root.title('Lotto number generator')
root.geometry('800x600')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

list_box = tk.Listbox()
list_box.place(relx=0.6, rely=0.5, anchor='center', height=300)
list_box.configure(background='skyblue4', foreground='white', font=('Arial', 15))

image = PhotoImage(file='graphics/player/player_stand.png')
image_label = tk.Button(root, image=image, command=restart_program)
image_label.place(relx=0.3, rely=0.2, anchor='center')

my_label = tk.Label(text = 'Press icon to restart \n or "Tab" to quit \n', font=('Arial', 15))
my_label.place(relx=0.3, rely=0.4, anchor='center') 

num_time_gen=tk.Scale(root, from_=1, to=10, orient='horizontal')  
num_time_gen.place(relx=0.6, rely=0.2, anchor='center') 

num_time_gen_label = tk.Label(text = 'How many times to generate?', font=('Arial', 10))
num_time_gen_label.place(relx=0.6, rely=0.15, anchor='center') 

def lotto_gen_7():
    for i in range(0,num_time_gen.get()):
        pick = random.sample(numbers, 7)
        pick.sort()
        print(pick)
        list_box.insert(tk.END, pick)

def lotto_gen_6():
    for i in range(0,num_time_gen.get()):
        pick = random.sample(numbers, 6)
        pick.sort()
        print(pick)
        list_box.insert(tk.END, pick)
    
def lotto_gen(x):
    for i in range(0,num_time_gen.get()):
        pick = random.sample(numbers, x)
        pick.sort()
        print(pick)
        list_box.insert(tk.END, pick)
    
def submit():
    digits=num_entry.get()
    try:
        digits=int(digits)
    except:
         messagebox.showerror('Invalid Input', 'Please enter numbers only')
    lotto_gen(digits)
    
def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=json, filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                list_box_str = list_box.get(0, "end")
                file.write(json.dumps(list_box_str, indent=4))
            messagebox.showinfo('File Saved to:', file_path)
        except Exception as e:
            messagebox.showerror('Error', 'An error has occured while saving.')
            
def clear_list_box():
   list_box.delete(0,"end")

button_7 = tk.Button(root, text="Generate 7 numbers", command = lotto_gen_7)
button_7.place(relx=0.3, rely=0.5, anchor='center')

button_6 = tk.Button(root, text="Generate 6 numbers", command = lotto_gen_6)
button_6.place(relx=0.3, rely=0.6, anchor='center')

save_button = tk.Button(root, text="Save to JSON", command = save_to_file)
save_button.place(relx=0.3, rely=0.7, anchor='center')

status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()

num_entry=tk.Entry(root, font = ('Arial',10,'normal'))
num_entry.place(relx=0.3, rely=0.8, anchor='center')

sub_btn=tk.Button(root,text = 'Custom number of digits', command=submit)
sub_btn.place(relx=0.3, rely=0.85, anchor='center')

list_clear=tk.Button(root, text = 'Clear all numbers', command=clear_list_box)
list_clear.place(relx=0.6, rely=0.8, anchor='center')

root.bind("<Tab>", exit)
root.mainloop()
