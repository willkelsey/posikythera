import sqlite3
import planentpos
import datetime

connection = sqlite3.connect('coordinate.db')
crsr = connection.cursor()


def coordinates(year, month, day):
    date = datetime.date(year, month, day).isoformat()
    crsr.execute("SELECT * FROM coordinate WHERE date = ?", (date,))
    results = crsr.fetchall()
    if len(results) == 0:
        T = planentpos.calc_date(year, month, day, 12, 0, 0)
        # planet orbital elements and calculating the position based on T
        Mercury = planentpos.planet(7.00559432, -0.00590158, 0.38709843, 0.000000, 48.33961819, -0.12214182, 0.20563661,0.00002123, 252.25166724, 149472.67486623, 77.45771895, 0.15940013, 88, 4.09, 'Mercury')
        Mercury.x, Mercury.y, Mercury.z = Mercury.calc_pos(Mercury.i, Mercury.icy, Mercury.a, Mercury.acy, Mercury.an,Mercury.ancy, Mercury.e, Mercury.ecy, Mercury.l, Mercury.lcy,Mercury.w, Mercury.wcy, T)
        Venus = planentpos.planet(3.397777545, 0.00043494, 0.72332102, -0.000000026, 76.67261496, -0.27274174, 0.00676399,-0.00005107, 181.9797085, 58517.81560260, 131.76755713, 0.05679648, 224.7, 1.602, 'Venus')
        Venus.x, Venus.y, Venus.z = Venus.calc_pos(Venus.i, Venus.icy, Venus.a, Venus.acy, Venus.an, Venus.ancy,Venus.e, Venus.ecy, Venus.l, Venus.lcy, Venus.w, Venus.wcy, T)
        Earth = planentpos.planet(-0.00054346, -0.01337178, 1.00000018, -0.00000003, -5.11260389, -0.24212385, 0.01673163,-0.00003661, 100.46691572, 35999.37306329, 102.93005885, 0.31795260, 365.2, 0.9857, 'Earth')
        Earth.x, Earth.y, Earth.z = Earth.calc_pos(Earth.i, Earth.icy, Earth.a, Earth.acy, Earth.an, Earth.ancy,Earth.e, Earth.ecy, Earth.l, Earth.lcy, Earth.w, Earth.wcy, T)
        Mars = planentpos.planet(1.85181869, -0.00724757, 1.52371243, 0.00000097, 49.71320984, -0.26852431, 0.09336511, 0.00009149,-4.56813164, 19149.29934243, -23.91744784, 0.45223625, 687, 0.524, 'Mars')
        Mars.x, Mars.y, Mars.z = Mars.calc_pos(Mars.i, Mars.icy, Mars.a, Mars.acy, Mars.an, Mars.ancy, Mars.e, Mars.ecy,Mars.l, Mars.lcy, Mars.w, Mars.wcy, T)
        Jupiter = planentpos.planet(1.29861416, -0.00322699, 5.20248019, -0.00002864, 100.29282654, 0.13024619, 0.04853590,0.00018026, 34.33479152, 3034.90371757, 14.27495244, 0.18199196, 4331, 0.08312, 'Jupiter')
        Jupiter.x, Jupiter.y, Jupiter.z = Jupiter.calc_pos(Jupiter.i, Jupiter.icy, Jupiter.a, Jupiter.acy, Jupiter.an,Jupiter.ancy, Jupiter.e, Jupiter.ecy, Jupiter.l, Jupiter.lcy,Jupiter.w, Jupiter.wcy, T)
        Saturn = planentpos.planet(2.49424102, 0.00451969, 9.54149883, -0.00003065, 113.63998702, -0.25015002, 0.05550825,-0.00032044, 50.07571329, 1222.11494724, 92.86136063, 0.54179478, 10747, 0.03349, 'Saturn')
        Saturn.x, Saturn.y, Saturn.z = Saturn.calc_pos(Saturn.i, Saturn.icy, Saturn.a, Saturn.acy, Saturn.an,Saturn.ancy, Saturn.e, Saturn.ecy, Saturn.l, Saturn.lcy,Saturn.w, Saturn.wcy, T)
        Uranus = planentpos.planet(0.77298127, -0.00180155, 19.18797948, -0.00020455, 73.96250215, 0.05739699, 0.04685740,-0.00001550, 314.20276625, 428.49512595, 172.43404441, 0.09266985, 30589, 0.01176, 'Uranus')
        Uranus.x, Uranus.y, Uranus.z = Uranus.calc_pos(Uranus.i, Uranus.icy, Uranus.a, Uranus.acy, Uranus.an,Uranus.ancy, Uranus.e, Uranus.ecy, Uranus.l, Uranus.lcy,Uranus.w, Uranus.wcy, T)
        Neptune = planentpos.planet(1.77005520, 0.00022400, 30.06952752, 0.00006447, 131.78635853, -0.00606302, 0.00895439,0.00000818, 304.22289287, 218.46515314, 46.68158724, 0.01009938, 59800, 0.00602, 'Neptune')
        Neptune.x, Neptune.y, Neptune.z = Neptune.calc_pos(Neptune.i, Neptune.icy, Neptune.a, Neptune.acy, Neptune.an,Neptune.ancy, Neptune.e, Neptune.ecy, Neptune.l, Neptune.lcy,Neptune.w, Neptune.wcy, T)
        Pluto = planentpos.planet(17.14104260, 0.00000501, 39.48686035, 0.00449751, 110.30167986, -0.00809981, 0.24885238,0.00006016, 238.96535011, 145.18042903, 224.09702598, -0.00968827, 90560, 0.003975, 'Pluto')
        Pluto.x, Pluto.y, Pluto.z = Pluto.calc_pos(Pluto.i, Pluto.icy, Pluto.a, Pluto.acy, Pluto.an, Pluto.ancy,Pluto.e, Pluto.ecy, Pluto.l, Pluto.lcy, Pluto.w, Pluto.wcy, T)
        Moon = planentpos.satellite(5.16, 0, 0.00256956, 0, 125.08000, -0.00000004, 0.0554, 0, 0, 0, 0, 0)
        Moon.x, Moon.y, Moon.z = Moon.calc_Moonpos(Moon.i, Moon.icy, Moon.a, Moon.acy, Moon.an, Moon.ancy, Moon.e,Moon.ecy, Moon.l, Moon.lcy, Moon.w, Moon.wcy, T)
        planets = ["Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
        xcoords = [Mercury.x, Venus.x, Earth.x, Moon.x, Mars.x, Jupiter.x, Saturn.x, Uranus.x, Neptune.x, Pluto.x]
        ycoords = [Mercury.y, Venus.y, Earth.y, Moon.y, Mars.y, Jupiter.y, Saturn.y, Uranus.y, Neptune.y, Pluto.y]
        zcoords = [Mercury.z, Venus.z, Earth.z, Moon.z, Mars.z, Jupiter.z, Saturn.z, Uranus.z, Neptune.z, Pluto.z]

        for i in range(len(planets)):
            crsr.execute("INSERT INTO coordinate VALUES(?, ?, ?, ?, ?)", (date, planets[i], xcoords[i], ycoords[i], zcoords[i]))

