from tkinter import *
import planentpos as p
import hohmann
import event
from simulation import simulate
from coordinates import coordinates
import sqlite3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime as dt
import time
import os
import itertools

root = Tk()
filepath = os.path.abspath('events.db')
connection2 = sqlite3.connect('planet.db')
connection = sqlite3.connect(filepath)
crsr = connection.cursor()
crsr2 = connection2.cursor()
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

y = 2019
m = 8
d = 6
run = 0

T = p.calc_date(y, m, d, 12, 0, 0)

xcoords, ycoords, zcoords = simulate(T)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
planets = ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
sc = ax.scatter(xcoords, ycoords, zcoords, cmap='jet', color=['#F7DC6F', '#444a41', 'g', '#244573', 'w', 'r', '#e07a04', '#6bc2c9', 'b', '#8e6aa6', 'k'], s=[260,3.8,9.5,10,2.5,5.3,111.9,94,40.4,38.3,1.8], depthshade=FALSE)


ax.set_xlim3d([-40, 40])
ax.set_xlabel('X')
ax.set_ylim3d([-40, 40])
ax.set_ylabel('Y')

ax.set_zlim3d([-40, 40])
ax.set_zlabel('Z')

ax.set_title('Antikythera')
fig.show()
def togglePP():
    global run
    if run == 0:
        run = 1
        while run == 1:
            animate()
    else:
        run = 0

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
    if (m > 12) or (m < 1):
        print("Invalid month")
    elif (d > 31) or (d < 1):
        print("Invalid day")
    elif (m == 2) & (d > 28):
        print("Invalid entry")
    elif (m == 4) & (d > 30):
        print("Invalid entry")
    elif (m == 6) & (d > 30):
        print("Invalid entry")
    elif (m == 9) & (d > 30):
        print("Invalid entry")
    elif (m == 11) & (d > 30):
        print("Invalid entry")
    else:
        print("Going to:", m,'/', d ,'/', y)

        sc._offsets3d = (xcoords, ycoords, zcoords)
        return d, m, y


def animate():
    global y
    global m
    global d
    global run
    plt.pause(0.01)
    print('Current Date:', m, '/', d, '/', y)
    xcoords, ycoords, zcoords = coordinates(y, m, d)
    sc._offsets3d = (xcoords, ycoords, zcoords)
    if m == 1:
        if d == 31:
            m = 2
            d = 1
        else:
            d += 1
    elif m == 2:
        if d == 28:
            m = 3
            d = 1
        else:
            d += 1
    elif m == 3:
        if d == 31:
            m = 4
            d = 1
        else:
            d += 1
    elif m == 4:
        if d == 30:
            m = 5
            d = 1
        else:
            d += 1
    elif m == 5:
        if d == 31:
            m = 6
            d = 1
        else:
            d += 1
    elif m == 6:
        if d == 30:
            m = 7
            d = 1
        else:
            d += 1
    elif m == 7:
        if d == 31:
            m = 8
            d = 1
        else:
            d += 1
    elif m == 8:
        if d == 31:
            m = 9
            d = 1
        else:
            d += 1
    elif m == 9:
        if d == 30:
            m = 10
            d = 1
        else:
            d += 1
    elif m == 10:
        if d == 31:
            m = 11
            d = 1
        else:
            d += 1
    elif m == 11:
        if d == 30:
            m = 12
            d = 1
        else:
            d += 1
    elif m == 12:
        if d == 31:
            m = 1
            d = 1
            y += 1
        else:
            d += 1

    return d, m, y

def execute_hohmann():
    orig = content_hohmann_origin.get()
    dest = content_hohmann_destination.get()
    hohmann.hohmann(orig, dest,y,m,d)

def search_event_event():
    s = content_event_event.get()
    crsr.execute("SELECT * FROM event WHERE type=?", (s,))
    results = crsr.fetchall()
    for i in results:
        print(i)

def search_event_date():
    s = content_event_date_begin.get()
    de = content_event_date_end.get()
    start = dt.datetime.strptime(s, "%Y-%m-%d")
    end = dt.datetime.strptime(de, "%Y-%m-%d")
    crsr.execute("SELECT * FROM event WHERE date BETWEEN ? AND ?", (start, end))
    results = crsr.fetchall()
    for i in results:
        print(i)

def mercury():
    crsr2.execute("SELECT * FROM planet where name = 'Mercury'")
    results1 = crsr2.fetchall()
    for row in results1:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

def earth() :
    crsr2.execute("SELECT * FROM planet where name = 'Earth'")
    results2 = crsr2.fetchall()
    for row in results2:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

def venus():
    crsr2.execute("SELECT * FROM planet where name = 'Venus'")
    results3 = crsr2.fetchall()
    for row in results3:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

def mars():
    crsr2.execute("SELECT * FROM planet where name = 'Mars'")
    results4 = crsr2.fetchall()
    for row in results4:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

def jupiter():
    crsr2.execute("SELECT * FROM planet where name = 'Jupiter'")
    results3 = crsr2.fetchall()
    for row in results3:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

def saturn():
    crsr2.execute("SELECT * FROM planet where name = 'Saturn'")
    results3 = crsr2.fetchall()
    for row in results3:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break
def uranus():
    crsr2.execute("SELECT * FROM planet where name = 'Uranus'")
    results3 = crsr2.fetchall()
    for row in results3:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

def neptune():
    crsr2.execute("SELECT * FROM planet where name = 'Neptune'")
    results3 = crsr2.fetchall()
    for row in results3:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

def pluto():
    crsr2.execute("SELECT * FROM planet where name = 'Pluto'")
    results3 = crsr2.fetchall()
    for row in results3:
        print("\nName:", row[0], "\nDiameter:", row[1], "\nMass:", row[2], "\nDensity:", row[3], "\nMean Orbital Velocity:", row[4], "\nSiderial Period:", row[5], "\nRotation Period:", row[6], "\nOrbital Eccentricity:", row[7], "\nDistance from Sun:", row[8], "\nNumber of moons:", row[9])
        break

planet_list = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
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
button_search_event_date = Button(root, text="Search by date", command=search_event_date).grid(row=14, column=0)

# Information for the user input
displayContext = Label(root, text = "Format as YYYY-MM-DD").grid(row=10, column=0)

# buttons for displaying planet info
button_Mercury = Button(root, text="Mercury", command=mercury).grid(row=16, column=0)
button_Venus = Button(root, text="Venus", command=venus).grid(row=16, column=1)
button_Earth = Button(root, text="Earth", command=earth).grid(row=17, column=0)
button_Mars = Button(root, text="Mars", command=mars).grid(row=17, column=1)
button_Jupiter = Button(root, text="Jupiter", command=jupiter).grid(row=18, column=0)
button_Saturn = Button(root, text="Saturn", command=saturn).grid(row=18, column=1)
button_Uranus = Button(root, text="Uranus", command=uranus).grid(row=19, column=0)
button_Neptune = Button(root, text="Neptune", command=neptune).grid(row=19, column=1)
button_Pluto = Button(root, text="Pluto", command=pluto).grid(row=20, column=0)
# keep the gui open until closed

mainloop()
