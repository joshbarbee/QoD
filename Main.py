import tkinter as tk
from tkinter import *
import requests
import math

def main():
    
    root = tk.Tk()
    
    top = Frame(root)
    bottom = Frame(root)

    top.config(bg="lightgray")
    top.pack(side=TOP)

    bottom.config(bg="gray")
    bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
    root.title("Quote of the Day")
    root.overrideredirect(True)
    
    root.lift()
    root.wm_attributes("-transparentcolor", "white")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
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
    newl = Label(root,text = "Quotify v 0.05                                                              ", bg = None)
    newl.pack(in_=top, side=LEFT)

    b1 = Button(root,text = " X ",  command = root.destroy, bg = None)
    b1.config(width = 1, height = 1, borderwidth = 0)
    
    b1.pack(in_=top, side=RIGHT)

    lolbel = Label(root, text = "-       Quote of the day       -"+"\n"+"\n"+ a+ "\n-" + RESPONSE2, height = math.floor(len(new)/5+5), width = 35,font=('Georgia','10'), bg='gray')

    lolbel.pack(in_=bottom, side = BOTTOM)
    root.geometry("+1630+5")
    
    
    root.mainloop()
    
if __name__==('__main__'):
    main()
