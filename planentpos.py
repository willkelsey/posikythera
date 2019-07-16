import math
import datetime
import matplotlib.pyplot as plt
from Antikythera import event
from Antikythera import hohmann
from Antikythera import simulation
from mpl_toolkits.mplot3d import Axes3D


class planet:
    # heliocentric coordinates
    x = 0
    y = 0
    z = 0

    def __init__(self, i, icy, a, acy, an, ancy, e, ecy, l, lcy, w, wcy,p,pdd,n):
        # inclination
        self.i = i
        self.icy = icy
        # semi major axis
        self.a = a
        self.acy = acy
        # longitude of ascending node
        self.an = an
        self.ancy = ancy
        # eccentricity
        self.e = e
        self.ecy = ecy
        # mean longitude
        self.l = l
        self.lcy = lcy
        # arguement of perihelion
        self.w = w
        self.wcy = wcy
        #orbital period
        self.period = p
        #orbital degree change per day
        self.degreeperiod = pdd
        self.name = n

    def calc_pos(self, i, icy, a, acy, an, ancy, e, ecy, l, lcy, w, wcy, T):
        # Orbital element values based on input date
        aa = a + acy * T
        ee = e + ecy * T
        ii = i + icy * T
        ll = l + lcy * T
        ww = w + wcy * T
        ann = an + ancy * T
        # calculate argument of perihelion
        w1 = ww - ann
        # calculate mean anomaly
        M = ll - ww
        if math.fmod(M,360) > 180:
            Mm = math.fmod(M,360) - 360
        else:
            Mm = math.fmod(M,360)
        estar = ee*(180/math.pi)
        # have to do these a couple times
        #calculating the eccentric anomaly
        e0 = Mm + estar * math.sin(Mm*(math.pi/180))
        dm0 = M - e0 + estar * math.sin(e0*math.pi/180)
        de0 = dm0/(1-ee * math.cos(e0*math.pi/180))
        e1 = e0 + de0
        dm1 = M - e1 + estar * math.sin(e1*math.pi/180)
        de1 = dm1 / (1 - ee * math.cos(e1 * math.pi / 180))
        e2 = e1 + de1
        dm2 = M - e2 + estar * math.sin(e2 * math.pi / 180)
        de2 = dm2 / (1 - ee * math.cos(e2 * math.pi / 180))
        e3 = e2 + de2
        dm3 = M - e3 + estar * math.sin(e3 * math.pi / 180)
        de3 = dm3 / (1 - ee * math.cos(e3 * math.pi / 180))
        e4 = e3 + de3
        dm4 = M - e4 + estar * math.sin(e4*math.pi/180)
        de4 = dm4 / (1 - ee * math.cos(e4 * math.pi / 180))
        e5 = e4 + de4
        dm5 = M - e5 + estar * math.sin(e5 * math.pi / 180)
        de5 = dm5 / (1 - ee * math.cos(e5 * math.pi / 180))
        e6 = e5 + de5
        dm6 = M - e6 + estar * math.sin(e6 * math.pi / 180)
        de6 = dm6 / (1 - ee * math.cos(e6 * math.pi / 180))

        #preliminary x,y,z coords use to calculate heliocentric coords
        xb = aa * (math.cos(e6 * math.pi/180)-ee)
        yb = aa * math.sqrt(1 - ee * ee) * math.sin(e6 * math.pi/180)
        zb = 0.0
        #calculation of the heliocentric coordinates
        x = (math.cos(w1 * math.pi / 180) * math.cos(ann * math.pi / 180) - math.sin(w1 * math.pi / 180) * math.sin(ann * math.pi / 180) * math.cos(ii * math.pi / 180)) * xb + (-math.sin(w1 * math.pi / 180) * math.cos(ann * math.pi / 180) - math.cos(w1 * math.pi / 180) * math.sin(ann * math.pi / 180) * math.cos(ii * math.pi / 180)) * yb
        y = (math.cos(w1*math.pi/180)*math.sin(ann*math.pi/180)+math.sin(w1*math.pi/180)*math.cos(ann*math.pi/180)*math.cos(ii*math.pi/180))*xb+(-math.sin(w1*math.pi/180)*math.sin(ann*math.pi/180)+math.cos(w1*math.pi/180)*math.cos(ann*math.pi/180)*math.cos(ii*math.pi/180))*yb
        z = (math.sin(w1*math.pi/180)*math.sin(ii*math.pi/180))*xb+(math.cos(w1*math.pi/180)*math.sin(ii*math.pi/180))*yb
        return x,y,z

