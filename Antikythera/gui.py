from tkinter import *
from Antikythera import planentpos as p
from Antikythera import hohman
from Antikythera import event
from Antikythera.simulation import simulate
import sqlite3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


root = Tk()
connection = sqlite3.connect('events.db')
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
content_event_date = StringVar()
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

entry_hohmann_origin = Entry(root, textvariable=content_hohmann_origin).grid(row=4, column=1)
text = content_hohmann_origin.get()
content_hohmann_origin.set(text)

entry_hohmann_destination = Entry(root, textvariable=content_hohmann_destination).grid(row=5, column=1)
text = content_hohmann_destination.get()
content_hohmann_destination.set(text)

entry_event_event = Entry(root, textvariable=content_event_event).grid(row=8, column=1)
text = content_event_event.get()
content_event_event.set(text)

entry_event_date = Entry(root, textvariable=content_event_date).grid(row=8, column=0)

planet_info_label = Label(root, text=" Click on a planet to display that planet's information").grid(row=10)

#callback functions for buttons
def go_to_time():
    y = content_year.get()
    m = content_month.get()
    d = content_day.get()
    y = int(y, 10)
    m = int(m, 10)
    d = int(d, 10)
    print("going to: ")
    print(y, m, d)
    T = p.calc_date(y, m, d, 12, 0, 0)

    xcoords, ycoords, zcoords = simulate(T)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xcoords, ycoords, zcoords, cmap='jet')

    ax.set_xlim3d([-40, 40])
    ax.set_xlabel('X')

    ax.set_ylim3d([-40, 40])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-40, 40])
    ax.set_zlabel('Z')

    ax.set_title('Antikythera')
    planets = ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    for i, word in enumerate(planets):
        ax.text(xcoords[i], ycoords[i], zcoords[i], word)
    plt.show()


def execute_hohmann():
    o = content_hohmann_origin.get()
    d = content_hohmann_destination.get()
    hohmann.hohmann(o, d)


def search_event_event():
    s = content_event_event.get()
    crsr.execute("SELECT * FROM event WHERE type=?", (s,))
    results = crsr.fetchall()
    for i in results:
        print(i)


def search_event_date():
    s = content_event_date.get()

    print("Searching by date " + s)

def display_planet_info() :
    # p  = display_planet_info.get()
    print("Displaying planet info...")


# buttons
button_go_to_time = Button(root, text="Go To Time", command=go_to_time).grid(row=3, column=1)
button_hohmann = Button(root, text="Calculate travel window", command=execute_hohmann).grid(row=6, column=1)
button_search_event_event = Button(root, text="Search by event", command=search_event_event).grid(row=9, column=1)
button_search_event_date = Button(root, text="Search by date", command=search_event_date).grid(row=9, column=0)



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
main
