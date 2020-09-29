import tkinter as tk
import pyjokes

root = tk.Tk()
root.title("Jokes Game")
root.geometry("400x400")
root.configure(bg="black")

def joke():
    global joke
    joke = pyjokes.get_joke()
    T.insert(tk.END,joke)

def clear():
    T.delete("1.0","end")

T = tk.Text(root)
T.place(x=5,y=5,height=200,width=390)
b1 = tk.Button(root, text="Smash me!", bg="violet",fg="black",command=joke)
b1.place(x=20,y=220,height=40,width=80)
b1 = tk.Button(root, text="Clear", bg="violet",fg="black",command=clear)
b1.place(x=105,y=220,height=40,width=80)

root.mainloop()
