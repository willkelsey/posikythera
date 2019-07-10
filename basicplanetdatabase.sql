DROP TABLE IF EXISTS planetinfo;


create table planetinfo

	(name					varchar(20),
	diameter				decimal,
	mass					decimal,
	density					decimal, 
	meanorbitalvelocity		decimal,
	siderialperiod			decimal,
	rotationperiod			decimal,
	orbitaleccentricity		decimal,
	distancefromsun			decimal,
	numberofmoons			int,

	);


insert into planetinfo
values

	('Mercury', 4878, 0.33, 5427, 47.4, 87.969, 58.646, 0.206, 57.9, 0),
	('Venus', 12104, 4.87, 5240, 35, 224.70, 243.01, .007, 108.2, 0),
	('Earth', 12756, 5.97, 5500, 29.8, 365.256, 23.9345, 0.0167,149.6, 1),
	('Mars', 6794, 0.642, 3940, 24.1, 686.98, 24.37, 0.093,227.9, 2),
	('Jupiter', 142984, 1898, 1326, 13.1, 11.86, 9.5, 0.048,778.6, 79),
	('Saturn', 120536, 568, 687, 9.6, 29.41, 10.13, 0.054, 1433.5, 62),
	('Uranus', 51118, 86.8, 1271, 6.8, 84.04, 17.2, 0.046,2872.5, 27),
	('Neptune', 49528, 102, 1638, 5.4, 163.72, 16.11, 0.01, 4495.1, 14),
	('Pluto', 2370, 0.0146, 2095, 4.74, 247.93, 6.3874, 0.248,5906.4, 5);




/*Mass (10^24kg)
Diameter (km)
Density (kg/m3)
Gravity (m/s2)
Escape Velocity (km/s)
Rotation Period (hours)
Length of Day (hours)
Orbital Eccentricity
Orbital Velocity (km/s)
*/


--not perfect, might need some editing