from Antikythera import planentpos as p


def simulate(t):
    T = t
# planet orbital elements and calculating the position based on T
    p.Mercury.x, p.Mercury.y, p.Mercury.z = p.Mercury.calc_pos(p.Mercury.i, p.Mercury.icy, p.Mercury.a, p.Mercury.acy, p.Mercury.an, p.Mercury.ancy, p.Mercury.e, p.Mercury.ecy, p.Mercury.l, p.Mercury.lcy, p.Mercury.w, p.Mercury.wcy, T)
    p.Venus.x, p.Venus.y, p.Venus.z = p.Venus.calc_pos(p.Venus.i, p.Venus.icy, p.Venus.a, p.Venus.acy, p.Venus.an, p.Venus.ancy, p.Venus.e, p.Venus.ecy, p.Venus.l, p.Venus.lcy, p.Venus.w, p.Venus.wcy, T)
    p.Earth.x, p.Earth.y, p.Earth.z = p.Earth.calc_pos(p.Earth.i, p.Earth.icy, p.Earth.a, p.Earth.acy, p.Earth.an, p.Earth.ancy, p.Earth.e, p.Earth.ecy, p.Earth.l, p.Earth.lcy, p.Earth.w, p.Earth.wcy, T)
    p.Mars.x, p.Mars.y, p.Mars.z = p.Mars.calc_pos(p.Mars.i, p.Mars.icy, p.Mars.a, p.Mars.acy, p.Mars.an, p.Mars.ancy, p.Mars.e, p.Mars.ecy, p.Mars.l, p.Mars.lcy, p.Mars.w, p.Mars.wcy, T)
    p.Jupiter.x, p.Jupiter.y, p.Jupiter.z = p.Jupiter.calc_pos(p.Jupiter.i, p.Jupiter.icy, p.Jupiter.a, p.Jupiter.acy, p.Jupiter.an, p.Jupiter.ancy, p.Jupiter.e, p.Jupiter.ecy, p.Jupiter.l, p.Jupiter.lcy, p.Jupiter.w, p.Jupiter.wcy, T)
    p.Saturn.x, p.Saturn.y, p.Saturn.z = p.Saturn.calc_pos(p.Saturn.i, p.Saturn.icy, p.Saturn.a, p.Saturn.acy, p.Saturn.an, p.Saturn.ancy, p.Saturn.e, p.Saturn.ecy, p.Saturn.l, p.Saturn.lcy, p.Saturn.w, p.Saturn.wcy, T)
    p.Uranus.x, p.Uranus.y, p.Uranus.z = p.Uranus.calc_pos(p.Uranus.i, p.Uranus.icy, p.Uranus.a, p.Uranus.acy, p.Uranus.an, p.Uranus.ancy, p.Uranus.e, p.Uranus.ecy, p.Uranus.l, p.Uranus.lcy, p.Uranus.w, p.Uranus.wcy, T)
    p.Neptune.x, p.Neptune.y, p.Neptune.z = p.Neptune.calc_pos(p.Neptune.i, p.Neptune.icy, p.Neptune.a, p.Neptune.acy, p.Neptune.an, p.Neptune.ancy, p.Neptune.e, p.Neptune.ecy, p.Neptune.l, p.Neptune.lcy, p.Neptune.w, p.Neptune.wcy, T)
    p.Pluto.x, p.Pluto.y, p.Pluto.z = p.Pluto.calc_pos(p.Pluto.i, p.Pluto.icy, p.Pluto.a, p.Pluto.acy, p.Pluto.an, p.Pluto.ancy, p.Pluto.e, p.Pluto.ecy, p.Pluto.l, p.Pluto.lcy, p.Pluto.w, p.Pluto.wcy, T)
    p.Moon.x, p.Moon.y, p.Moon.z = p.Moon.calc_Moonpos(p.Moon.i, p.Moon.icy, p.Moon.a, p.Moon.acy, p.Moon.an, p.Moon.ancy, p.Moon.e, p.Moon.ecy, p.Moon.l, p.Moon.lcy, p.Moon.w, p.Moon.wcy, T)
    p.Moon.x = p.Moon.x + p.Earth.x
    p.Moon.y = p.Moon.y + p.Earth.y
    p.Moon.z = p.Moon.z + p.Earth.z
    xcoords = [0, p.Mercury.x, p.Venus.x, p.Earth.x, p.Moon.x, p.Mars.x, p.Jupiter.x, p.Saturn.x, p.Uranus.x, p.Neptune.x, p.Pluto.x]
    ycoords = [0, p.Mercury.y, p.Venus.y, p.Earth.y, p.Moon.y, p.Mars.y, p.Jupiter.y, p.Saturn.y, p.Uranus.y, p.Neptune.y, p.Pluto.y]
    zcoords = [0, p.Mercury.z, p.Venus.z, p.Earth.z, p.Moon.z, p.Mars.z, p.Jupiter.z, p.Saturn.z, p.Uranus.z, p.Neptune.z, p.Pluto.z]
    return xcoords, ycoords, zcoords
