# import the customtkinter and tkinter modules
import customtkinter as ctk
import tkinter as tk
from PIL import Image

# set the appearance mode and the default color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# create a class that inherits from ctk.CTk
class App(ctk.CTk):
  # define the __init__ method
  def __init__(self):
    # call the __init__ method of the parent class
    super().__init__()
    # set the title and geometry of the window
    self.title("My GUI")
    self.geometry("400x600")
    img = customtkinter.CTkImage(Image.open("poster.png"), size=(30, 30))
    # create a label widget with the image object
    label = ctk.CTkLabel(master=self, image=img)
    # place the label widget at the top center of the window
    label.grid(row=0, column=0, sticky="nsew")
    # create a button widget with the text "Click me"
    button = ctk.CTkButton(master=self, text="Click me")
    # place the button widget at the bottom center of the window
    button.grid(row=1, column=0, sticky="nsew")

# create an instance of the App class
app = App()
# start the GUI application
app.mainloop()
