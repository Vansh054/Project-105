import pandas as pd 
import plotly.express as pe
import csv
import math

f = open("data.csv")
csvObject = csv.reader(f)
fileData = list(csvObject)
number = []
add = 0
mean = 0

for i in fileData[0]:
    h = float(i)
    number.append(h)
    add = add + h

mean = add/len(number)
addition = 0

for i in fileData[0]:
    a = int(i) - mean
    square = a * a
    addition = addition + square

lengths = len(fileData[0])-1
final = addition/lengths
stdDerive = math.sqrt(final)

print('Standard Derivation : ' + str(stdDerive))
