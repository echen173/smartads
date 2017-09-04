mport os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tkinter as tk
from PIL import ImageTk, Image

#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

directoryPath = '/Users/eli/Documents/SmartAds/'

directory = os.fsencode(directoryPath)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        #do something
        continue
    else:
        #do something
        continue
    
#This creates the main window of an application
window = tk.Tk()
window.title("TEST")
window.geometry("300x300")
window.configure(background='grey')

path = '/Users/eli/Documents/SmartAds/Test1.jpg'

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()

