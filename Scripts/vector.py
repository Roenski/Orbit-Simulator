import numpy as np
from numpy import linalg as la

class Vector:
	'''
	This class handles all vector calculations
	'''
	
	'''
	Initialize a vector as a numpy array
	@param x,y,z: float
	'''
	def __init__(self, x, y, z):
		self._vector = np.array([x, y, z], dtype = np.float64)
		
	'''
	Operator overloads
	'''
	def __mul__(self, other):
		if type(other) is Vector:
			new_numpy = self._vector*other.get_numpy()
		else:
			new_numpy = self._vector*other
		return self.make_vector(new_numpy)
		
	def __rmul__(self, other):
		if type(other) is Vector:
			new_numpy = self._vector*other.get_numpy()
		else:
			new_numpy = self._vector*other
		return self.make_vector(new_numpy)
			
	def __add__(self, other):
		if type(other) is Vector:
			new_numpy = self._vector+other.get_numpy()
		else:
			new_numpy = self._vector+other
		return self.make_vector(new_numpy)
		
	def __truediv__(self, other):
		if type(other) is Vector:
			new_numpy = self._vector/other.get_numpy()
		else:
			new_numpy = self._vector/other
		return self.make_vector(new_numpy)
		
	def __floordiv__(self, other):
		if type(other) is Vector:
			new_numpy = self._vector/other.get_numpy()
		else:
			new_numpy = self._vector/other
		return self.make_vector(new_numpy)
		
	def __sub__(self, other):
		if type(other) is Vector:
			new_numpy = self._vector-other.get_numpy()
		else:
			new_numpy = self._vector-other
		return self.make_vector(new_numpy)
		
	def __getitem__(self, index):
		return self._vector[index]
		
	def __str__(self):
		string = str(self._vector[0]) + " " + str(self._vector[1]) + " " + str(self._vector[2])
		return string
		
	def get_numpy(self):
		return self._vector
		
	def get_x(self):
		return self._vector[0]
		
	def get_y(self):
		return self._vector[1]
		
	def get_z(self):
		return self._vector[2]
		
	def get_length(self):
		return la.norm(self._vector)
		
	def get_unit_vector(self):
		return np.divide(self._vector, self.get_length())
		
	def make_vector(self, numpy):
		vector = Vector(numpy[0], numpy[1], numpy[2])
		return vector
		
	# allows for easy access to components, i.e vector.x, vector.y
	x = property(get_x)
	y = property(get_y)
	z = property(get_z)
