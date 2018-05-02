from celestial_object import Cel_object
from planet import Planet
from sun import Sun
from satellite import Satellite
from route import Route
from vector import Vector
from read_planets import Read_planets

class Solar_system:
	
	'''
	Initializes a Solar_system type
	'''
	def __init__(self):
		self._satellites = [] # list of satellites
		self._planets = [] # list of planets
		self._sun = None # the Sun of the solar system
		self._read = Read_planets() # just a method to read the planets
		
	def add_planet(self, planet):
		self._planets.append(planet)
		
	'''
	Adds a satellite.
	@param satellite: Satellite (satellite to be added)
	@param message: boolean (whether the message is written to console or not)
	'''
	def add_satellite(self, satellite, message = True):
		self._satellites.append(satellite)
		if message == True:
			print("Satellite called " + satellite.get_name() + " was added.")
		
	'''
	Delete a satellite by name.
	@param satellite_name: string
	@returns: boolean (whether deletion was successful)
	'''
	def delete_satellite_by_name(self, satellite_name):
		for satellite in self._satellites:
			if satellite.get_name() == satellite_name:
				self._satellites.remove(satellite)
				print("Satellite called " + satellite.get_name() + " was removed.")
				return True
		return False
	
	'''
	Delete a satellite.
	@param satellite: Satellite
	@returns: boolean (whether deletion was successful)
	'''
	def delete_satellite(self, satellite):
		if satellite in self._satellites:
			self._satellites.remove(satellite)
			print("Satellite called " + satellite.get_name() + " was removed.")
			return True
		return False
	
	def delete_all_satellites(self):
		self._satellites = []
		print("All satellites were deleted.")
			
	def get_planets(self):
		return self._planets
			
	def get_satellites(self):
		return self._satellites
		
	def get_sun(self):
		return self._sun
		
	'''
	Read the planets from a planet file.
	@param input: file object
	'''	
	def read_planets(self, input):
		self._planets = self._read.read(input)
		for planet in self._planets:
			if planet.get_name().lower() == "aurinko" or planet.get_name().lower() == "sun":
				self.set_sun(planet)
				return
		raise OSError("Couldn't find the Sun from the file")
		
	'''
	Overloads conversion to string.
	'''	
	def __str__(self):
		string = ""
		for cel_object in self._planets:
			string = string + cel_object.get_name() + " " + str(cel_object.get_route().x_vector) + " "
		for satellite in self._satellites:
			string = string + satellite.get_name() + " " + str(satellite.get_route().x_vector) + " "
		string += "\n"
		return string

		
	def set_sun(self, sun):
		self._sun = sun
		
	def set_planets(self, planets):
		self._planets = planets
	
	def set_satellites(self, satellites):
		self._satellites = satellites
