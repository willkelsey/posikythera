import datetime as d
import planentpos
import sqlite3


connection = sqlite3.connect('event.db')
crsr = connection.cursor()


class event(object):
    def __init__(self, tp, dt, tm):
        self.type = tp
        self.date = dt
        self.time = tm

    def solarSystem(self):
        T = planentpos.calc_date(self.date.year, self.date.month, self.date.day, self.time.hour, self.time.minute, self.time.second)
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
        Earth = planentpos.planet(-0.00054346, -0.01337178, 1.00000018, -0.00000003, -5.11260389, -0.24212385, 0.01673163,
                                  -0.00003661, 100.46691572, 35999.37306329, 102.93005885, 0.31795260, 365.2, 0.9857, 'Earth')
        Earth.x, Earth.y, Earth.z = Earth.calc_pos(Earth.i, Earth.icy, Earth.a, Earth.acy, Earth.an, Earth.ancy,
                                                   Earth.e, Earth.ecy, Earth.l, Earth.lcy, Earth.w, Earth.wcy,
                                                   self.solarSystem())
        Moon = planentpos.satellite(5.16, 0, 0.00256956, 0, 125.08000, -0.00000004, 0.0554, 0, 0, 0, 0, 0)
        Moon.x, Moon.y, Moon.z = Moon.calc_Moonpos(Moon.i, Moon.icy, Moon.a, Moon.acy, Moon.an, Moon.ancy, Moon.e,
                                                   Moon.ecy, Moon.l, Moon.lcy, Moon.w, Moon.wcy, self.solarSystem())
        Sun_x, Sun_y, Sun_z = 0

        if self.type == "solar eclipse":

            return 0

        elif self.type == "lunar eclipse":

            return 1


class alignment(event):
    def __init__(self, tp, dt, tm):
        event.__init__(self, tp, dt, tm)


def events():
    crsr.execute("SELECT * FROM event WHERE type='solar eclipse'")
    solar_eclipse = crsr.fetchall()
    crsr.execute("SELECT * FROM event WHERE type='lunar eclipse'")
    lunar_eclipse = crsr.fetchall()
    for i in solar_eclipse:
        print(i)
    for j in lunar_eclipse:
        print(j)


def search_event():
    events()
