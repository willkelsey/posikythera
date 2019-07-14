from tkinter import *


root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
year_label = Label(root, text='Year').grid(row=0)
month_label = Label(root, text="Month").grid(row=1)
day_label = Label(root, text="Day").grid(row=2)
hohmann_label_orign = Label(root, text="Origin").grid(row=4)
hohmann_label_destination = Label(root, text="Destination").grid(row=5)
content_hohmann_origin = StringVar()
content_hohmann_destination = StringVar()
content_year = StringVar()
content_month = StringVar()
content_day = StringVar()

entry_year = Entry(root, textvariable=content_year).grid(row=0, column=1)
text = content_year.get()
content_year.set(text)

entry_month = Entry(root, textvariable=content_month).grid(row=1, column=1)
text = content_month.get()
content_month.set(text)

entry_day = Entry(root, textvariable=content_day).grid(row=2, column=1)
text = content_day.get()
content_day.set(text)

entry_hohmann_origin = Entry(root, textvariable=content_hohmann_origin).grid(row=4, column=1)
text = content_hohmann_origin.get()
content_hohmann_origin.set(text)

entry_hohmann_destination = Entry(root, textvariable=content_hohmann_destination).grid(row=5, column=1)
text = content_hohmann_destination.get()
content_hohmann_destination.set(text)

def go_to_time():
    y = content_year.get()
    m = content_month.get()
    d = content_day.get()
    y = int(y, 10)
    m = int(m, 10)
    d = int(d, 10)
    print("going to: ")
    print(y, m, d)

def print_year():
    s = content_year.get()
    s = int(s, 10)
    print(s)


def print_month():
    s = content_month.get()
    s = int(s, 10)
    print(s)


def print_day():
    s = content_day.get()
    s = int(s, 10)
    print(s)

def execute_hohmann():
    print("Hohman")
    #     o = eval(content_hohmann_origin.get())
    #     d = eval(content_hohmann_destination.get())


button_year = Button(root, text="Print Year", width=10, command=print_year).grid(row=0, column=2)
button_month = Button(root, text="Print Month", width=10, command=print_month).grid(row=1, column=2)
button_day = Button(root, text="Print Day", width=10, command=print_day).grid(row=2, column=2)
button_go_to_time = Button(root, text="Go To Time", width=50, command=go_to_time).grid(row=3)
button_hohmann = Button(root, text="Calculate travel window", width=50, command=execute_hohmann).grid(row=6)

mainloop()
