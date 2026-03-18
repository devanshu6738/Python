# A file is a collection of data or information stored on a computer or storage device (like a hard disk, SSD, or USB drive) that is identified by a name and a file extension (like .txt, .jpg, .pdf).
# File handling in Python refers to the process of working with files, which are used to store data on a computer's storage system.
# Files can be used to store a wide range of information, such as:
# Text
# Numbers
# Images
# And more
# In Python, you can perform various operations on files, such as:
# Creating files
# Reading content
# Writing data
# Updating existing content

# See all the files in your directory
import os
def show_file():   #list all the folder 
    folder="D:\\Python"

    items=os.listdir(folder)
    for i in items:
        print(i)

show_file()


# Read the file and open in the console

def open_file():
    file_path="D:\\Python\\filehandling.txt"
    try:
        with open(file_path,'r') as file:
            for line in file:
                number=int(line.strip())
                print(number)
    
    except FileNotFoundError:
        print("File is not present")


open_file()
