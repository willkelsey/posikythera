from tkinter import *
from Antikythera import planentpos as p
from Antikythera import hohmann
from Antikythera import event
from Antikythera.simulation import simulate
from Antikythera.coordinates import coordinates
import sqlite3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime as d
import time

root = Tk()
connection = sqlite3.connect('Antikythera/events.db')
crsr = connection.cursor()
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
#labels
year_label = Label(root, text='Year').grid(row=0)
month_label = Label(root, text="Month").grid(row=1)
day_label = Label(root, text="Day").grid(row=2)
hohmann_label_orign = Label(root, text="Origin").grid(row=4)
hohmann_label_destination = Label(root, text="Destination").grid(row=5)
search_event_date = Label(root, text="Search for event by date").grid(row=7)
search_event_event = Label(root, text="Search for event by event type").grid(row=7, column=1)
#setup to get value from entry
content_hohmann_origin = StringVar()
content_hohmann_destination = StringVar()
content_year = StringVar()
content_month = StringVar()
content_day = StringVar()
content_event_event = StringVar()
content_event_date_begin = StringVar()
content_event_date_end = StringVar()
#entry boxes
entry_year = Entry(root, textvariable=content_year).grid(row=0, column=1)
text = content_year.get()
content_year.set(text)

entry_month = Entry(root, textvariable=content_month).grid(row=1, column=1)
text = content_month.get()
content_month.set(text)

entry_day = Entry(root, textvariable=content_day).grid(row=2, column=1)
text = content_day.get()
content_day.set(text)

#entry_event_event = Entry(root, textvariable=content_event_event).grid(row=8, column=1)
text = content_event_event.get()
content_event_event.set(text)

entry_event_date_begin = Entry(root, textvariable=content_event_date_begin).grid(row=8, column=0)
entry_event_date_end = Entry(root, textvariable=content_event_date_end).grid(row=9)

#planet_info_label = Label(root, text=" Click on a planet to display that planet's information").grid(row=10)


#initialize sim

y = 2000
m = 1
d = 1
run = 0

T = p.calc_date(y, m, d, 12, 0, 0)

xcoords, ycoords, zcoords = simulate(T)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(xcoords, ycoords, zcoords, cmap='jet')

ax.set_xlim3d([-40, 40])
ax.set_xlabel('X')

ax.set_ylim3d([-40, 40])
ax.set_ylabel('Y')

ax.set_zlim3d([-40, 40])
ax.set_zlabel('Z')

ax.set_title('Antikythera')
planets = ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
#for i, word in enumerate(planets):
    #ax.text(xcoords[i], ycoords[i], zcoords[i], word)
fig.show()

def togglePP():
    global run
    if run == 0:
        run = 1
        while run == 1:
            animate()
    else:
        run = 0

#callback functions for buttons
def go_to_time():
    global y
    global m
    global d
    gy = content_year.get()
    gm = content_month.get()
    gd = content_day.get()
    y = int(gy, 10)
    m = int(gm, 10)
    d = int(gd, 10)

    print("going to: ")
    print(y, m, d)
    xcoords, ycoords, zcoords = coordinates(y, m, d)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xcoords, ycoords, zcoords, cmap='jet')

    ax.set_xlim3d([-40, 40])
    ax.set_xlabel('X')

    sc._offsets3d = (xcoords, ycoords, zcoords)
    return d,m,y

def animate():
    global y
    global m
    global d
    global run
    plt.pause(0.1)
    print("going to: ")
    print(y, m, d)
    xcoords, ycoords, zcoords = coordinates(y, m, d)
    sc._offsets3d = (xcoords, ycoords, zcoords)
    ##for i, word in enumerate(planets):
        ## x.text(xcoords[i], ycoords[i], zcoords[i], word)
#        if d == 31:
#            m += 1
#            d = 1
#            if m == 12:
#                y += 1
#                m = 1
#        else:
#            d += 1
    if m == 12:
        y += 1
        m = 1
    else:
        m += 1
    return d,m,y

def execute_hohmann():
    orig = content_hohmann_origin.get()
    dest = content_hohmann_destination.get()
    hohmann.hohmann(orig, dest)


def search_event_event():
    s = content_event_event.get()
    crsr.execute("SELECT * FROM event WHERE type=?", (s,))
    results = crsr.fetchall()
    for i in results:
        print(i)


def search_event_date():
    s = content_event_date_begin.get()
    de = content_event_date_end.get()
    start = d.datetime.strptime(s, "%Y-%m-%d")
    end = d.datetime.strptime(de, "%Y-%m-%d")
    crsr.execute("SELECT * FROM event WHERE date BETWEEN ? AND ?", (start, end))
    results = crsr.fetchall()
    for i in results:
        print(i)

def display_planet_info() :
    # p  = display_planet_info.get()
    print("Displaying planet info...")


planet_list = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
event_types = ['solar eclipse', 'lunar eclipse']

#spinbox maybe will work for hohmann select
hohmann_spinbox_origin = Spinbox(root, state="readonly", values=planet_list, textvariable=content_hohmann_origin).grid(row=4, column=1)
hohmann_spinbox_destination = Spinbox(root, state="readonly", values=planet_list, textvariable=content_hohmann_destination).grid(row=5, column=1)
search_event_spinbox = Spinbox(root, state="readonly", values=event_types, textvariable=content_event_event).grid(row=8, column=1)

# buttons
button_go_to_time = Button(root, text="Go To Time", command=go_to_time).grid(row=3, column=1)
button_play_pause = Button(root, text="Play/Pause", command=togglePP) .grid(row=3, column=0)
button_hohmann = Button(root, text="Calculate travel window", command=execute_hohmann).grid(row=6, column=1)
button_search_event_event = Button(root, text="Search by event", command=search_event_event).grid(row=9, column=1)
button_search_event_date = Button(root, text="Search by date", command=search_event_date).grid(row=10, column=0)



# buttons for displaying planet info
button_Mercury = Button(root, text="Mercury", command=display_planet_info).grid(row=14, column=0)
button_Venus = Button(root, text="Venus", command=display_planet_info).grid(row=14, column=1)
button_Earth = Button(root, text="Earth", command=display_planet_info).grid(row=15, column=0)
button_Mars = Button(root, text="Mars", command=display_planet_info).grid(row=15, column=1)
button_Jupiter = Button(root, text="Jupiter", command=display_planet_info).grid(row=16, column=0)
button_Saturn = Button(root, text="Saturn", command=display_planet_info).grid(row=16, column=1)
button_Uranus = Button(root, text="Uranus", command=display_planet_info).grid(row=17, column=0)
button_Neptune = Button(root, text="Neptune", command=display_planet_info).grid(row=17, column=1)
button_Pluto = Button(root, text="Pluto", command=display_planet_info).grid(row=18, column=0)

# keep the gui open until closed
mainloop()
