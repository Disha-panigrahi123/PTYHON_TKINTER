from tkinter import *
from PIL import Image, ImageTk  # Import from Pillow

root = Tk()  # Create the main window

# Load the image using Pillow
image = Image.open("image/image-1.jpg")
resized_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
label = Label(root, image=img)
label.pack()

root.mainloop()  # Start the event loop
