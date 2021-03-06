import sqlite3
import simulation
import planentpos
import datetime


def coordinates(year, month, day):
    connection = sqlite3.connect("coordinate.db")
    crsr = connection.cursor()

    planets = ["Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
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
        x_result = crsr.fetchone()
        xcoords.append(x_result[0])
        crsr.execute("SELECT y_coordinate FROM coordinate WHERE date = ? and planet = ?", (date, planets[i]))
        y_result = crsr.fetchone()
        ycoords.append(y_result[0])
        crsr.execute("SELECT z_coordinate FROM coordinate WHERE date = ? and planet = ?", (date, planets[i]))
        z_result = crsr.fetchone()
        zcoords.append(z_result[0])

    connection.commit()
    connection.close()

    return xcoords, ycoords, zcoords
