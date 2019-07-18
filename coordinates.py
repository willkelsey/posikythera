import sqlite3
from Antikythera import simulation, planentpos
import datetime

connection = sqlite3.connect('coordinate.db')
crsr = connection.cursor()


def coordinates(year, month, day):
    planets = ["Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    date = datetime.date(year, month, day).isoformat()
    crsr.execute("SELECT * FROM coordinate WHERE date = ?", (date,))
    test = crsr.fetchall()

    if len(test) == 0:
        T = planentpos.calc_date(year, month, day, 12, 0, 0)
        x, y, z = simulation.simulate(T)
        for i in range(len(planets)):
            crsr.execute("INSERT INTO coordinate VALUES(?, ?, ?, ?, ?)", (date, planets[i], x[i], y[i], z[i]))

    xcoords, ycoords, zcoords = [], [], []
    for i in range(len(planets)):
        crsr.execute("SELECT x_coordinate FROM coordinate WHERE date = ? and planet = ?", (date, planets[i]))
        xcoords.append(crsr.fetchone())
        crsr.execute("SELECT y_coordinate FROM coordinate WHERE date = ? and planet = ?", (date, planets[i]))
        ycoords.append(crsr.fetchone())
        crsr.execute("SELECT z_coordinate FROM coordinate WHERE date = ? and planet = ?", (date, planets[i]))
        zcoords.append(crsr.fetchone())

    return xcoords, ycoords, zcoords
