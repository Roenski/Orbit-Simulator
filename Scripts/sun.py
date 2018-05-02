from celestial_object import Cel_object

'''
The Sun of the solar system.
'''
class Sun(Cel_object):
	
	def __init__(self, name, route, mass, diameter):
		super().__init__(name, route, mass)
		self._diameter = diameter
		
	def is_sun(self):
		return True
