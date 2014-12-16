#!/usr/bin/env python
from monitor import Monitor
from optparse import OptionParser
import subprocess

if(__name__ == '__main__'):
	process = subprocess.Popen(['uname', '-I'], stdout=subprocess.PIPE)
	localhost_ip = process.stdout.read().strip()
	parser = OptionParser()
    	parser.add_option("-a", "--address", dest="address", default=localhost_ip,
     	                 help="ADDRESS of localhost", metavar="ADDRESS")
    	parser.add_option("-p", "--port", dest="port", type="int", default=2712, 
                         help="PORT of localhost to listen to", metavar="PORT")
        parser.add_option("-d", "--duration", dest="duration", type="int", default=10,
                         help="DURATION of experiment", metavar="DURATION")
	parser.add_option("-P", "--protocol", dest="protocol", default="UDP",
                         help="Communication PROTOCOL", metavar="PROTOCOL")
    	(options, args) = parser.parse_args()
        monitor = Monitor(ip=options.address, port=options.port,
			  duration=options.duration, connectionType=options.protocol)
        monitor.startUDPConnection()
