import sqlite3

connection2 = sqlite3.connect('planet.db')

crsr2 = connection2.cursor()


sql_command = """INSERT INTO planet VALUES('Pluto', 2370, 0.0146, 2095, 4.74, 247.93, 6.3874, 0.248,5906.4, 5);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES('Neptune', 49528, 102, 1638, 5.4, 163.72, 16.11, 0.01, 4495.1, 14);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES('Uranus', 51118, 86.8, 1271, 6.8, 84.04, 17.2, 0.046,2872.5, 27);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES('Saturn', 120536, 568, 687, 9.6, 29.41, 10.13, 0.054, 1433.5, 62);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES('Jupiter', 142984, 1898, 1326, 13.1, 11.86, 9.5, 0.048,778.6, 79);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES('Mars', 6794, 0.642, 3940, 24.1, 686.98, 24.37, 0.093,227.9, 2);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES('Venus', 12104, 4.87, 5240, 35, 224.70, 243.01, .007, 108.2, 0);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES ('Earth', 12756, 5.97, 5500, 29.8, 365.256, 23.9345, 0.0167,149.6, 1);"""
crsr2.execute(sql_command)

sql_command = """INSERT INTO planet VALUES ('Mercury', 4878, 0.33, 5427, 47.4, 87.969, 58.646, 0.206, 57.9, 0);"""
crsr2.execute(sql_command)

connection2.commit()