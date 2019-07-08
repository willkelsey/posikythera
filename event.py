import datetime as d


def search_event():
    print("Searching by event")


class event(object):
  def __init__(self, tp, dt, tm):
    self.type = tp
    self.date = dt
    self.time = tm

# test if our solar system aligns when there is a known event
# send date and time of eclipse and check if the position is right
# T = calc_date(x.dt.year, x.dt.month, x.dt.day, x.tm.hour, x.tm.minute, x.tm.second)
  def validation(self):
    v = True

class eclipse(event):
  def __init__(self, tp, dt, tm, mag, dur, georeg):
    self.magnitude = mag
    self.duration = dur
    self.geoRegion = georeg
    event.__init__(self, tp, dt, tm)

  def printAll(self):
    print(self.type, self.date, self.time,self.magnitude,self.duration, self.geoRegion)

solar_eclipse = [
  eclipse("solar eclipse", d.date(2012,11,13), d.time(22,12,55), 1.05, d.time(0, 4,2), ["n Australia", "s Pacific"]),
  eclipse("solar eclipse", d.date(2015,3,20), d.time(9,46,47), 1.045, d.time(0,2,47), ["n Atlantic"])
]
lunar_eclipse = [
  eclipse("lunar eclipse", d.date(2011,6,15), d.time(20,13,43), 1.7, d.time(1,40), ["S.America", "Europe", "Africa", "Asia", "Aus."]),
  eclipse("lunar eclipse", d.date(2011,12,10), d.time(14,32,56), 1.106, d.time(0,51), ["Europe", "e Africa", "Asia", "Aus.", "Pacific", "N.A."])
]