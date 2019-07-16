import datetime as d
from Antikythera import planentpos as p
import sqlite3


connection = sqlite3.connect('events.db')
crsr = connection.cursor()


class event(object):
    def __init__(self, tp, dt, tm):
        self.type = tp
        self.date = dt
        self.time = tm

    def solarSystem(self):
        T = p.calc_date(self.date.year, self.date.month, self.date.day, self.time.hour, self.time.minute, self.time.second)
        return T


class eclipse(event):
    def __init__(self, tp, dt, tm, mag, dur, georeg):
        self.magnitude = mag
        self.duration = dur
        self.geoRegion = georeg
        event.__init__(self, tp, dt, tm)

    def printAll(self):
        print(self.type, self.date, self.time, self.magnitude, self.duration, self.geoRegion)

    # test if our solar system aligns when there is a known event
    # send date and time of eclipse and check if the position is right
    def validation(self):
        aligned = False

        Earth = p.planet(-0.00054346, -0.01337178, 1.00000018, -0.00000003, -5.11260389, -0.24212385, 0.01673163, -0.00003661, 100.46691572, 35999.37306329, 102.93005885, 0.31795260, 365.2, 0.9857, 'Earth')
        Earth.x, Earth.y, Earth.z = Earth.calc_pos(Earth.i, Earth.icy, Earth.a, Earth.acy, Earth.an, Earth.ancy, Earth.e, Earth.ecy, Earth.l, Earth.lcy, Earth.w, Earth.wcy, self.solarSystem())
        Moon = p.satellite(5.16, 0, 0.00256956, 0, 125.08000, -0.00000004, 0.0554, 0, 0, 0, 0, 0)
        Moon.x, Moon.y, Moon.z = Moon.calc_Moonpos(Moon.i, Moon.icy, Moon.a, Moon.acy, Moon.an, Moon.ancy, Moon.e, Moon.ecy, Moon.l, Moon.lcy, Moon.w, Moon.wcy, self.solarSystem())
        Moon.x = Moon.x + Earth.x
        Moon.y = Moon.y + Earth.y
        Moon.z = Moon.z + Earth.z
        if self.type == "solar eclipse":
            # find the line between sun and earth and check if the moon is on that line
            solarSlope = Earth.y/Earth.x
            if Moon.y == solarSlope * Moon.x:
                aligned = True

        elif self.type == "lunar eclipse":
            # find the line between sun and moon and check if the earth is on that line
            lunarSlope = Moon.y/Moon.x
            if Earth.y == lunarSlope * Earth.x:
                aligned = True
        
        return aligned


class alignment(event):
    def __init__(self, tp, dt, tm):
        event.__init__(self, tp, dt, tm)


def search_event():
    choice = input("Select 1 to search by date, 2 to search by type, 3 to go back\n")
    while 1:
        if choice == "1":
            print("Enter a range of dates you would like to search for an event. (yyyy-mm-dd)")
            date1 = input("From: ")
            start = d.datetime.strptime(date1, "%Y-%m-%d")
            date2 = input("To: ")
            end = d.datetime.strptime(date2, "%Y-%m-%d")
            crsr.execute("SELECT * FROM event WHERE date BETWEEN ? AND ?", (start, end))
            results = crsr.fetchall()
            for i in results:
                print(i)
            break
        elif choice == "2":
            type = input("Enter a type of event you would like to search for: ")
            crsr.execute("SELECT * FROM event WHERE type=?", (type,))
            results = crsr.fetchall()
            for i in results:
                print(i)
            break
        break
