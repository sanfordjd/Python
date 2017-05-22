import numpy as np
import cv2
import imutils
import sys
import matplotlib
from time import time, sleep
from serial import Serial

VERBOSE = True

class DeviceError(Exception):
    pass
class SyncError(DeviceError):
    pass
class ChecksumError(DeviceError):
    pass

class DKSB1015A(object):
	PacketWidth = 134

	def __init__(self, *args, **kwD):
		port = Serial(port='/dev/ttyUSB0', baudrate = 115200)
		self.port = port
		self.stopData()
		
	def startData(self):
		self.port.flushInput()
		self.port.write('*')
		self.port.flushOutput()
		
	def stopData(self):
		self.port.write('~')
		self.port.flushInput()
		self.port.flushOutput()	
	
	def array_from_data(self, data):
		data = unpack('h'*64, str(data))
		return fliplr(reshape(data,(8,8)))
	
	def average_data(self, data):
		if self.samples==0:
			self.adata = data
		else:
			self.adata = self.adata+data
		
		self.samples = self.samples+1
		
		if self.samples == self.numAvg:
			if self.numAvg > 1: 
				self.adata = self.adata/self.numAvg
				self.samples = 0
				return True
		else:
			return False
	def step(self):
		try:
			data, temp = self.read_packet()
		except DeviceError, e:
			print e
			return 
			
		if VERBOSE:
			detla = time()-self._startT
			print 'T=', temp[0]
			print '#%s'%self.numPackets, '%6.3f packets/sec'%(self.numPackets/delta)
		
		self.current_frame = self.array_from_data(data)
		#ret = self.average_data(self.current_frame)
		
		#for now, no data averaging 
		
	def _run(self,data):
		print data	
	
	def read_packet(self):
		self._synStream()
		chk = 0
		
		_read = self.port.read
		
		data = read(2)
		temp = unpack('h', str(data))
		chk = chk + sum(map(ord,data))
		
		data = _read(128)
		chk = chk + sum(map(ord,data))
		
		chksum = ord( _read(1) )
		chk = chk % 256
		if chk != chksum:
			print 'chksumT = %d, checksumR = %d'%(chksum, chk)
			print self.array_from_data(data)
            # could just go back to syncStream and try again later, and return no data
			raise ChecksumError('Bad checksum')	
		self.numPackets = self.numPackets + 1
		return data, temp
		
	def run(self, numAvg = 1, triggerL=(0, ), show=False, doLoop=True):
		if numAvg<1:
			numAvg=1
		self.numAvg = numAvg
		self.triggerL=triggerL
        self.show=show
        self.samples=0
        self.numPackets=0
        self.occupancy=False
        self.motion=False
        self.adata = None
        self.olddata=None
        # maybe delay this until plot window is up, otherwise introduce slight delay in plot
        self.startData() 
        self._startT=time()
        # thread this???? 
        while doLoop:
            self.step()		
       
	def quit(self):
		print 'Cleaning up...'
		self.stopData()

if __name__ == '__main__':
	import datetime
	theMap=DKSB1015A()
        
	theMap.run(numAvg=10, triggerL=(0,), show=True)		
		
