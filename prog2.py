#  made by pratik kinage (thirstycode)
# https://github.com/thirstycode



# importing module tkinter
# first you need to install tkinter module
from tkinter import *

# create window using tkinter
win = Tk()
# title for window
win.title("Convertor")

# declaring input variable in tkinter
input1 = StringVar()

# label allows to insert text and photos (**for photos we need pillow)
w = Label(win,text="This Is Distance Convertor! Entry Value Here(In km) & Press Convert")
# grid specifies the position of objects to be displayed
w.grid(row = 0 , column = 0)

# function
def conversion():
    text1.insert(END, str(float(input1.get())*1000) + " grams")
    text2.insert(END, str(float(input1.get())*2.20462) + " pounds")
    text3.insert(END, str(float(input1.get())*35.274) + " ounches")

# input box declaration
# text variable is variable assigned to text typed in textbox
Input_box = Entry(win , textvariable = input1)
Input_box.grid(row = 1 , column = 0)

# command is the function to be called after pressing the button
# command only needs function name without parenthesis
button1 = Button(win,text = "Convert", command = conversion )
button1.grid(row = 2 , column = 0)

# declaring text box
text1 = Text(win,height = 1 , width = 40)
text1.grid(row = 3,column = 0)

text2 = Text(win,height = 1 , width = 40)
text2.grid(row = 4,column = 0)

text3 = Text(win,height = 1 , width = 40)
text3.grid(row = 5,column = 0)

w2 = Label(win,text="@developed BY Pratik")
w2.grid(row = 6 , column = 1)


win.mainloop()
