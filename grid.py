import tkinter as tk

root = tk.Tk()
root.title("Grid Example")
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
label1.grid(row=0, column=0)  
label2.grid(row=1, column=10)  
button1.grid(row=2, column=0) 
button2.grid(row=2, column=1) 

root.mainloop()
