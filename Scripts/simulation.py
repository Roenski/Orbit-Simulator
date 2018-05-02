from solar_system import Solar_system
from runge_kutta import Runge_Kutta
from unit import t_unit

class Simulation:
	# make the solarsystem publicly accessible for easier editing
	solarsystem = Solar_system()
	
	'''
	Initializes a Simulation type.
	@param ss: Solar_system
	@param prd: float
	@param stp: float
	'''
	def __init__(self, ss = Solar_system(), prd = 0, stp = 0):
		self.solarsystem = ss # solar system to be simulated
		self._period = prd # time period of the simulation
		self._step = stp # time step for the simulation
		self._time = 0 # time elapsed
		self._method = Runge_Kutta() # simulation metod
		
	def set_solarsystem(self, ss):
		self.solarsystem = ss
		
	def set_period(self, prd):
		self._period = prd
		
	def set_step(self, stp):
		self._step = stp
		
	def set_time(self, tm):
		self._time = tm
		
	def get_step(self):
		return self._step
		
	def get_period(self):
		return self._period
		
	def get_solarsystem(self):
		return self.solarsystem
		
	'''
	Simulates one time step.
	'''	
	def simulate(self):
		# do the simulation if there is still time
		if self._time < self._period:
			self.solarsystem = self._method.calculate(self.solarsystem, self._step, self._period)
			self._time += self._step
			return True
		else:
			return False
		

