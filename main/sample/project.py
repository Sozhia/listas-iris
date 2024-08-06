import csv
import math
import pathlib
import tkinter as tk   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def load_file(url):
  with open (url, 'r') as file:
    csv_reader = csv.reader(file)
    dataset = [row for row in csv_reader if row]
  return dataset


from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

dataset = load_file(file_path)
print(dataset)