import time
import tkinter as tk
from tkinter import messagebox
def display(content):
 root = tk.Tk()
 root.withdraw()
 t=messagebox.showinfo('LeArN',content)
if __name__=="__main__":
 display("hello thangamani")
