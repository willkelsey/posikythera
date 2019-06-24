import math
import datetime
import matplotlib.pyplot as plt

class planet(object):
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


def calc_date(year, month, day, hour, minute, second):
    # J2000 Reference date 1/1/2000
    ref = datetime.datetime(2000, 1, 1, 12, 0, 0)
    date = datetime.datetime(year, month, day, hour, minute, second)
    print(date)
    days_elapsed = date - ref
    dec_days_elapsed = days_elapsed.days + (hour / 24 + minute / 60 / 24 + second / 60 / 60 / 24) - (12 / 24 + 0 / 60 / 24 + 0 / 60 / 60 / 24)
    return dec_days_elapsed / 36525

#change the values for T to alter the date of calculation
T = calc_date(2019, 6, 23, 12, 0, 0)



# planet orbital elements and calculating the position based on T
Mercury = planet(7.00559432, -0.00590158, 0.38709843, 0.000000, 48.33961819, -0.12214182, 0.20563661, 0.00002123,252.25166724, 149472.67486623, 77.45771895, 0.15940013)
Mercury.x, Mercury.y, Mercury.z = Mercury.calc_pos(Mercury.i, Mercury.icy, Mercury.a, Mercury.acy, Mercury.an, Mercury.ancy, Mercury.e, Mercury.ecy,Mercury.l, Mercury.lcy, Mercury.w, Mercury.wcy, T)
Venus = planet(3.397777545,0.00043494,0.72332102,-0.000000026,76.67261496,-0.27274174,0.00676399,-0.00005107,181.9797085,58517.81560260,131.76755713,0.05679648)
Venus.x, Venus.y, Venus.z = Venus.calc_pos(Venus.i, Venus.icy, Venus.a, Venus.acy, Venus.an, Venus.ancy, Venus.e, Venus.ecy, Venus.l, Venus.lcy, Venus.w, Venus.wcy, T)
Earth = planet(-0.00054346,-0.01337178,1.00000018,-0.00000003,-5.11260389,-0.24212385,0.01673163,-0.00003661,100.46691572,35999.37306329,102.93005885,0.31795260)
Earth.x, Earth.y, Earth.z = Earth.calc_pos(Earth.i, Earth.icy, Earth.a, Earth.acy, Earth.an, Earth.ancy, Earth.e, Earth.ecy, Earth.l, Earth.lcy, Earth.w, Earth.wcy, T)
Mars = planet(1.85181869,-0.00724757,1.52371243,0.00000097,49.71320984,-0.26852431,0.09336511,0.00009149,-4.56813164,19149.29934243,-23.91744784,0.45223625)
Mars.x, Mars.y, Mars.z = Mars.calc_pos(Mars.i, Mars.icy, Mars.a, Mars.acy, Mars.an, Mars.ancy, Mars.e, Mars.ecy, Mars.l, Mars.lcy, Mars.w, Mars.wcy, T)
Jupiter = planet(1.29861416,-0.00322699,5.20248019,-0.00002864,100.29282654,0.13024619,0.04853590,0.00018026,34.33479152,3034.90371757,14.27495244,0.18199196)
Jupiter.x, Jupiter.y, Jupiter.z = Jupiter.calc_pos(Jupiter.i, Jupiter.icy, Jupiter.a, Jupiter.acy, Jupiter.an, Jupiter.ancy, Jupiter.e, Jupiter.ecy, Jupiter.l, Jupiter.lcy, Jupiter.w, Jupiter.wcy, T)
Saturn = planet(2.49424102,0.00451969,9.54149883,-0.00003065,113.63998702,-0.25015002,0.05550825,-0.00032044,50.07571329,1222.11494724,92.86136063,0.54179478)
Saturn.x, Saturn.y, Saturn.z = Saturn.calc_pos(Saturn.i, Saturn.icy, Saturn.a, Saturn.acy, Saturn.an, Saturn.ancy, Saturn.e, Saturn.ecy, Saturn.l, Saturn.lcy, Saturn.w, Saturn.wcy, T)
Uranus = planet(0.77298127,-0.00180155,19.18797948,-0.00020455,73.96250215,0.05739699,0.04685740,-0.00001550,314.20276625,428.49512595,172.43404441,0.09266985)
Uranus.x, Uranus.y, Uranus.z = Uranus.calc_pos(Uranus.i, Uranus.icy, Uranus.a, Uranus.acy, Uranus.an, Uranus.ancy, Uranus.e, Uranus.ecy, Uranus.l, Uranus.lcy, Uranus.w, Uranus.wcy, T)
Neptune = planet(1.77005520,0.00022400,30.06952752,0.00006447,131.78635853,-0.00606302,0.00895439,0.00000818,304.22289287,218.46515314,46.68158724,0.01009938)
Neptune.x, Neptune.y, Neptune.z = Neptune.calc_pos(Neptune.i, Neptune.icy, Neptune.a, Neptune.acy, Neptune.an, Neptune.ancy, Neptune.e, Neptune.ecy, Neptune.l, Neptune.lcy, Neptune.w, Neptune.wcy, T)
Pluto = planet(17.14104260,0.00000501,39.48686035,0.00449751,110.30167986,-0.00809981,0.24885238,0.00006016,238.96535011,145.18042903,224.09702598,-0.00968827)
Pluto.x, Pluto.y, Pluto.z = Pluto.calc_pos(Pluto.i, Pluto.icy, Pluto.a, Pluto.acy, Pluto.an, Pluto.ancy, Pluto.e, Pluto.ecy, Pluto.l, Pluto.lcy, Pluto.w, Pluto.wcy, T)


xcoords = [0, Mercury.x, Venus.x, Earth.x, Mars.x, Jupiter.x, Saturn.x, Uranus.x, Neptune.x, Pluto.x]
ycoords = [0, Mercury.y, Venus.y, Earth.y, Mars.y, Jupiter.y, Saturn.y, Uranus.y, Neptune.y, Pluto.y]
zcoords = [0, Mercury.z, Venus.z, Earth.z, Mars.z, Jupiter.z, Saturn.z, Uranus.z, Neptune.z, Pluto.z]
print(xcoords)
print(ycoords)
print(zcoords)
plt.plot(xcoords, ycoords, 'o')
plt.xlim(-10, 30)
plt.ylim(-40, 20)
plt.show()
