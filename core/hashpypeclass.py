# This file is part of the HashPype Suite.
#
#    HashPype is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    HashPype is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with HashPype.  If not, see <http://www.gnu.org/licenses/>.
#
# Completer handles the auto-completion features for HashPype
import Queue
from hashpypethread import *
from colours import *

class hashpype:
	
	def __init__(self, credentials, attack, com='cmd.exe', path='c:\\windows\\system32\\', threadcount=30, verbose=0):
		# Initiaite input and output queues for threads
		self.ip_queue = Queue.Queue()
		self.result_queue = Queue.Queue()
		self.credentials = credentials
		self.com = com
		self.path = path
		self.threadcount = threadcount
		self.attack = attack
		self.colours = colours()
		self.verbose = verbose

	def banner(self):
		print self.colours.cstring("\nHashPype Alpha 0.0.1\n" + "By: Phaedrus\n" + "Date: May 5, 2013\n" + "OpenWire Security LLC\n", "blue")

	def run(self):

		self.banner()
		
		# Populate input Queue for threads with list of IP Addresses
		for i in self.attack:
			self.ip_queue.put(i)

		# Initiate Threads
		print self.colours.cstring("Spawning " + str(self.threadcount) + " threads.", "light_blue")
		pool = [HashPypeThread(ip_q=self.ip_queue, result_q=self.result_queue, credentials=self.credentials, colours=self.colours, com=self.com, path=self.path, verbose=self.verbose) for i in range(self.threadcount)]
		for thread in pool:
			thread.start()
	
		# Parse Results
		
		while 1:
			check = raw_input("\rPlease wait for all threads to complete then type exit...:")
			if check.lower() == 'exit':
				break
		# Close Threads and close
		print self.colours.cstring("Closing up Threads this may take a few moments...", "green")
		for thread in pool:
			thread.join()
		print self.colours.cstring("BYE :D", "red")