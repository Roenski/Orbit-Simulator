from unit import m_unit, x_unit, t_unit
from planet import Planet
from sun import Sun
from route import Route

'''
The class that reads planets from the planet file.
Used also in reading user input.
'''

class Read_planets:
	
	def read(self, input):
		self.planets = [] 
		self.read_planets = 0 # number of planets read
		
		try:
			
			line = input.readline()
			attribute = 0 # this variable determines which attribute is being read
			self.reset_attributes()
			
			while line != "":
				line = "".join(line.split()) # strips all whitespaces
				if line == "": # skip a blank row
					line = input.readline()
					continue
				try:
					if attribute == 0: # read the name
						self.name = self.read_name(line)
						attribute += 1
					elif attribute == 1: # read the mass
						self.mass = self.read_mass(line)
						attribute += 1
					elif attribute == 2: # read the diameter
						self.diameter = self.read_diameter(line)
						attribute += 1
					elif attribute == 3: # read the position vector
						self.position = self.read_position(line)
						attribute += 1
					elif attribute == 4: # read the velocity vector
						self.velocity = self.read_velocity(line)
						self.route = Route(self.position, self.velocity)
						
						if self.name.lower() == "aurinko" or self.name.lower() == "sun": # check if planet is the Sun
							planet = Sun(self.name, self.route, self.mass, self.diameter) 
							print("Succesfully saved the Sun, called {:s}".format(self.name))
						else:
							planet = Planet(self.name, self.route, self.mass, self.diameter)
							print("Succesfully saved planet called {:s}".format(self.name))
						self.planets.append(planet)
						self.read_planets += 1
						self.reset_attributes()
						attribute = 0
				
				except Exception as e: # if an error happened while reading an attribute
					if self.name != None:
						print("Failed to load a planet called {:s}. Error: {:s}".format(self.name, str(e)))
					else:
						print("Failed to load planet number {:d} entirely! Error: {:s}".format(self.read_planets, str(e)))

					'''
					Should implement here some code that skips to next planet
					'''
					
				line = input.readline()
					
		except:
			pass
							
		return self.planets
		
	def read_diameter(self, diameter):
		
		'''
		@param diameter: string with a from "(int)(string)", i.e "12km"
		'''
		
		number = ""
		unit = ""
		
		'''
		Go through each character that is a digit.
		For floating point numbers, also '.' or ',' are valid.
		'''
		for char in diameter:
			if char.isdigit():
				number += char
			elif char == "." or char == ",":
				number += "."
			elif char == "e" or char == "E" or char == "-":
				number += char
			else:
				break
				
		'''
		Store the size of the number, and if there are no
		numbers, raise an error
		'''
		num_len = len(number)
		if num_len == 0:
			raise ValueError
		
		'''
		Store the rest of the string, the unit-part, to a string.
		'''
		for char in diameter[num_len:]:
			unit += char
		
		'''
		Convert the number-string to a floating point number.
		This will throw an error if there are strings such as
		12.34.56 or 123,45.4 etc.	
		'''	
		try:
			number = float(number)
		except ValueError:
			raise ValueError("Problem with reading diameter value")
		
		'''
		Convert the given unit into SI-form. If the unit is not proper,
		throw an error.
		'''

		if unit == "mm":
			number *= x_unit.mm.value
		elif unit == "cm":
			number *= x_unit.cm.value
		elif unit == "dm":
			number *= x_unit.dm.value
		elif unit == "m":
			number *= x_unit.m.value
		elif unit == "km":
			number *= x_unit.km.value
		elif unit == "Mm":
			number *= x_unit.Mm.value
		elif unit == "Gm":
			number *= x_unit.Gm.value
		elif unit == "Tm":
			number *= x_unit.Tm.value
		else:
			raise ValueError("Problem with reading diameter unit")
			
		return number
		
	def read_mass(self, mass):
		'''
		@param mass: string with a form "(int)(string)", i.e "12kg"
		returns: mass in kilograms (float)
		'''
		
		number = ""
		unit = ""
		
		'''
		Go through each character that is a digit.
		For floating point numbers, also '.' or ',' are valid.
		'''
		for char in mass:
			if char.isdigit():
				number += char
			elif char == "." or char == "," :
				number += "."
			elif char == "e" or char == "E" or char == "-":
				number += char
			else:
				break
		
		'''
		Raise an error if there is no number
		'''
		num_len = len(number)
		if num_len == 0:
			raise ValueError("There were no numbers in mass.")
		
		'''
		Convert the number to floating point
		'''
		try:
			number = float(number)
		except ValueError:
			raise ValueError("Problem with converting mass number to float.")
			
		'''
		Store the rest to a string. This is the unit part
		'''
		for char in mass[num_len:]:
			unit += char
			
		'''
		Check which unit it is. Throw error if invalid unit.
		'''
		if unit == "g":
			number *= m_unit.g.value
		elif unit == "kg":
			number *= m_unit.kg.value
		elif unit == "Mg":
			number *= m_unit.Mg.value
		elif unit == "Gg":
			number *= m_unit.Gg.value
		elif unit == "Tg":
			number *= m_unit.Tg.value
		elif unit == "Pg":
			number *= m_unit.Pg.value
		elif unit == "Eg":
			number *= m_unit.Eg.value
		elif unit == "Zg":
			number *= m_unit.Zg.value
		elif unit == "Yg":
			number *= m_unit.Yg.value
		else:
			raise ValueError("Problem with reading mass unit.")
			
		return number
		
	def read_name(self, name):
		return name
		
		
	def read_position(self, position):
		
		'''
		@param: position: a string, that has to be in form:
		"x:(float)(unit)y:(float)(unit)z:(float)(unit)" 
		(the string has been stripped from whitespace beforehand)
		'''
		
		'''
		Reading the x-coordinate starts here
		'''
		
		'''
		Using iterators this time.
		'''
		pos_it = position.__iter__()
		
		'''
		First characters have to be "x:"
		'''
		if pos_it.__next__() != "x" or pos_it.__next__() != ":":
			raise ValueError("Problem with reading x-coordinate")
			
		x_val = ""
		x_u = ""
				
		'''
		Reading the x-value
		'''
		while True:
			try:
				char = pos_it.__next__()
			except StopIteration:
				raise ValueError("Iteration reached end at reading x-value")
				
			if char.isdigit():
				x_val += char
			elif char == "." or char == ",": 
				x_val += "."
			elif char == "e" or char == "E" or char == "-": # these are for ten's exponentials, e.g 1e3 = 1000
				x_val += char
			else:
				break
			
		x_val_len = len(x_val)

		if x_val_len == 0:
			raise ValueError("Problem with reading x-coordinate (value length 0)")
		
		try:
			x_val = float(x_val)
		except ValueError:
			raise ValueError("Problem with converting x value to float")
			
		'''
		Read the x unit until the start of y-coordinate is found
		'''
		while True:
			if char == "y":
				break
			x_u += char
			try:
				char = pos_it.__next__()
			except StopIteration:
				raise ValueError("Stopped iteration while finding 'y' after x-unit)")
				break
			
		if x_u == "mm":
			x_val *= x_unit.mm.value
		elif x_u == "cm":
			x_val *= x_unit.cm.value
		elif x_u == "dm":
			x_val *= x_unit.dm.value
		elif x_u == "m":
			x_val *= x_unit.m.value
		elif x_u == "km":
			x_val *= x_unit.km.value
		elif x_u == "Mm":
			x_val *= x_unit.Mm.value
		elif x_u == "Gm":
			x_val *= x_unit.Gm.value
		elif x_u == "Tm":
			x_val *= x_unit.Tm.value
		else:
			raise ValueError("Problem with reading x-coordinate unit")
			
		'''
		Reading the x-coordinate ends here.
		
		Reading the y-coordinate starts here.
		Nearly identical steps compared to reading the x-coordinate.
		'''
		
		y_val = ""
		y_unit = ""
		
		# iterate over the ':' character, which is required
		try:
			char = pos_it.__next__()
		except StopIteration:
			raise ValueError("Iteration stopped at reading ':' at y")
		
		if char != ":":
			raise ValueError("The character after 'y' should be ':'")
		
		while True:
			try:
				char = pos_it.__next__()
			except StopIteration:
				raise ValueError("Iteration stopped at reading y value")
			if char.isdigit():
				y_val += char
			elif char == "." or char == ",": 
				y_val += "."
			elif char == "e" or char == "E" or char == "-":
				y_val += char
			else:
				break
				
		y_val_len = len(y_val)
		
		if y_val_len == 0:
			raise ValueError("Problem with reading y-coordinate value")
		
		try:
			y_val = float(y_val)
		except ValueError:
			raise ValueError("Problem with converting y-coordinate value to float")
			
		while True:
			if char == "z":
				break
			y_unit += char
			try:
				char = pos_it.__next__()
			except StopIteration:
				raise ValueError("Stopped iteration while searching for 'z' after y-unit)")
				break
				
		if y_unit == "mm":
			y_val *= x_unit.mm.value
		elif y_unit == "cm":
			y_val *= x_unit.cm.value
		elif y_unit == "dm":
			y_val *= x_unit.dm.value
		elif y_unit == "m":
			y_val *= x_unit.m.value
		elif y_unit == "km":
			y_val *= x_unit.km.value
		elif y_unit == "Mm":
			y_val *= x_unit.Mm.value
		elif y_unit == "Gm":
			y_val *= x_unit.Gm.value
		elif y_unit == "Tm":
			y_val *= x_unit.Tm.value
		else:
			raise ValueError("Problem with reading y-coordinate unit")
			
		'''
		Reading the y-coordinate ends here.
		
		Reading the z-coordinate starts here.
		Again, identical steps compared to previous components.
		'''
		
		z_val = ""
		z_unit = ""
		
		# iterate over the ':' character, which is required
		try:
			char = pos_it.__next__()
		except StopIteration:
			raise ValueError("Iteration stopped at reading ':' at z")
		
		if char != ":":
			raise ValueError("The character after 'z' should be ':'")
		
		while True:
			try:
				char = pos_it.__next__()
			except StopIteration:
				raise ValueError("Iteration stopped at reading z value")
			if char.isdigit():
				z_val += char
			elif char == "." or char == "," or char == "e" or char == "E" or char == "-":
				z_val += char
			else:
				break
				
		z_val_len = len(z_val)
		if z_val_len == 0:
			raise ValueError("Problem with reading z-value (lenght 0)")
			
		try:
			z_val = float(z_val)
		except ValueError:
			raise ValueError("Problem with converting z-coordinate value to float")
			
		while True:
			z_unit += char
			try:
				char = pos_it.__next__()
			except StopIteration:
				break
				
		if z_unit == "mm":
			z_val *= x_unit.mm.value
		elif z_unit == "cm":
			z_val *= x_unit.cm.value
		elif z_unit == "dm":
			z_val *= x_unit.dm.value
		elif z_unit == "m":
			z_val *= x_unit.m.value
		elif z_unit == "km":
			z_val *= x_unit.km.value
		elif z_unit == "Mm":
			z_val *= x_unit.Mm.value
		elif z_unit == "Gm":
			z_val *= x_unit.Gm.value
		elif z_unit == "Tm":
			z_val *= x_unit.Tm.value
		else:
			raise ValueError("Problem with reading z-coordinate unit")
			
		pos_vec = [x_val, y_val, z_val]
		return pos_vec

		
	'''
	Read the velocity vector.
	It just edits the string to resemble a position vector
	by removing '/s'-parts. 
	@param velocity: string
	@param velocity_vector: array
	'''	
	def read_velocity(self, velocity):
		velocity = velocity.replace("/s", "")
		velocity_vector = self.read_position(velocity)
		return velocity_vector
		
	'''
	Read a time string.
	@param time: string
	@returns time_total: float
	'''	
	def read_time(self, time):
		time = "".join(time.split())
		time_it = time.__iter__()
		time_val = ""
		time_u = ""
		
		'''
		Iterate and copy the contents until a non-number or non-comma is found.
		'''
		while True:
			try:
				next = time_it.__next__()
				if next.isdigit() or next == "," or next == ".":
					time_val += next
				else:
					break
			except StopIteration:
				raise ValueError("Problem with reading time unit")
				
		if time_val == 0:
			raise ValueError("Problem with reading time value (length was 0)")
			
		try:
			time_val = float(time_val)
		except:
			raise ValueError("Problem with converting time value to int")
				
		'''
		Copy the rest of the string.
		'''		
		while True:
			try:
				time_u += next
				next = time_it.__next__()
			except StopIteration:
				break
				
				
		'''
		Convert the unit to seconds
		'''
		time_total = 0
		if time_u == "ms":
			time_total = time_val*t_unit.ms.value
		elif time_u == "s":
			time_total = time_val
		elif time_u == "min":
			time_total = time_val*t_unit.min.value
		elif time_u == "h":
			time_total = time_val*t_unit.h.value
		elif time_u == "d":
			time_total = time_val*t_unit.d.value
		elif time_u == "wk":
			time_total = time_val*t_unit.wk.value
		elif time_u == "mo":
			time_total = time_val*t_unit.mo.value
		elif time_u == "y":
			time_total = time_val*t_unit.y.value
		else:
			raise ValueError("Problem with reading time unit")
			
		return time_total

		
	'''
	Resets the planet attributes when a planet has been read
	'''
	def reset_attributes(self):
		self.name = None
		self.mass = None
		self.position = [None]
		self.velocity = [None]
		self.diameter = None
