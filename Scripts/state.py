from vector import Vector

'''
Used in simulation. Stores two Vector types.
'''

class State:
	def __init__(self, pos, vel):
		self._x = pos
		self._v = vel
		
	def get_x(self):
		return self._x
		
	def get_v(self):
		return self._v
		
	x = property(get_x)
	v = property(get_v)
	
