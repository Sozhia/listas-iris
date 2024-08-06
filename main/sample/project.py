import csv
import math
import pathlib
import tkinter as tk   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

def load_dataset(datafile):
  with open (datafile, 'r') as file:
    csv_reader = csv.reader(file)
    dataset = [row for row in csv_reader if row]
  return dataset

def format_dataset(dataset):
  
  formated_dataset= []
  
  for row in dataset:
    flower_type = row[-1]
    
    if flower_type  not in formated_dataset:
      formated_dataset.append(flower_type)
    
    flower_data = list(row[:-1])
    flower_index = formated_dataset.index(flower_type) + 1
    
    formated_dataset.insert(flower_index, flower_data)
  return formated_dataset
     
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

rawdataset = load_dataset(file_path)

print(format_dataset(rawdataset))

