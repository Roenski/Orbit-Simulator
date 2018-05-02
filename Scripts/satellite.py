from celestial_object import Cel_object
from enum import Enum

class State(Enum):
	ALIVE = 1
	DESTROYED = 2

class Satellite(Cel_object):
	
	'''
	Initialize a Satellite type.
	@param name: string
	@param route: Route
	@param mass: float
	@param state: Satellite.State
	'''
	def __init__(self, name, route, mass, state):
		super().__init__(name, route, mass)
		self._state = state
		
	def get_name(self):
		return self._name	
		
	def is_alive(self):
		if self._state == State.ALIVE:
			return True
		return False
		
	def is_destroyed(self):
		if self._state == State.DESTROYED:
			return True
		return False
		
	def is_sun(self):
		return False
		
	def set_destroyed(self):
		self._state = State.DESTROYED
		
	def update_route(self, new_route):
		self._route = new_route
		
	'''
	Returns a copy of itself with the given route.
	@param new_route: Route
	@returns new_sat: Satellite
	'''
	def updated_copy(self, new_route):
		new_sat = Satellite(self._name, new_route, self._mass, self._state)
		return new_sat