class satellite(planet):
    # heliocentric coordinates
    x = 0
    y = 0
    z = 0

    def __init__(self, i, icy, a, acy, an, ancy, e, ecy, l, lcy, w, wcy):
        # inclination
        self.i = i
        self.icy = icy
        # semi major axis
        self.a = a
        self.acy = acy
        # longitude of ascending node
        self.an = an
        self.ancy = ancy
        # eccentricity
        self.e = e
        self.ecy = ecy
        # mean longitude
        self.l = l
        self.lcy = lcy
        # arguement of perihelion
        self.w = w
        self.wcy = wcy

    def calc_Moonpos(self, i, icy, a, acy, an, ancy, e, ecy, l, lcy, w, wcy, T):
        # Orbital element values based on input date
        aa = a + acy * T
        ee = e + ecy * T
        ii = i + icy * T
        ll = l + lcy * T
        ww = w + wcy * T
        ann = an + ancy * T
        # calculate argument of perihelion
        w1 = 318.15+(360/999999999999 * 100)*T
        # calculate mean anomaly
        M = 93565.26993900
        if math.fmod(M,360) > 180:
            Mm = math.fmod(M,360) - 360
        else:
            Mm = math.fmod(M,360)
        estar = ee*(180/math.pi)
        # have to do these a couple times
        #calculating the eccentric anomaly
        e0 = Mm + estar * math.sin(Mm*(math.pi/180))
        dm0 = M - e0 + estar * math.sin(e0*math.pi/180)
        de0 = dm0/(1-ee * math.cos(e0*math.pi/180))
        e1 = e0 + de0
        dm1 = M - e1 + estar * math.sin(e1*math.pi/180)
        de1 = dm1 / (1 - ee * math.cos(e1 * math.pi / 180))
        e2 = e1 + de1
        dm2 = M - e2 + estar * math.sin(e2 * math.pi / 180)
        de2 = dm2 / (1 - ee * math.cos(e2 * math.pi / 180))
        e3 = e2 + de2
        dm3 = M - e3 + estar * math.sin(e3 * math.pi / 180)
        de3 = dm3 / (1 - ee * math.cos(e3 * math.pi / 180))
        e4 = e3 + de3
        dm4 = M - e4 + estar * math.sin(e4*math.pi/180)
        de4 = dm4 / (1 - ee * math.cos(e4 * math.pi / 180))
        e5 = e4 + de4
        dm5 = M - e5 + estar * math.sin(e5 * math.pi / 180)
        de5 = dm5 / (1 - ee * math.cos(e5 * math.pi / 180))
        e6 = e5 + de5
        dm6 = M - e6 + estar * math.sin(e6 * math.pi / 180)
        de6 = dm6 / (1 - ee * math.cos(e6 * math.pi / 180))

        #preliminary x,y,z coords use to calculate heliocentric coords
        xb = aa * (math.cos(e6 * math.pi/180)-ee)
        yb = aa * math.sqrt(1 - ee * ee) * math.sin(e6 * math.pi/180)
        zb = 0.0
        #calculation of the heliocentric coordinates
        x = (math.cos(w1 * math.pi / 180) * math.cos(ann * math.pi / 180) - math.sin(w1 * math.pi / 180) * math.sin(ann * math.pi / 180) * math.cos(ii * math.pi / 180)) * xb + (-math.sin(w1 * math.pi / 180) * math.cos(ann * math.pi / 180) - math.cos(w1 * math.pi / 180) * math.sin(ann * math.pi / 180) * math.cos(ii * math.pi / 180)) * yb
        y = (math.cos(w1*math.pi/180)*math.sin(ann*math.pi/180)+math.sin(w1*math.pi/180)*math.cos(ann*math.pi/180)*math.cos(ii*math.pi/180))*xb+(-math.sin(w1*math.pi/180)*math.sin(ann*math.pi/180)+math.cos(w1*math.pi/180)*math.cos(ann*math.pi/180)*math.cos(ii*math.pi/180))*yb
        z = (math.sin(w1*math.pi/180)*math.sin(ii*math.pi/180))*xb+(math.cos(w1*math.pi/180)*math.sin(ii*math.pi/180))*yb
        return x,y,z


