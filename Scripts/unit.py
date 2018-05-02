from enum import Enum

class m_unit(Enum):
	# the multipliers are compared to kg (kilogram), which is the SI-unit
	g = 10**-3
	kg = 1
	Mg = 10**3
	Gg = 10**6
	Tg = 10**9
	Pg = 10**12
	Eg = 10**15
	Zg = 10**18
	Yg = 10**21
	
	
class x_unit(Enum):
	# the multipliers are compared to m (metre), which is the SI-unit
	mm = 10**-3
	cm = 10**-2
	dm = 10**-1
	m = 1
	km = 10**3
	Mm = 10**6
	Gm = 10**9
	Tm = 10**12
	
class t_unit(Enum):
	# multipliers are compared to s (second), which is the SI-unit
	ms = 10**-3
	s = 1
	min = 60
	h = 60*60
	d = 24*60*60
	wk = 7*24*60*60
	mo = 30*24*60*60
	y = 365*24*60*60
	
