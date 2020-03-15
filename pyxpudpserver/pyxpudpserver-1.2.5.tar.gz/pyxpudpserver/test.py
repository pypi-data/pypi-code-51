import XPlaneUDPServer as XPUDP
pyXPUDPServer = XPUDP.XPlaneUDPServer()
pyXPUDPServer.initialiseUDP(('127.0.0.1',49008), ('192.168.1.146',49000), 'STEPHANESIMPC')
# # where ('127.0.0.1',49008) is the IP and port this class is listening on (configure in the Net connections in XPlane)
# # and ('192.168.1.1',49000) is the IP and port of XPlane
# # 'MYPC' is the name of the computer XPlane is running on
# # You can also initialise from an XML configuration file:
# XPUDP.pyXPUDPServer.initialiseUDPXMLConfig('UDPSettings.xml')
#
pyXPUDPServer.start() # start the server which will run an infinite loop
#

while True: # infinite loop - for a real application plan for a 'proper' way to exit the programme and break this loop
    value = pyXPUDPServer.getData((17,3)) 	# read the value sent by XPlane for datagroup 17, position 4 (mag heading)
    #print(value)
    
# 	transp_mode = XPUDP.pyXPUDPServer.getData("sim/cockpit2/radios/actuators/transponder_mode[0]") # gets the value of this dataref in XPlane
#
#	XPUDP.pyXPUDPServer.sendXPCmd('sim/engines/engage_starters') # send command to XPlane to engage the engine starters
#	XPUDP.pyXPUDPServer.sendXPDref("sim/flightmodel/controls/flaprqst", 0, value = 0.5) # set the requested flap deployment to 0.5 - bear in mind the flap will then deploy and take some time to do so - monitor its actual position if needed
#
pyXPUDPServer.quit() # exit the server thread and close the sockets
