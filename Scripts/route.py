from vector import Vector

class Route:
	
	'''
	Initialize a Route type
	@param position: array, e.g [1,2,3]
	@param velocity: array, e.g [1,2,3]
	'''
	def __init__(self, position, velocity):
		self._x_vector = Vector(position[0], position[1], position[2])
		self._v_vector = Vector(velocity[0], velocity[1], velocity[2])
	
	def get_x_vector(self):
		return self._x_vector
		
	def get_v_vector(self):
		return self._v_vector
	
	'''
	Operator overloads.
	'''
	def __add__(self, other):
		if type(other) is Route:
			new_x = self._x_vector + other.x_vector
			new_v = self._v_vector + other.v_vector
			return Route(new_x, new_v)
		else:
			raise ValueError("Route cannot be added with other than a Route-type.")
			
	def __sub__(self, other):
		if type(other) is Route:
			new_x = self._x_vector - other.x_vector
			new_v = self._v_vector - other.v_vector
			return Route(new_x, new_v)
		else:
			raise ValueError("Route cannot be subtracted with other than a Route-type.")
			
	def __mul__(self, other):
		if type(other) is Route:
			new_x = self._x_vector*other.x_vector
			new_v = self._v_vector*other.v_vector
			return Route(new_x, new_y)
		elif type(other) in (int, float):
			new_x = self._x_vector*other
			new_v = self._v_vector*other
			return Route(new_x, new_v)
		else:
			raise ValueError("Route cannot be multiplied with other than a Route-type, int or float.")
			
	def __rmul__(self, other):
		if type(other) is Route:
			new_x = self._x_vector*other.x_vector
			new_v = self._v_vector*other.v_vector
			return Route(new_x, new_y)
		elif type(other) in (int, float):
			new_x = self._x_vector*other
			new_v = self._v_vector*other
			return Route(new_x, new_v)
		else:
			raise ValueError("Route cannot be multiplied with other than a Route-type, int or float.")
		
	'''
	For easier access to the vectors
	'''	
	x_vector = property(get_x_vector)
	v_vector = property(get_v_vector)
	
