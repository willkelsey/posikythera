from Antikythera import planentpos as p

import datetime
import math


def hohmann(orig, dest):
    u = 1.32712440018e20
    i = 0
    for i in range(len(p.list)):
        if orig == p.list[i].name:
            origin = p.list[i]
    i = 0
    for i in range(len(p.list)):
        if dest == p.list[i].name:
            destination = p.list[i]
    if origin.name == 'Sun' or destination.name == 'Sun':
        print("What the hell are you doing.")
        return
    if origin.name == destination.name:
        print("Already there")
        return
    a_transfer = 0.5 * (origin.a + destination.a)
    p_transfer = math.sqrt(a_transfer * a_transfer * a_transfer) / 2
    p_transferdays = p_transfer * 365
    print("The period in years to complete transfer is", p_transfer, "years or", p_transferdays, "days")
    deltaang = destination.degreeperiod * p_transferdays
    # if the angle is greater than 360, take the mod of it to make it smaller
    delta2 = math.fmod(deltaang, 360)
    position = 180 - delta2
    if position < 0:
        position = math.fabs(position)
        print("In order to perform this transfer orbit,", origin.name, " must be", position, "degrees ahead of", destination.name)
    else:
        print("In order to perform this transfer orbit,", origin.name, " must be", position, "degrees ahead of", destination.name)
    V1 = math.sqrt(u / origin.a) * (math.sqrt((2 * destination.a) / (origin.a + destination.a)) - 1)
    V2 = math.sqrt(u / destination.a) * (1 - math.sqrt((2 * origin.a) / (origin.a + destination.a)))
    totalV = V1 + V2
    totalV = math.fabs(totalV)
    print("The total ∆V to get from", origin.name, "to", destination.name, "is", totalV)
    k = 1
    ref = datetime.datetime(2000, 1, 1, 12, 0, 0)
    date = datetime.datetime(2008, 1, 1, 12, 0, 0)
    while (k):
        days_elapsed = date - ref
        dec_days_elapsed = days_elapsed.days + (12 / 24 + 0 / 60 / 24 + 0 / 60 / 60 / 24) - (12 / 24 + 0 / 60 / 24 + 0 / 60 / 60 / 24)
        Tme = dec_days_elapsed / 36525
        ox, oy, oz = origin.calc_pos(origin.i, origin.icy, origin.a, origin.acy, origin.an, origin.ancy, origin.e, origin.ecy, origin.l, origin.lcy, origin.w, origin.wcy, Tme)
        dx, dy, dz = destination.calc_pos(destination.i, destination.icy, destination.a, destination.acy, destination.an, destination.ancy, destination.e, destination.ecy, destination.l, destination.lcy, destination.w, destination.wcy, Tme)
        temp = math.atan2(oy - dy, ox - dx)
        temp = temp * (180/math.pi)
        if math.isclose(position, temp, rel_tol=0.005):
            print("The window opens on", date)
            date2 = date + datetime.timedelta(days = p_transferdays)
            print("Arrival on", destination.name, "will occur on", date2)
            days_elapsed = date2 - ref
            dec_days_elapsed = days_elapsed.days + (12 / 24 + 0 / 60 / 24 + 0 / 60 / 60 / 24) - (12 / 24 + 0 / 60 / 24 + 0 / 60 / 60 / 24)
            Tme2 = dec_days_elapsed / 36525
            ox2, oy2, oz2 = origin.calc_pos(origin.i, origin.icy, origin.a, origin.acy, origin.an, origin.ancy, origin.e, origin.ecy, origin.l, origin.lcy, origin.w, origin.wcy, Tme2)
            dx2, dy2, dz2 = destination.calc_pos(destination.i, destination.icy, destination.a, destination.acy, destination.an, destination.ancy, destination.e, destination.ecy,destination.l, destination.lcy, destination.w, destination.wcy, Tme2)
            break
        else:
            date += datetime.timedelta(days=1)
            k =1