import tkinter as tk
import string
import random
import itertools

root = tk.Tk()
root.title("Show me a random barcode...")
root.geometry("400x400")


msg = tk.Label(root,text="your random barcode:")
barcode = tk.Label(root)

alphabet = list(string.ascii_lowercase)

for i in itertools.repeat(None, 5):
    current_num = random.randint(0,25)
    barcode["text"] += alphabet[current_num] 
msg.pack()
barcode.pack()

root.mainloop()
