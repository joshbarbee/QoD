import tkinter as tk
from tkinter import *
import requests
import math
root = tk.Tk()
root.title("Quote of the Day")
root.overrideredirect(True)

root.lift()
root.wm_attributes("-transparentcolor", "white")
root.wm_attributes("-disabled", True)
root.attributes('-alpha', 0.8)
root.iconbitmap("icon.png")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

link = requests.get('https://talaikis.com/api/quotes/random/')
RESPONSE = link.json()['quote']   
RESPONSE2 = link.json()['author']
new = RESPONSE.split(" ")

l = []
b = []
a = ""
for i in range(0,len(new),5):
    
    l+=(new[i:i+5],''+'\n')
    
for i in l:
    a += ' '.join(i)
m = a.split("\n")

b.sort(reverse=True)

lolbel = Label(root, text = "Quote of the day"+"\n"+"\n"+ a+ "\n-" + RESPONSE2, height = math.floor(len(new)/5+5), width = 35,font=('Georgia','10'), bg='gray')

lolbel.pack(side = tk.BOTTOM)
root.geometry("+1630+5")
root.smooth=1
root.mainloop()
