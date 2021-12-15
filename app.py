import numpy as np
import cv2
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from config import data
import functions
from PIL import ImageTk, Image
from functools import partial
 

class Temp:
	def dummy(self,func):
		temp = functions.mapping[func]
		newImage = temp(self.root, self.img, self.spin)
		self.img = newImage
		self.image = ImageTk.PhotoImage(self.img)
		self.display()

	def display(self):
		try:
			self.canvas.config(width = self.image.width())
			self.canvas.config(height = self.image.height())
			self.canvas.create_image(0,0, anchor=NW, image=self.image)
		except:
			pass
		
	def __init__(self):
		self.image = []
		self.root = Tk()
		self.root.minsize(600, 700)
		
		Font_tuple = ("Times New Roman", 13, "bold")
		font_tuple = ("Times New Roman", 12, "bold")
		self.root.title(data['title'])
		
		#creating menubar and adding space
		menubar = Menu(self.root, bg="#09dec9", activebackground="#09dec9")
		
		space = Menu(menubar, tearoff = 0, bg="#09dec0", activebackground="#09de11",)
		menubar.add_cascade(label =' ', menu = space)
		
		menuItems = data['filters']
		
		for item in menuItems.keys():
			file = Menu(menubar, tearoff = 0, bg="#09dea0", activebackground="#09dec9")
			menubar.add_cascade(label =item, menu = file,font=Font_tuple)
			
			for value in menuItems[item]:
				if(value == ''):
					file.add_separator()
				else:
					temp = value.replace(" ","")
					file.add_command(label = value, command = partial(self.dummy, temp) , font = font_tuple)
			menubar.add_cascade(label =' ', menu = space)
				
		self.root.config(menu = menubar)

		#spinbox showing
		w = Label(self.root, text ='Filter Strength', font = "50", anchor='e')
		w.grid(row=0, column=0)
		self.spin = Spinbox(self.root, from_=1 ,to=10, textvariable="Filter Strength")
		self.spin.grid(row=0, column=1)
		#image showing
		array = np.ones((900,900))*150
		self.img = Image.fromarray(array)
		if self.img.mode == "F":
			self.img = self.img.convert('RGB')
		self.image = ImageTk.PhotoImage(self.img)
		self.canvas = Canvas(self.root, width = self.image.width(), height = self.image.height())      
		self.canvas.grid(row=1, column=0, columnspan=2)
		self.canvas.create_image(0,0, anchor=NW, image=self.image)
		
		self.root.columnconfigure(0, weight=1)
		self.root.columnconfigure(1, weight=1)
		self.root.rowconfigure(0, weight=1)
		self.root.rowconfigure(1, weight=5)
		self.root.mainloop()
if __name__ == '__main__':
	Temp()
	
	
	
	
	
