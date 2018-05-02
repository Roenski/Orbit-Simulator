from solar_system import Solar_system
from planet import Planet
from state import State
from vector import Vector
from route import Route
import numpy as np


class Runge_Kutta:
	
	'''
	@param solarsystem: Solarsystem
	@param step: float
	@param period: float
	'''
	def calculate(self, solarsystem, step, period):
		self.solarsystem = solarsystem
		# initialize the next step solarsystem
		self.new_system = Solar_system()
		
		for planet in solarsystem.get_planets():
			if planet.is_sun():
				self.new_system.set_sun(planet)
				self.new_system.add_planet(planet)
			else:
				# calculate new route for planet
				route_derivative = self.integrate(planet, step)
				new_route = planet.get_route() + route_derivative*step
				new_planet = planet.updated_copy(new_route)
				self.new_system.add_planet(new_planet)
			
		for satellite in solarsystem.get_satellites():
			# calculate new route for satellite
			route_derivative = self.integrate(satellite, step)
			new_route = satellite.get_route() + route_derivative*step
			new_sat = satellite.updated_copy(new_route)
			self.new_system.add_satellite(new_sat, False)
			
		return self.new_system
		
	
	'''
	@param state: State
	@param name: string
	'''
	def calculate_acc(self, state, name):
		g_const = 6.67408*(10**-11)
		dv_x = 0
		dv_y = 0
		dv_z = 0
		for planet in self.solarsystem.get_planets():
			if planet.get_name() == name: # don't calculate the force with yourself
				continue
			# R = (x_planet - x_calculated)x + (y_planet - y_calculated)y + (z_planet - z_calculated)z
			r_vector = Vector(planet.get_route().x_vector.x - state.x.x, planet.get_route().x_vector.y - state.x.y, planet.get_route().x_vector.z - state.x.z)
			r_len = r_vector.get_length()
			# unit vector
			r_hat = r_vector / r_len
			# Newton law of gravity
			acc = g_const*planet.get_mass()/r_len**2
			# multiply the overall force with unit vector components
			dv_x = dv_x + (acc*r_hat.x)
			dv_y = dv_y + (acc*r_hat.y)
			dv_z = dv_z + (acc*r_hat.z)
		return Vector(dv_x, dv_y, dv_z)
			
	'''
	@param state: State
	@param step: float
	@param derivative: State
	@param name: string
	'''
	def calculate_param(self, state, step, derivative, name):
		x = state.x + derivative.x*step
		v = state.v + derivative.v*step
		new_state = State(x, v)
		
		dx = new_state.v
		dv = self.calculate_acc(new_state, name)
		return State(dx, dv)
			
	'''
	@param cel_object: Celestial_object
	@param step: float
	'''
	def integrate(self, cel_object, step):
		
		# create the state that has current x and v vector
		state = State(cel_object.get_route().x_vector, cel_object.get_route().v_vector)
		name = cel_object.get_name()
		mass = cel_object.get_mass()
		
		# calculate the parameters for Runge-Kutta method
		a = self.calculate_param(state, 0*step, State(Vector(0,0,0), Vector(0,0,0)), name)
		b = self.calculate_param(state, 0.5*step, a, name)
		c = self.calculate_param(state, 0.5*step, b, name)
		d = self.calculate_param(state, step, c, name)
		
		dx = (1/6)*(a.x + 2*(b.x + c.x) + d.x)
		dv = (1/6)*(a.v + 2*(b.v + c.v) + d.v)
		return Route(dx, dv)
		
	
			
