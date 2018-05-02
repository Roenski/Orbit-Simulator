from simulation import Simulation
from route import Route
from state import State
from solar_system import Solar_system
from satellite import Satellite
from satellite import State as SatState
from unit import x_unit, m_unit, t_unit
from read_planets import Read_planets

'''
Text-based user interface.
''' 
class TUI:
	def __init__(self):
		self._simulation = Simulation()
		
		# The solar system in the beginning of the simulation
		# It will be loaded when user wants to reset the simulation.
		self._begin_ss = Solar_system() 
		self.print_menu()

	def print_menu(self):
		print("Welcome to Solar System Simulator!\n")
		self.ask_for_planetfile()
		
		# for test purposes
		
		#sat1 = Satellite("Aalto-1", Route([300e3+6371e3, 0, 0], [0, 7.8e3 , 0]), 10, SatState.ALIVE)
		#sat2 = Satellite("Aalto-3", Route([30e9, 0, 0], [0, 20e3, 0]), 1, SatState.ALIVE)
		#self._simulation.solarsystem.add_satellite(sat1)
		#self._simulation.solarsystem.add_satellite(sat2)
		
		
		print("\nYou have the following options:")
		self.print_options()
		
		'''
		Loop until valid input is given
		'''
		choice = self.loop_until_valid()
		
		'''
		The main loop of the program.
		'''
		while True:
			'''
			Add a satellite.
			'''
			if choice == 1:
				self.ask_for_satellite()
			
			
			# Remove a satellite.	
			elif choice == 2:
				if not self._simulation.solarsystem.get_satellites():
					print("There are no satellites to remove!")
				else:
					print("Here are the satellites that have been added:")
					self.print_satellites()
					print("Which of these you wish to remove?")
					rem_name = input()
					if self._simulation.solarsystem.delete_satellite_by_name(rem_name):
						pass
					else:
						print("Could not find a satellite called {:s} .".format(rem_name))
						
			
			# Change the planetfile.
			elif choice == 3:
				self._simulation.solarsystem.delete_all_satellites()
				self.ask_for_planetfile()
				
			
			# Change simulation settings.
			elif choice == 4:
				times = self.ask_for_settings()
				try:
					self._simulation.set_step(times[0])
					self._simulation.set_period(times[1])
				except:
					print("Quit adding settings due to an error")

			
			# Simulate.
			elif choice == 5:
				everything_is_fine = True # variable to check if simulation settings are done.
				
				while True:
					if self._simulation.get_step() <= 0 or self._simulation.get_period() <= 0:
						print("\nSimulation settings haven't been correctly set yet.")
						try:
							# Ask for simulation settings.
							times = self.ask_for_settings()
							self._simulation.set_step(times[0])
							self._simulation.set_period(times[1])
						except Exception as e:
							print("Encountered an error with the following message: " + str(e))
							everything_is_fine = False

				
					if everything_is_fine:
						# ask if user wants to save results to a file
						save = self.ask_for_input("Do you wish to have the results saved to a file? (y/n)")
						if save.lower() == "y":
							filename = input("Please give the filename you wish to save the results to: ")
							file = open(filename, 'w')
							
							# Here the simulation starts
							print(self._simulation.solarsystem)
							file.write(str(self._simulation.solarsystem))
							while self._simulation.simulate(): # this returns false when simulation ends
								print(self._simulation.solarsystem)
								file.write(str(self._simulation.solarsystem))
							file.close()
						
						# simulation without saving to a file
						else:
							print(self._simulation.solarsystem)
							while self._simulation.simulate():
								print(self._simulation.solarsystem)
							
						print("\nSimulation finished. Restart the program to reset the situation, or continue simulating.")
						self._simulation.set_time(0)
						break
					
					else:
						break
						
			
			# Reset simulation.
			elif choice == 6:
				self.reset_simulation()
				print("The simulation was reset.")
				
			choice = self.loop_until_valid()
				
			
			
		
	def print_options(self):
		print("\n1. Add a satellite")
		print("2. Remove a satellite")
		print("3. Change the planet file (this will delete added satellites)")
		print("4. Change simulation settings")
		print("5. Simulate")
		print("6. Reset simulation (will not delete satellites)")
		print("You can also quit the program by typing 'Quit'.\n")
		
	def print_satellites(self):
		print("\nThe following satellites have been added:\n")
		for satellite in self._simulation.solarsystem.get_satellites():
			print(satellite.get_name())
			
	def print_planet_names(self):
		for planet in self._simulation.solarsystem.get_planets():
			if planet.is_sun():
				print(planet.get_name() + " (the Sun)")
			else:
				print(planet.get_name())
			
	'''
	Asks for simulation settings.
	@returns: array
	'''	
	def ask_for_settings(self):
		
		print("Please insert simulation settings.")
		print("Enter a number and a unit, e.g '10h'.")
		print("Available units are: ms, s, min, h, d, wk, mo, y.")
		try:
			step = input("Time step: ")
			step = Read_planets().read_time(step)
		except Exception as e:
			print("Encountered an error with the following message: " + str(e))
			return
			
		try:
			period = input("Total simulation time period: ")
			period = Read_planets().read_time(period)
		except Exception as e:
			print("Encountered an error with the following message: " + str(e))
			return
			
		ret = [step, period]
		return ret
		
	def ask_for_input(self, message):
		print("\n" + message)
		ans = input()
		return ans
	
	'''
	Asks for input until a valid input is given.
	'''	
	def loop_until_valid(self):
		while True:
			ans = self.ask_for_input("Please give your input: ")
			choice = None
			try:
				choice = int(ans)
				if not choice in (1,2,3,4,5,6): # the options in main menu
					print("Invalid input: your input must be a number between 1-6")
					print("You can print the options by typing 'Options' or 'Asetukset'")
				else:
					break
			except ValueError:
				# exit if a blank input is given
				if (ans.strip()).lower() in ("quit", "lopeta"):
					exit("User decided to quit the program")
				elif (ans.strip()).lower() in ("options", "asetukset"):
					self.print_options()
					continue
				print("Invalid input: your input must be a number between 0-5.") 
				print("You can print the options by typing 'Options' or 'Asetukset'")
		return choice
		
	'''
	Asks for a planet file. Adds the planets to the solar system.
	Loops until a valid file is given. No way to exit the program, other than Ctrl+Z
	'''
	def ask_for_planetfile(self):
		# loop until you get a valid input. A condition about exiting the program could be implemented.
		while True:
			print("Please enter the file name for planet specifications:")
			try:
				
				# testing purposes
				planet_file = input()
				# planet_file = "test_read.txt"
				
				planet_read = Read_planets()
				planets = open(planet_file)
				self._simulation.solarsystem.read_planets(planets)
				print("The planets were successfully read.")
				planets.close()
				self._begin_ss.set_planets(self._simulation.solarsystem.get_planets()) # copy the planets to the restart-solarsystem
				break
			except Exception as e:
				print("Encountered an error with the following message:")
				print("\t" + str(e))
		
		
				
	'''
	Adds a satellite to the system.
	'''
	def ask_for_satellite(self):
		print("\nPlease give the following information for the satellite. Remember to give the unit as well. A blank input will stop the process.\n")
		print("Units that can be used:")
		print("Mass: g, kg, Mg, Gg, Tg, Pg, Eg, Zg, Yg")
		print("Position: mm, cm, dm, m, km, Mm, Gm, Tm")
		print("Velocity: mm/s, cm/s, dm/s, m/s, km/s, Mm/s, Gm/s, Tm/s")
		print("You can also use format '1e-3' for 0.001, or 1e3 for 1000, for example.\n")
		print("Give the vectors in component format, i.e 'x: 10km y: 20e10m z: 0m'\n")
		reading_functions = Read_planets()
		
		name = None
		mass = None
		position = None
		velocity = None
		
		# reference point for the satellite. This way you can easily e.g set an orbit around the Earth for a satellite
		print("Which celestial object do you wish to be the reference point for the satellite?")
		print("Added planet(s):")
		self.print_planet_names()
		reference = input("Reference point: ")
		ref = 0 # the reference route
		for planet in self._simulation.solarsystem.get_planets():
			if planet.get_name() == reference:
				ref = planet.get_route() # set a planet as reference
				break
		if ref == 0:
			print("Chose the Sun as reference point.")
			ref = Route([0,0,0], [0,0,0]) # set the sun as reference
		else:
			print("Chose " + str(reference) + " as reference point.")
		
				
		name = input("Name: ")
		# quit adding if blank input
		if name.strip() == "":
			print("User decided to stop adding a satellite.\n")
			return
		
		# Ask for mass
		while True:
			mass = input("Mass: ")
			mass = "".join(mass.split())
			try:
				mass = reading_functions.read_mass(mass)
				break
			except Exception as e:
				# quit adding if blank input
				if mass == "":
					print("User decided to stop adding a satellite.\n")
					return
				print("Catched an error with the following error message:")
				print("\t" + str(e))
		
		# Ask for position vector.
		while True:
			position = input("Position: ")
			position = "".join(position.split())
			try:
				position = reading_functions.read_position(position)
				break
			except Exception as e:
				# quit adding if blank input
				if position == "":
					print("User decided to stop adding a satellite.\n")
					return
				print("Catched an error with the following error message:")
				print("\t" + str(e))
				
		# Ask for velocity vector.
		while True:
			velocity = input("Velocity: ")
			velocity = "".join(velocity.split())
			try:
				velocity = reading_functions.read_velocity(velocity)
				break
			except Exception as e:
				# quit adding if blank input
				if velocity == "":
					print("User decided to stop adding a satellite.\n")
					return
				print("Catched an error with the following error message:")
				print("\t" + str(e))
				
		route = Route(position, velocity) + ref # add the reference
		satellite = Satellite(name, route, mass, SatState.ALIVE)
		self._simulation.solarsystem.add_satellite(satellite)
		self._begin_ss.add_satellite(satellite, False) # This is for the copy solar system, which is used in resetting simulation.
		
	def reset_simulation(self):
		self._simulation.set_solarsystem(self._begin_ss)
		self._simulation.set_time(0)
				


