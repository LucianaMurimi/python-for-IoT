# 1. import GUI library
from tkinter import *

# 2. create an object of type tkinter
window = Tk()

# 3. set: title, size(geometry), background-color
window.title('Graphical User Interface')
window.geometry('450x350')
window.configure(background='pink')

# 4. create label & entry
lbl1 = Label(window, text="Username",
             font=('Times New Roman', 10))
lbl1.place(x=30, y=40)

e1 = Entry(window,
           font=('Times New Roman', 10))
e1.place(x=100, y=40)

lbl2 = Label(window, text="Password",
             font=('Times New Roman', 10))
lbl2.place(x=30, y=80)

e2 = Entry(window, show='*',
           font=('Times New Roman', 10))
e2.place(x=100, y=80)

# 5. create buttons
btn1 = Button(window, text='Submit',
              font=('Times New Roman', 10),
              # width = '10',
              bg='green',
              fg='pink')
btn2 = Button(window, text='Cancel',
              font=('Times New Roman', 10),
              # width = '10',
              bg='red',
              fg='pink')

btn1.place(x=30, y=120)
btn2.place(x=100, y=120)

window = mainloop()
