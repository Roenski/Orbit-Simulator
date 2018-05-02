

'''
Not used in the project!
'''

from PyQt5.Qt import *
from simulation import Simulation
import sys

class GUI(QMainWindow):
  
  def __init__(self):
    super().__init__()
    self.initUI()
    
  def initUI(self):
    self._simulation = Simulation()
    
    while True:
      self.start_menu = StartMenu(self)
      if self.read_planets():
        break
    self.main_menu = MainMenu(self)
    self.setCentralWidget(self.main_menu)
    self.setGeometry(300,300,300,150)
    self.setWindowTitle('Solar System Simulator')
    self.show()
    
  def read_planets(self):
    try:
      filename = self.start_menu.planetfile
      file = open(filename)
      self._simulation.solarsystem.read_planets(file)
      print("Planets read.")
      file.close()
      return True
    except Exception as e:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Critical)
      msg.setText("Encountered an error with the following message: ")
      msg.setInformativeText(str(e))
      msg.setStandardButtons(QMessageBox.Ok)
      msg.exec_()
      return False
    
class StartMenu2(QWidget):
  
  def __init__(self, parent):
    super().__init__(parent)
    self.initUI()
    
  def initUI(self):
    


class StartMenu(QInputDialog):
  
  def __init__(self, parent):
    super().__init__(parent)
    self.initUI()
    
  def initUI(self):
    
    self.filename = ""
    filebut = QPushButton()
    filebut.clicked.connect(self.show_files)
    
    qr = self.frameGeometry()
    cp = QDesktopWidget().screenGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())
    
    self.planetfile = ""
    text, ok = self.getText(self, 'Solar System Simulator', 'Please enter the planet file:')
    if ok:
      self.planetfile += str(text)
    else:
      exit("User decided to close the program.")
      
  def show_files(self):
    self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')


class MainMenu(QWidget):

  def __init__(self, parent):
    super().__init__(parent)
    self.initUI()
    
  def initUI(self):
    
    addSatBut = QPushButton("Add a satellite")
    addSatBut.clicked.connect(self.add_satellite)
    
    remSatBut = QPushButton("Remove a satellite")
    remSatBut.clicked.connect(self.remove_satellite)
    
    chaPlaFilBut = QPushButton("Change the planet file")
    chaPlaFilBut.clicked.connect(self.change_planet_file)
    
    chaSimSetBut = QPushButton("Change simulation settings")
    chaSimSetBut.clicked.connect(self.change_simulation_settings)
    
    simBut = QPushButton("Simulate")
    simBut.clicked.connect(self.simulate)
    
    vbox = QVBoxLayout()
    vbox.addWidget(addSatBut)
    vbox.addWidget(remSatBut)
    vbox.addWidget(chaPlaFilBut)
    vbox.addWidget(chaSimSetBut)
    vbox.addWidget(simBut)
    #vbox.addStretch()
    
    self.setLayout(vbox)

  def add_satellite(self):
    print("Add satellite pressed.")
    
  def remove_satellite(self):
    print("Remove satellite pressed.")
    
  def change_planet_file(self):
    print("Change planet file pressed.")
    
  def change_simulation_settings(self):
    print("Change simulation settings pressed.")
    
  def simulate(self):
    print("Simulate pressed.")
    
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
    
    
