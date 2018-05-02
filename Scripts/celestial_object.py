from route import Route

class Cel_object:
	
	
	def __init__(self, name, route, mass):
		'''
		Every celestial object has these attributes
		
		@param route: Route
		@param name: string
		@param mass: float
		'''
		
		self._route = route
		self._name = name
		self._mass = mass
		
		
	def get_route(self):
		return self._route
		
	def get_name(self):
		return self._name
		
	def get_mass(self):
		return self._mass
