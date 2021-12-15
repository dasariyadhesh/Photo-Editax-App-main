import numpy as np
import cv2
from PIL import ImageTk, Image  
import numpy as np
from tkinter import Tk,Spinbox,Button, Label
from tkinter.filedialog import askopenfilename
import secrets
import string
import threading
import time

def OpenImage(root, image, spin):
	print('open image')
	try:
		Tk().withdraw() 
		filename = askopenfilename() 
		return Image.open(filename)
	except:
		print("Choose correct file")
		return image
def Save(root, image, spin):
	try:
		print("Save image")
		image.save('ark.jpg')
		print("after saving")
		return image
	except:
		return image
def Exit(root, image, spin):
	print("Exit")
	root.destroy()
	exit()
def Averaging(root, image,spin):
	print("Averaging Blur")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		blur = cv2.blur(data,(n,n))
		return Image.fromarray(blur)
	except:
		showpop("May be you used wrong input")
def GaussianBlurring(root, image,spin):
	print("Guassian Blur")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		if(n%2 == 0):
			showpop("Use odd values only for Guassian Kernel")
			return image
		blur = cv2.GaussianBlur(data,(n,n),0)
		return Image.fromarray(blur)
	except:
		showpop("May be you used wrong input")
def	MedianBlurring(root, image,spin):
	print("Median Blur")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		if(n%2 == 0):
			showpop("Use odd values only for Median Blur")
			return image
		blur = cv2.medianBlur(data,n)
		return Image.fromarray(blur)
	except:
		showpop("May be you used wrong input")

def	BilateralFiltering(root, image,spin):
	try:
		print("Bilateral Filtering")
		data = np.asarray(image)
		n = int(spin.get())
		blur = cv2.bilateralFilter(data,n,75,75)
		return Image.fromarray(blur)
	except:
		return image
def	Convolution2D(root, image,spin):
	print("Convolution 2D Filter")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		kernel = np.ones((n,n),np.float32)/25
		blur = cv2.filter2D(data,-1,kernel)
		return Image.fromarray(blur)
	except:
		showpop("May be you used wrong input")
		return image
def	RGB2GRAY(root, image,spin):
	print("RGB to Gray")
	try:
		data = np.asarray(image)
		blur = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
		return Image.fromarray(blur)
	except:
		showpop("Something went wrong")
		return image
def	RGB2HSV(root, image,spin):
	print("RGB to HSV")
	try:
		data = np.asarray(image)
		blur = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)
		print(data.shape, blur.shape)
		return Image.fromarray(blur)
	except:
		showpop("Gray Scale images are not allowed HSV filter")
		return image
def	RGB2HLS(root, image,spin):
	print("RGB to HLS")
	try:
		data = np.asarray(image)
		blur = cv2.cvtColor(data, cv2.COLOR_RGB2HLS)
		return Image.fromarray(blur)
	except:
		showpop("May be you used wrong input")
		return image
def	Scaling(root, image,spin):
	print("Scaling")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		sample = {
			10:3,
			9:2,
			8:1,
			7:0.9,
			6:0.8,
			5:0.7,
			4:0.6,
			3:0.5,
			2:0.4,
			1:0.3
		}
		n = sample[n]
		blur = cv2.resize(data,None,fx=n, fy=n, interpolation = cv2.INTER_CUBIC)
		return Image.fromarray(blur)
	except:
		return image
def	Translation(root, image,spin):
	print("Translation")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		rows,cols,channels = data.shape
		sample = {
			10:-100,
			9:-50,
			8:-30,
			7:-10,
			6:-5,
			5:10,
			4:20,
			3:40,
			2:50,
			1:100
		}
		M = np.float32([[1,0,sample[n]],[0,1,sample[n]]])
		dst = cv2.warpAffine(data,M,(cols,rows))
		return Image.fromarray(dst)
	except:
		showpop("Something went wrong")
		return image
def	Rotation(root, image,spin):
	print("Rotation")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		rows,cols,channels = data.shape
		M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),n*10,1)
		dst = cv2.warpAffine(data,M,(cols,rows))
		return Image.fromarray(dst)
	except:
		showpop("Something went wrong")
		return image
def	AffineTransformation(root, image,spin):
	print("Affine Transform")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		rows,cols,channels = data.shape
		pts1 = np.float32([[50,50],[200,50],[50,200]])
		pts2 = np.float32([[10,100],[200,50],[100,250]])
		M = cv2.getAffineTransform(pts1,pts2)
		dst = cv2.warpAffine(data,M,(cols,rows))
		return Image.fromarray(dst)
	except:
		showpop("Something went wrong")
		return image
def	Laplacian(root, image,spin):
	print("Laplace transform")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		if(n%2 == 0):
			showpop("Use odd values only for Laplacian")
			return image
		laplacian = cv2.Laplacian(data,cv2.CV_64F)
		
		return Image.fromarray((laplacian * 255).astype(np.uint8))
	except:
		showpop("Something went wrong")
		return image
def	SobelX(root, image,spin):
	print("SobelY gradient")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		if(n%2 == 0):
			showpop("Use odd values only for Laplacian")
			return image
		sobelx = cv2.Sobel(data,cv2.CV_64F,1,0,ksize=int(n/2))
		
		return Image.fromarray((sobelx * 255).astype(np.uint8))
	except:
		showpop("Something went wrong")
		return image
def	SobelY(root, image,spin):
	print("SobelX gradient")
	try:
		data = np.asarray(image)
		n = int(spin.get())
		if(n%2 == 0):
			showpop("Use odd values only for Laplacian")
			return image
		sobelx = cv2.Sobel(data,cv2.CV_64F,0,1,ksize=int(n/2))
		
		return Image.fromarray((sobelx * 255).astype(np.uint8))
	except:
		showpop("Something went wrong")
		return image
def	Canny(root, image,spin):
	try:
		print("Canny edge detection")
		data = np.asarray(image)	
		edges = cv2.Canny(data,100,200)
			
		return Image.fromarray(edges)
	except:
		showpop("Something went wrong")
		return image
def	ImageBlending(root, image,spin):
	try:
		n = int(spin.get())
		alpha = n/10.0
		A = np.asarray(image)
		B = np.asarray(OpenImage(root, image,spin))
		B = cv2.resize(B, (A.shape[1], A.shape[0]), interpolation = cv2.INTER_AREA)
		beta = (1.0 - alpha)
		dst = np.uint8(alpha*(A)+beta*(B))
		return Image.fromarray(dst)
	except:
		return image
def showpop(string):
	top = Tk()
	top.title("Error")
	l = Label(top, text=string)
	l.pack()
	top.mainloop()
	return 
mapping = {
	"OpenImage":OpenImage,
	"Save":Save,
	"Exit":Exit,
	"Averaging":Averaging,
	"GaussianBlurring":GaussianBlurring,
	"MedianBlurring":MedianBlurring,
	"BilateralFiltering":BilateralFiltering,
	"Convolution2D":Convolution2D,
	"RGB2GRAY":RGB2GRAY,
	"RGB2HSV":RGB2HSV,
	"RGB2HLS":RGB2HLS,
	"Scaling":Scaling,
	"Translation":Translation,
	"Rotation":Rotation,
	"AffineTransformation":AffineTransformation,
	"Laplacian":Laplacian,
	"SobelX":SobelX,
	"SobelY":SobelY,
	"Canny":Canny,
	"ImageBlending":ImageBlending,
}