def calc_date(year, month, day, hour, minute, second):
    # J2000 Reference date 1/1/2000
    ref = datetime.datetime(2000, 1, 1, 12, 0, 0)
    date = datetime.datetime(year, month, day, hour, minute, second)
    days_elapsed = date - ref
    dec_days_elapsed = days_elapsed.days + (hour / 24 + minute / 60 / 24 + second / 60 / 60 / 24) - (12 / 24 + 0 / 60 / 24 + 0 / 60 / 60 / 24)
    return dec_days_elapsed / 36525


Mercury = planet(7.00559432, -0.00590158, 0.38709843, 0.000000, 48.33961819, -0.12214182, 0.20563661,0.00002123, 252.25166724, 149472.67486623, 77.45771895, 0.15940013, 88, 4.09, 'Mercury')
Venus = planet(3.397777545, 0.00043494, 0.72332102, -0.000000026, 76.67261496, -0.27274174, 0.00676399, -0.00005107, 181.9797085, 58517.81560260, 131.76755713, 0.05679648, 224.7, 1.602, 'Venus')
Earth = planet(-0.00054346, -0.01337178, 1.00000018, -0.00000003, -5.11260389, -0.24212385, 0.01673163, -0.00003661, 100.46691572, 35999.37306329, 102.93005885, 0.31795260, 365.2, 0.9857, 'Earth')
Mars = planet(1.85181869, -0.00724757, 1.52371243, 0.00000097, 49.71320984, -0.26852431, 0.09336511, 0.00009149, -4.56813164, 19149.29934243, -23.91744784, 0.45223625, 687, 0.524, 'Mars')
Jupiter = planet(1.29861416, -0.00322699, 5.20248019, -0.00002864, 100.29282654, 0.13024619, 0.04853590, 0.00018026, 34.33479152, 3034.90371757, 14.27495244, 0.18199196, 4331, 0.08312, 'Jupiter')
Saturn = planet(2.49424102, 0.00451969, 9.54149883, -0.00003065, 113.63998702, -0.25015002, 0.05550825, -0.00032044, 50.07571329, 1222.11494724, 92.86136063, 0.54179478, 10747, 0.03349, 'Saturn')
Uranus = planet(0.77298127, -0.00180155, 19.18797948, -0.00020455, 73.96250215, 0.05739699, 0.04685740, -0.00001550, 314.20276625, 428.49512595, 172.43404441, 0.09266985, 30589, 0.01176, 'Uranus')
Neptune = planet(1.77005520, 0.00022400, 30.06952752, 0.00006447, 131.78635853, -0.00606302, 0.00895439, 0.00000818, 304.22289287, 218.46515314, 46.68158724, 0.01009938, 59800, 0.00602, 'Neptune')
Pluto = planet(17.14104260, 0.00000501, 39.48686035, 0.00449751, 110.30167986, -0.00809981, 0.24885238, 0.00006016, 238.96535011, 145.18042903, 224.09702598, -0.00968827, 90560, 0.003975, 'Pluto')
Moon = satellite(5.16, 0, 0.00256956, 0, 125.08000, -0.00000004, 0.0554, 0, 0, 0, 0, 0)
Sun = planet(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Sun')
list = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]
T = calc_date(1983, 11, 17, 12, 0, 0)
x, y, z = simulation.simulate(T)
while 1:
    print("Welcome to Antikythera Simulation main menu")
    c = input("Press 1 to view the entire system, 2 to search for an astronomical event, "
              "3 for best travel window and 0 to exit\n")
    # typecast to int of base 10
    choice = int(c, 10)
    if choice == 1:
        year = input("Type the year to see\n")
        year = int(year, 10)
        month = input("Type the month\n")
        month = int(month, 10)
        day = input("Type the day\n")
        day = int(day, 10)
        T = calc_date(year, month, day, 12, 0, 0)
        x, y, z = simulation.simulate(T)


        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, cmap='jet')

        ax.set_xlim3d([-40, 40])
        ax.set_xlabel('X')

        ax.set_ylim3d([-40, 40])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-40, 40])
        ax.set_zlabel('Z')

        ax.set_title('Antikythera')
        planets =['Sun','Mercury','Venus','Earth','Moon','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
        for i, word in enumerate(planets):
            ax.text(x[i], y[i], z[i],word)
        plt.show()
    elif choice == 0:
        break
    elif choice == 2:
        event.search_event()
    elif choice == 3:
        orig = input('Origin: \n')
        dest = input('Destination: \n')
        hohmann.hohmann(orig, dest)
    else:
        print("Invalid input")