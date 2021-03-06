# 1. import GUI library
from tkinter import *
from tkcalendar import Calendar, DateEntry

# 2. create an object of type tkinter
window = Tk()

# 3. set: title, size(geometry), background-color
window.title('Registration Form')
window.geometry('530x420')
window.configure(background='#f2f2f2')

# 4. brand logo image
imgCanvas = Canvas(window)
img = PhotoImage(file="logo.png")
imgCanvas.create_image(5,5, anchor=NW, image=img)
imgCanvas.place(x=200, y=0)

# 5. create labels & entrys
# Row 1
firstNameLbl = Label(window, text="First Name",
             font=('Times New Roman', 10))
firstNameLbl.place(x=30, y=100)
firstNameEtry = Entry(window,
           font=('Times New Roman', 10))
firstNameEtry.place(x=100, y=100)

lastNameLbl = Label(window, text="Last Name",
             font=('Times New Roman', 10))
lastNameLbl.place(x=300, y=100)
lastNameEtry = Entry(window,
           font=('Times New Roman', 10))
lastNameEtry.place(x=370, y=100)
#=============================================================

# Row 2
genderLbl = Label(window, text="Gender",
             font=('Times New Roman', 10))
genderLbl.place(x=30, y=140)
maleBtn = Radiobutton(window, text="Male", value="Male")
maleBtn.place(x=100, y=140)
femaleBtn = Radiobutton(window, text="Female", value="Female")
femaleBtn.place(x=100, y=180)

DOBLbl = Label(window, text="D.O.B",
             font=('Times New Roman', 10))
DOBLbl.place(x=300, y=140)
DOBEtry = DateEntry(window, width='17',
                    background='#b8b8b8',
                    foreground='#000000',
                    headersbackground='#cccccc',
                    selectbackground='#229e02')
DOBEtry.place(x=370, y=140)
#=============================================================

# Row 3
phoneNoLbl = Label(window, text="Phone",
             font=('Times New Roman', 10))
phoneNoLbl.place(x=30, y=220)
phoneNoEtry = Entry(window,
           font=('Times New Roman', 10))
phoneNoEtry.place(x=100, y=220)

emailLbl = Label(window, text="Email",
             font=('Times New Roman', 10))
emailLbl.place(x=300, y=220)
emailEtry = Entry(window,
           font=('Times New Roman', 10))
emailEtry.place(x=370, y=220)

#=============================================================

# Row 4
countryLbl = Label(window, text="Country",
             font=('Times New Roman', 10))
countryLbl.place(x=30, y=260)

options = StringVar(window)
options.set("select a country")    # default value
countryOptn = OptionMenu(window, options, "Kenya", "Tanzania", "Uganda", "Rwanda", "South Sudan", "Burundi",)
countryOptn.place(x=100, y=260)

cityLbl = Label(window, text="City",
             font=('Times New Roman', 10))
cityLbl.place(x=300, y=260)
cityEtry = Entry(window,
           font=('Times New Roman', 10))
cityEtry.place(x=370, y=260)

# 6. create buttons
cancelBtn = Button(window, text='Cancel',
              font=('Times New Roman', 10),
              width='10',
              padx='5', pady='3',
              bg='#cc474b')
submitBtn = Button(window, text='Submit',
              font=('Times New Roman', 10),
              width = '10',
              padx='5', pady='3',
              bg='#31fc03')

cancelBtn.place(x=150, y=330)
submitBtn.place(x=280, y=330)


window = mainloop()