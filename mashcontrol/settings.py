
#Run Flask application in Debug mode (reload the process on filechanges)
#This enables the Flask debugger but disables to ability to control the process externally (supervisor or PyDev debugger)
DEBUG = False
PORT = 5000


RECORDINGS_DIR = "/opt/data/brewzone/recordings"

#One wire ids of the DS1820 sensors, put 'None' if not connected
#from mashcontrol.sensors import DS1820
 
#SENSORS = {
#            'HLT': DS1820('28-00000481da8b'),
#            'BOIL':DS1820('28-00000481da8b'),
#            'MASHIN':DS1820('28-00000481a5f0'),
#            'MASHOUT':DS1820('28-0000048158b6')
#            }

from mashcontrol.sensors import Simulator
SENSORS = {
            'HLT': Simulator(),
            'BOIL':None,
            'MASHIN':Simulator(),
            'MASHOUT':Simulator()
            }


#from mashcontrol.regulators import heater
#HEATERS = {
#           'mash': heater.Heater(16)
#           }

from mashcontrol.regulators import heatersimulation
HEATERS = {
           'mash': heatersimulation.HeaterSimulation(16)
           }


#from mashcontrol.regulators import pump
#PUMPS = {
#         'mash': pump.Pump(22)
#         }


from mashcontrol.regulators import pumpsimulation
PUMPS = {
         'mash': pumpsimulation.PumpSimulation(18)
         }

from mashcontrol.regulators import PIController

HEATCONTROLLERS = {
                   'mash': PIController.PIController()
                   }