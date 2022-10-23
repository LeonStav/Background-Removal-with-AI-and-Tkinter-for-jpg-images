#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Essential packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation


# In[41]:


#Create the function for the background removal 
def Background_image():
    #Global variables
    global img, panel
    
    #Upload the image
    path = filedialog.askopenfilename()
    
    #Test if you have uploaded the image correctly
    if len(path) > 0:
        
        #Remove the background with opencv package
        segmentor = SelfiSegmentation()
        image = cv2.imread(path)
        edged = segmentor.removeBG(image, (255,255,255), threshold=0.7)

        # Resize image the image to fit in the panel
        if edged.shape > (900,900,3) and edged.shape <(1500,1500,3):
            scale_percent = 50 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA)
            
        elif edged.shape > (1500, 1500, 3):
            scale_percent = 25 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA) 
            
        elif edged.shape < (200,200,3):
            scale_percent = 200 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA)

        # Because the opencv represents the images in BGR order and PIL in RGB order we swap them.
        edged = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format
        edged = Image.fromarray(edged)

        # convert to ImageTk format
        edged = ImageTk.PhotoImage(edged)

        if panel is None:
            #Place the panel at the top after the button
            panel = Label(image=edged)
            panel.image = edged
            panel.pack(side="top", padx=10, pady=10)  
        else:
            # update the pannel
            panel.configure(image=edged)
            panel.image = edged


# In[53]:


#Create the function for the background removal 
def Background_image2():
    #Global variables
    global img, panel
    
    #Upload the image
    path = filedialog.askopenfilename()
    
    #Test if you have uploaded the image correctly
    if len(path) > 0:
        
        #Remove the background with opencv package
        segmentor = SelfiSegmentation()
        image = cv2.imread(path)
        edged = segmentor.removeBG(image, (255,255,255), threshold=0.6)

        # Resize image the image to fit in the panel
        if edged.shape > (900,900,3) and edged.shape <(1500,1500,3):
            scale_percent = 50 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA)
            
        elif edged.shape > (1500, 1500, 3):
            scale_percent = 25 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA) 
            
        elif edged.shape < (200,200,3):
            scale_percent = 200 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA)

        # Because the opencv represents the images in BGR order and PIL in RGB order we swap them.
        edged = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format
        edged = Image.fromarray(edged)

        # convert to ImageTk format
        edged = ImageTk.PhotoImage(edged)

        if panel is None:
            #Place the panel at the top after the button
            panel = Label(image=edged)
            panel.image = edged
            panel.pack(side="top", padx=10, pady=10)  
        else:
            # update the pannel
            panel.configure(image=edged)
            panel.image = edged


# In[56]:


#Create the function for the background removal 
def Background_image3():
    #Global variables
    global img, panel
    
    #Upload the image
    path = filedialog.askopenfilename()
    
    #Test if you have uploaded the image correctly
    if len(path) > 0:
        
        #Remove the background with opencv package
        segmentor = SelfiSegmentation()
        image = cv2.imread(path)
        edged = segmentor.removeBG(image, (255,255,255), threshold=0.5)

        # Resize image the image to fit in the panel
        if edged.shape > (900,900,3) and edged.shape <(1500,1500,3):
            scale_percent = 50 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA)
            
        elif edged.shape > (1500, 1500, 3):
            scale_percent = 25 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA) 
            
        elif edged.shape < (200,200,3):
            scale_percent = 200 # percent of original size
            width = int(edged.shape[1] * scale_percent / 100)
            height = int(edged.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            edged = cv2.resize(edged, dim, interpolation = cv2.INTER_AREA)

        # Because the opencv represents the images in BGR order and PIL in RGB order we swap them.
        edged = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format
        edged = Image.fromarray(edged)

        # convert to ImageTk format
        edged = ImageTk.PhotoImage(edged)

        if panel is None:
            #Place the panel at the top after the button
            panel = Label(image=edged)
            panel.image = edged
            panel.pack(side="top", padx=10, pady=10)  
        else:
            # update the pannel
            panel.configure(image=edged)
            panel.image = edged


# In[67]:


#Initialize the window
root = Tk()
panel = None

# Adjust the window
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title('Background Removal')
my_font1=('times', 18, 'bold')

#Create the button to trigger the file chooser dialog for the input
Btn1 = Button(root, text = "Select an image and remove the background with 70 threshold", width= 20, command = Background_image)
Btn1.pack(side = "top", fill = "both", expand = "no", padx = "20", pady = "10")
Btn2 = Button(root, text = "Select an image and remove the background with 60 threshold", width = 20, command = Background_image2)
Btn2.pack(side = "top", fill = "both", expand = "no", padx = "20", pady = "10")
Btn3 = Button(root, text = "Select an image and remove the background with 50 threshold", width = 20, command = Background_image3)
Btn3.pack(side = "top", fill = "both", expand = "no", padx = "20", pady = "10")
# Start the GUI

root.mainloop()


# In[ ]:




