import datetime as d
from Antikythera import planentpos as p
import sqlite3


connection = sqlite3.connect('events.db')
crsr = connection.cursor()


# test if our solar system aligns when there is a known event
# send date and time of eclipse and check if the position is right
def validation(T, type):
    aligned = False

    Earth = planentpos.planet(-0.00054346, -0.01337178, 1.00000018, -0.00000003, -5.11260389, -0.24212385, 0.01673163,
                                -0.00003661, 100.46691572, 35999.37306329, 102.93005885, 0.31795260, 365.2, 0.9857, 'Earth')
    Earth.x, Earth.y, Earth.z = Earth.calc_pos(Earth.i, Earth.icy, Earth.a, Earth.acy, Earth.an, Earth.ancy,
                                                Earth.e, Earth.ecy, Earth.l, Earth.lcy, Earth.w, Earth.wcy,
                                                T)
    Moon = planentpos.satellite(5.16, 0, 0.00256956, 0, 125.08000, -0.00000004, 0.0554, 0, 0, 0, 0, 0)
    Moon.x, Moon.y, Moon.z = Moon.calc_Moonpos(Moon.i, Moon.icy, Moon.a, Moon.acy, Moon.an, Moon.ancy, Moon.e,
                                                Moon.ecy, Moon.l, Moon.lcy, Moon.w, Moon.wcy, T)

    if type == "solar eclipse":
        # find the line between sun and earth and check if the moon is on that line
        solarSlope = Earth.y/Earth.x
        if (Moon.y - (solarSlope * Moon.x))/(solarSlope * Moon.x) < 0.01:
            aligned = True

    elif type == "lunar eclipse":
        # find the line between sun and moon and check if the earth is on that line
        lunarSlope = Moon.y/Moon.x
        if (Earth.y - (lunarSlope * Earth.x))/ (lunarSlope * Earth.x) < 0.01:
            aligned = True
        
    return aligned


def search_event():
    choice = input("Select 1 to search by date, 2 to search by type, 3 to go back\n")
    while 1:
        if choice == "1":
            print("Enter a range of dates you would like to search for an event. (yyyy-mm-dd)")
            date1 = input("From: ")
            start = datetime.datetime.strptime(date1, "%Y-%m-%d")
            date2 = input("To: ")
            end = datetime.datetime.strptime(date2, "%Y-%m-%d")
            crsr.execute("SELECT * FROM event WHERE date BETWEEN ? AND ?", (start, end))
            results = crsr.fetchall()
            for i in results:
                print(i)
            break
        elif choice == "2":
            type = input("Enter a type of event you would like to search for: ")
            crsr.execute("SELECT * FROM event WHERE type=?", (type,))
            results = crsr.fetchall()
            print(len(results))
            for i in results:
                print(i)
            break
        break
