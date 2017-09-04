mport os
import sys
import random

from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk


path = r'C:\Users\danie\Desktop\Business'

images = []

for dirname, dirnames, filenames in os.walk(path):
   # print path to all subdirectories first.
   # for subdirname in dirnames:
       # print os.path.join(dirname, subdirname)

   # print path to all filenames.
   for filename in filenames:
       file = os.path.join(dirname, filename)
       if '.jpg' in file.lower() or '.gif' in file.lower() or '.png' in file.lower():
           images.append(file)


random_max = random.randrange(2, 5)
print (random_max)

selection = []
counter = 0
while counter < random_max:
   index = random.randrange(0, len(images))
   selection.append(images[index])
   print (images[index])
   images.pop(index)
   counter +=1



print (selection)


## Main window
root = Tk()
## Grid sizing behavior in window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
## Canvas
cnv = Canvas(root)
cnv.grid(row=0, column=0, sticky='nswe')
## Scrollbars for canvas
hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
hScroll.grid(row=1, column=0, sticky='we')
vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=1, sticky='ns')
cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
## Frame in canvas
frm = Frame(cnv)
## This puts the frame in the canvas's scrollable zone
cnv.create_window(0, 0, window=frm, anchor='nw')
## Frame contents

for s in selection:
   im = Image.open(s)
   tkimage = ImageTk.PhotoImage(im)
   myvar=Label(frm,image = tkimage)
   myvar.image = tkimage
   myvar.pack()

## Update display to get correct dimensions
frm.update_idletasks()
## Configure size of canvas's scrollable zone
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
## Go!


root.mainloop()
