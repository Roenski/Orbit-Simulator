import unittest


from vector import Vector
from route import Route
from celestial_object import Cel_object
from planet import Planet
from sun import Sun
from satellite import Satellite, State
from solar_system import Solar_system
from read_planets import Read_planets
from simulation import Simulation
from runge_kutta import Runge_Kutta
from tui import TUI
from unit import t_unit

class Test(unittest.TestCase):
	
	def setUp(self):
		self._solarsystem = Solar_system()
		#self._planet_1 = None
		
		route_1_x = [1000, 0, 0]
		route_1_v = [0, -1000, 0]
		route_1 = Route(route_1_x, route_1_v)
		name_1 = "Aalto-3"
		mass_1 = 10
		state_1 = State.ALIVE
		self._satellite_1 = Satellite(name_1, route_1, mass_1, state_1)
		
		route_1_x = [152100000000, 0, 0]
		route_1_v = [0, 29780, 0]
		route_1 = Route(route_1_x, route_1_v)
		name_1 = "Earth"
		mass_1 = 5.97237*10**24
		diameter = 2*6371000
		self._planet_1 = Planet(name_1, route_1, mass_1, diameter)
		
		self.pos_test_string = "x:220my:100kmz:20m"
		self.test_read = Read_planets()
		test_file = open("test_read.txt")
		self._solarsystem.read_planets(test_file)		
		test_file.close()
		
		

		
	
	def test_satellites(self):
		
		self.assertEqual("Aalto-3", self._satellite_1.get_name(), "Satellite name should be Aalto-3")
		self.assertEqual([1000, 0, 0], \
		[self._satellite_1.get_route().x_vector.x, self._satellite_1.get_route().x_vector.y, self._satellite_1.get_route().x_vector.z], \
		 "Position coordinates should be 1000, 0, 0")
		self.assertEqual([0, -1000, 0], \
		[self._satellite_1.get_route().v_vector.x, self._satellite_1.get_route().v_vector.y, self._satellite_1.get_route().v_vector.z], \
		"Velocity components should be 0, 1000, 0")
		
	def test_planets(self):
		self.assertEqual("Earth", self._planet_1.get_name(), "Planet name should be Earth")
		self.assertEqual([152100000000, 0, 0], \
		[self._planet_1.get_route().x_vector.x, self._planet_1.get_route().x_vector.y, self._planet_1.get_route().x_vector.z], \
		"Planet coordinates should be" + str([152100000000, 0, 0]))
		self.assertEqual([0, 29780, 0], \
		[self._planet_1.get_route().v_vector.x, self._planet_1.get_route().v_vector.y, self._planet_1.get_route().v_vector.z], \
		"Planet coordinates should be" + str([0, 29780, 0]))
		
	def test_adding_cel_objects(self):
		self._solarsystem.add_satellite(self._satellite_1)
		self._solarsystem.add_planet(self._planet_1)
		self.assertTrue((self._satellite_1 in self._solarsystem.get_satellites()))
		self.assertTrue((self._planet_1 in self._solarsystem.get_planets()))
		
	def test_updating_route(self):
		route_2_x = [500, 500, 0]
		route_2_v = [-500, -500, 0]
		route_2 = Route(route_2_x, route_2_v)
		self._satellite_1.update_route(route_2)
		self.assertEqual(route_2_x, \
		[self._satellite_1.get_route().x_vector.x, self._satellite_1.get_route().x_vector.y, self._satellite_1.get_route().x_vector.z], \
		 "Position coordinates should be " + str(route_2_x))
		self.assertEqual(route_2_v, \
		[self._satellite_1.get_route().v_vector.x, self._satellite_1.get_route().v_vector.y, self._satellite_1.get_route().v_vector.z], \
		"Velocity components should be " + str(route_2_v))
		
	def test_reading_position(self):
		corr_pos = [220.0, 100000.0, 20.0]
		ret_pos = self.test_read.read_position(self.pos_test_string)
		self.assertEqual(corr_pos, ret_pos, "Position vector should be " + str(corr_pos))
		
	def test_reading_file(self):
		test_file = open("test_read.txt")
		self._solarsystem.read_planets(test_file)		
		test_file.close()
		self.assertEqual(self._solarsystem.get_planets()[0].get_name(), "Maa", "planet should be called 'Maa'")
		self.assertEqual(self._solarsystem.get_planets()[0].get_mass(), 5.97219*10**24, "Planet mass wrong") 
		self.assertEqual(self._solarsystem.get_planets()[0].get_diameter(), 6371*10**3, "Planet diameter wrong")
		test_route = Route([149.6*10**9, 0, 0], [0, 30*10**3, 0])
		self.assertEqual(self._solarsystem.get_planets()[0].get_route().x_vector.x, test_route.x_vector.x, "Route is wrong")
		self.assertEqual(self._solarsystem.get_planets()[0].get_route().v_vector.y, test_route.v_vector.y, "Route is wrong")
		
		self.assertEqual(self._solarsystem.get_sun().get_mass(), 1.98855e30, "The sun has wrong mass")
		self.assertEqual(self._solarsystem.get_sun().get_name(), "Aurinko", "The name of the sun should be 'Aurinko'")
		
		

if __name__ == "__main__":
	unittest.main()
