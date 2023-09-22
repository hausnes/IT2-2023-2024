import customtkinter as ctk
import tkinter as tk
from PIL import Image

# set the appearance mode and the default color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.title("Filmplakat!")
    self.geometry("320x418")
    
    # Bilde
    img = ctk.CTkImage(Image.open("poster.png"), size=(320, 388))
    label = ctk.CTkLabel(master=self, image=img) # create a label widget with the image object
    label.grid(row=0, column=0, sticky="nsew") # place the label widget at the top center of the window
    label.configure(text="Jaws")
    
    # Knapp
    button = ctk.CTkButton(master=self, text="Finn plakat")
    button.grid(row=1, column=0, sticky="nsew") # place the button widget at the bottom center of the window

# create an instance of the App class
app = App()
# start the GUI application
app.mainloop()