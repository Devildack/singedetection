# Import required Libraries
from sre_constants import SUCCESS
from tkinter import *
from PIL import Image, ImageTk
import hand_tracking_module as htm
import cv2
import voice

win= Tk()

# Set the size of the window
win.geometry("900x700")# Create a Label to capture the Video frames
web_frame = LabelFrame(win,text="Web cam")
web_frame.place(x=110,y=10)
label =Label(web_frame)
label.pack()


output_frame = LabelFrame(win,text="Output Frame")
output_frame.place(x=10,y=520)
hand_track_lable =Label(output_frame)
hand_track_lable.pack()
text_label =Label(output_frame)
text_label.pack()



cap= cv2.VideoCapture(0)
detect = htm.handDetector()

# Define function to show frame
def show_frames():
    # Get the latest frame and convert into Image
    sucess,img = cap.read()
    img = detect.findHands(img)
    mark_position =detect.findPosition(img,draw=False)
    if mark_position:
        id8,x1,x2=mark_position[8]
        id4,y1,y2=mark_position[4]
        dist = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
        hand_track_lable.configure(text="Hand Detect")
        if dist < 50:
            text_label.configure(text="okkkk")
        else:
            text_label.configure(text=" ")
    else:
        hand_track_lable.configure(text="No Hand Detect")

    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)

    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    

# Repeat after an interval to capture continiously
    label.after(20, show_frames)

show_frames()
win.mainloop()