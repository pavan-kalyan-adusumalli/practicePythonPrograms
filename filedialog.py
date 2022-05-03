# 32) Write a program that opens a file dialog that allows you to select a text file. The program

from tkinter import filedialog as fd
filename = fd.askopenfilename()
f = open(filename, "r")
for line in f.readlines():
    print(line, end="")
f.close()
