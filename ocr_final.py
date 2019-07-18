import PIL.Image
import pytesseract
from tkinter import *
from tkinter.filedialog import *
import cv2

root=Tk()
root.withdraw()
root.fileName=askopenfilename(filetypes=( ("Image","*.*"),("All files","*.*") ))
name=root.fileName

im=PIL.Image.open(name)

text=pytesseract.image_to_string(im,lang='eng')

print(text)
