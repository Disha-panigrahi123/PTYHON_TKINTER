import tkinter as tk

def submit_form():
    name = entry_name.get()  # Get the name from the entry
    email = entry_email.get()  # Get the email from the entry
    print(f"Name: {name}\nEmail: {email}")

# Create the main window
root = tk.Tk()
root.title("Entry Example")

# Create labels for name and email
label_name = tk.Label(root, text="Name:")
label_email = tk.Label(root, text="Email:")

# Create entry fields for name and email
entry_name = tk.Entry(root, width=30)
entry_email = tk.Entry(root, width=30)

# Create a submit button
button_submit = tk.Button(root, text="Submit", command=submit_form)

# Place the labels, entry fields, and button in the grid
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email.grid(row=1, column=1, padx=10, pady=10)

button_submit.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
import tkinter as tk

def submit_form():
    name = entry_name.get()  # Get the name from the entry
    email = entry_email.get()  # Get the email from the entry
    print(f"Name: {name}\nEmail: {email}")

# Create the main window
root = tk.Tk()
root.title("Entry Example")

# Create labels for name and email
label_name = tk.Label(root, text="Name:")
label_email = tk.Label(root, text="Email:")

# Create entry fields for name and email
entry_name = tk.Entry(root, width=30)
entry_email = tk.Entry(root, width=30)

# Create a submit button
button_submit = tk.Button(root, text="Submit", command=submit_form)

# Place the labels, entry fields, and button in the grid
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email.grid(row=1, column=1, padx=10, pady=10)

button_submit.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
