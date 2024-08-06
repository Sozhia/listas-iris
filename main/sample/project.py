import csv
import math
import pathlib
from Tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def load_file(url):
  with open (url, 'r') as file:
    csv_reader = csv.reader(file)
    dataset = [row for row in csv_reader if row]
  return dataset




Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)