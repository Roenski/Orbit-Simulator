from celestial_object import Cel_object

class Planet(Cel_object):
	
	'''
	@param diameter: float
	'''
	
	def __init__(self, name, route, mass, diameter):
		super().__init__(name, route, mass)
		self._diameter = diameter

	def is_sun(self):
		return False

	'''
	Returns a copy of the planet with updated route-parameters.
	Used in simulation.
	@param route: Route
	@returns new_planet: Planet
	'''
	def updated_copy(self, route):
		new_planet = Planet(self._name, route, self._mass, self._diameter)
		return new_planet
	
	def get_diameter(self):
		return self._diameter
		
	def update_route(self, new_route):
		self._route = new_route
