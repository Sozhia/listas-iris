#!/usr/bin/python3

import csv
import math
import pathlib
import tkinter as tk   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

class Iris:
  
  def __init__(self, type, data) -> None:
    self.type = type
    self.data = {
      'sepal_length' : data[0],
      'sepal_width' : data[1],
      'petal_length' : data[2],
      'petal_width' : data[3]
    }

  def __str__(self):
    return f"Type: {self.type}, Measures: {self.data}"

def load_dataset(datafile):
  with open (datafile, 'r') as file:
    csv_reader = csv.reader(file)
    dataset = [row for row in csv_reader if row]
  return dataset

def format_dataset(dataset):
  
  formated_dataset= []
  
  for row in dataset:
    flower_type = row[-1]
    flower_data = list(row[:-1])
    new_flower = Iris(flower_type,flower_data)
    formated_dataset.append(new_flower)
  return formated_dataset

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

rawdataset = load_dataset(file_path)

collection = format_dataset(rawdataset)

for element in collection:
  print(element)

