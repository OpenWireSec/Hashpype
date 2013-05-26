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
import threading
from time import sleep
import Queue
import psexec
import random

class HashPypeThread(threading.Thread):

	# Modify the defaults here to alter the psexec functionality used by threads
	def __init__(self, ip_q, result_q, credentials, colours, com='whoami', path='c:\\windows\\system32\\', verbose=0):
		super(HashPypeThread, self).__init__()
		self.stoprequest = threading.Event()
		self.ip_q = ip_q
		self.result_q = result_q
		self.credentials = credentials
		self.com = com
		self.path = path
		self.colours = colours
		self.verbose = verbose
		
	def run(self):
		while not self.stoprequest.isSet():
			try:
				ip = self.ip_q.get(True, 0.05)
				self.process(ip)
				#self.result_q.put((results, ip))
				sleep(random.randint(1,5))

			except Queue.Empty:
				continue

	def join(self, timeout=None):
		self.stoprequest.set()
		super(HashPypeThread, self).join(0.05)

	def process(self, ip):
		#Do stuff with the server here
		for user, auth in self.credentials:
			if self.verbose == 1:
				print self.colours.cstring("Attempting to auth with " + ip + " using Username: " + user + " And Auth: " + auth, "light_blue")
			if len(auth) == 65 and ':' in auth:
				psobject = psexec.PSEXEC(self.com, self.path, "445/SMB", username=user, hashes=auth)
			else:
				psobject = psexec.PSEXEC(self.com, self.path, "445/SMB", username=user, password=auth)
			try:
				psobject.run(ip)			
			except:
				continue