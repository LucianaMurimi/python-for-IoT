#Graphical User Interface
from tkinter import *

#creating an object of type tkinter
window = Tk()   #object = class
window.configure(background = 'pink' )
window.title('Graphical User Interface')
window.geometry('550x550')  #size of the window

#creating buttons
btn1 = Button(window, text = 'Send',
                width = '10',
                bg = 'blue',
                fg = 'yellow')
btn2 = Button(window, text = 'Receive',
                width = '10',
                bg = 'blue',
                fg = 'yellow')
#btn1.pack() #to show the button; making it viscible
# btn1.grid(column = 1, row = 1, columnspan = 3, rowspan = 2, ipadx = 4, ipady = 4, padx = 4, pady = 4)
# btn2.grid(column = 6, row = 4)

btn1.place(x=250, y=250)
btn2.place(x=450, y=500)

window = mainloop() #include mainloop as end of program